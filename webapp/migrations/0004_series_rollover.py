# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_round_round_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='rollover',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=8),
        ),
    ]
