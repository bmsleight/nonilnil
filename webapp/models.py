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

    class Meta:
        ordering = ['id']


class Series(models.Model):
    # Include in Admin
    series_name = models.CharField(max_length=200, help_text='Name of series of games')
    series_open = models.BooleanField(default=True)
    entry_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rollover = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    end_message = models.TextField(null=True, blank=True, help_text="A Message to include at end of series (e.g. Winner: HHH, after 8 rounds")

    def __str__(self):              # __unicode__ on Python 2
        return self.series_name
    class Meta:
        ordering = ['-id']
  
class Round(models.Model):
    # Include in Admin
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    round_date = models.DateTimeField('Date games will be played on')
    round_open = models.BooleanField(default=True)
    email_message = models.TextField(null=True, blank=True, help_text="A Message to include in the email")

    def __str__(self):              # __unicode__ on Python 2
        return self.series.series_name + " " + str(self.round_date)
    class Meta:
        ordering = ['-round_date']


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
    class Meta:
        ordering = ['series']

class Prediction(models.Model):
    # User form - the only one ?
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.user) + " " + str(self.round_f) + " " + str(self.team)
    def failed(self):
        possible_nilnils = Nilnils.objects.filter(round_f=self.round_f, team=self.team)[:1]
        if possible_nilnils:
            return(Nilnils.objects.get(round_f=self.round_f, team=self.team).ohno)
        else:
            return(False)
    class Meta:
        ordering = ['round_f']


class Nilnils(models.Model):
    # Superuser form, list teams select from that round and edit the ohno by exception
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    ohno = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.round_f) + " " + str(self.team) + " " + str(self.ohno)
    class Meta:
        ordering = ['round_f']

