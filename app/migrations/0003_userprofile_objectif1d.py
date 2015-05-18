# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150518_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='objectif1d',
            field=models.CharField(max_length=30, default='NULL'),
            preserve_default=False,
        ),
    ]
