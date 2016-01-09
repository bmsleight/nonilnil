# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_series_rollover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nilnils',
            name='ohno',
            field=models.BooleanField(default=False),
        ),
    ]
