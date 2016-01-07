# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emailround',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sent', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('series', models.ForeignKey(to='webapp.Series')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('round_date', models.DateTimeField(verbose_name='Date games will be played on')),
                ('email_message', models.TextField(blank=True, help_text='A Message to include in the email', null=True)),
                ('series', models.ForeignKey(to='webapp.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('team_name', models.CharField(help_text='Name of Team', max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Fgroups',
            new_name='Fgroup',
        ),
        migrations.RenameModel(
            old_name='Predictions',
            new_name='Prediction',
        ),
        migrations.RemoveField(
            model_name='emailrounds',
            name='round_f',
        ),
        migrations.RemoveField(
            model_name='emailrounds',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='series',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rounds',
            name='series',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='fgroup',
        ),
        migrations.AlterField(
            model_name='nilnils',
            name='round_f',
            field=models.ForeignKey(to='webapp.Round'),
        ),
        migrations.AlterField(
            model_name='nilnils',
            name='team',
            field=models.ForeignKey(to='webapp.Team'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='round_f',
            field=models.ForeignKey(to='webapp.Round'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='team',
            field=models.ForeignKey(to='webapp.Team'),
        ),
        migrations.DeleteModel(
            name='Emailrounds',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
        migrations.DeleteModel(
            name='Rounds',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
        migrations.AddField(
            model_name='team',
            name='fgroup',
            field=models.ForeignKey(default=1, to='webapp.Fgroup'),
        ),
        migrations.AddField(
            model_name='emailround',
            name='round_f',
            field=models.ForeignKey(to='webapp.Round'),
        ),
        migrations.AddField(
            model_name='emailround',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
