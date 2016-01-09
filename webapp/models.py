from django.db import models
from django.conf import settings 

# Create your models here.

class Fgroup(models.Model):
    # Include in Admin
    # examples, English League, champions league 2017
    DEFAULT_PK=1
    group_name = models.CharField(max_length=200, help_text='Name of group, e.g. Champions League')

    def __str__(self):              # __unicode__ on Python 2
        return self.group_name

class Team(models.Model):
    # Include in Admin
    # The list of eligable teams, e.g. English football
    # Some team may drop out of the league  - tough luck
    fgroup = models.ForeignKey(Fgroup, on_delete=models.CASCADE, default=Fgroup.DEFAULT_PK)
    team_name = models.CharField(max_length=200, help_text='Name of Team')

    def __str__(self):              # __unicode__ on Python 2
        return self.team_name

class Series(models.Model):
    # Include in Admin
    series_name = models.CharField(max_length=200, help_text='Name of series of games')
    series_open = models.BooleanField(default=True)
    entry_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rollover = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    end_message = models.TextField(null=True, blank=True, help_text="A Message to include at end of series (e.g. Winner: HHH, after 8 rounds")

    def __str__(self):              # __unicode__ on Python 2
        return self.series_name
  
class Round(models.Model):
    # Include in Admin
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    round_date = models.DateTimeField('Date games will be played on')
    round_open = models.BooleanField(default=True)
    email_message = models.TextField(null=True, blank=True, help_text="A Message to include in the email")

    def __str__(self):              # __unicode__ on Python 2
        return self.series.series_name + " " + str(self.round_date)

class Emailround(models.Model):
    # Include in Admin in case of error.
    # Slowly notify users of new round. 
    # Cron job ?
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    sent = models.BooleanField(default=True)

class Payment(models.Model):
    # Include in Admin
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

class PredictionManager(models.Manager):
    def with_nonilnil(self):
        print ("ping ")
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT p.id, p.user_id, p.round_f_id, n.ohno
            FROM webapp_prediction p, webapp_nilnils n
            WHERE p.round_f_id = n.round_f_id
            GROUP BY p.id, p.user_id, p.round_f_id
            ORDER BY p.id DESC""")
        result_list = []
        print ("RL ", result_list)
        for row in cursor.fetchall():
            p = self.model(id=row[0], user_id=row[1], round_f_id=row[2])
            p.ohno = row[3]
            result_list.append(p)
        return result_list

class Prediction(models.Model):
    # User form - the only one ?
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    objects = PredictionManager()

class Nilnils(models.Model):
    # Superuser form, list teams select from that round and edit the ohno by exception
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ohno = models.BooleanField(default=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.round_f) + " " + str(self.team) + " " + str(self.ohno)
