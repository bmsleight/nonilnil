# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20160107_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='round_open',
            field=models.BooleanField(default=True),
        ),
    ]
