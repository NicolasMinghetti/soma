# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChoixDeObjectif',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif2a',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif2b',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif2c',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif3',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif3a',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif3b',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='objectif3c',
        ),
    ]
