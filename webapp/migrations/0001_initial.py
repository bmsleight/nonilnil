# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emailrounds',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('sent', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('group_name', models.CharField(help_text='Name of group, e.g. Champions League', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Nilnils',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ohno', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('round_date', models.DateTimeField(verbose_name='Date games will be played on')),
                ('email_message', models.TextField(help_text='A Message to include in the email', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('series_name', models.CharField(help_text='Name of series of games', max_length=200)),
                ('series_open', models.BooleanField(default=True)),
                ('entry_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('end_message', models.TextField(help_text='A Message to include at end of series (e.g. Winner: HHH, after 8 rounds', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('team_name', models.CharField(help_text='Name of Team', max_length=200)),
                ('fgroup', models.ForeignKey(to='webapp.Fgroups', default=1)),
            ],
        ),
        migrations.AddField(
            model_name='rounds',
            name='series',
            field=models.ForeignKey(to='webapp.Series'),
        ),
        migrations.AddField(
            model_name='predictions',
            name='round_f',
            field=models.ForeignKey(to='webapp.Rounds'),
        ),
        migrations.AddField(
            model_name='predictions',
            name='team',
            field=models.ForeignKey(to='webapp.Teams'),
        ),
        migrations.AddField(
            model_name='predictions',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payments',
            name='series',
            field=models.ForeignKey(to='webapp.Series'),
        ),
        migrations.AddField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nilnils',
            name='round_f',
            field=models.ForeignKey(to='webapp.Rounds'),
        ),
        migrations.AddField(
            model_name='nilnils',
            name='team',
            field=models.ForeignKey(to='webapp.Teams'),
        ),
        migrations.AddField(
            model_name='emailrounds',
            name='round_f',
            field=models.ForeignKey(to='webapp.Rounds'),
        ),
        migrations.AddField(
            model_name='emailrounds',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
