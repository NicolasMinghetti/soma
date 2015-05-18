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
            name='ChoixDeObjectif',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('objectifa', models.CharField(max_length=10)),
                ('objectifb', models.CharField(max_length=30)),
                ('objectifc', models.CharField(max_length=30)),
                ('objectifd', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('photo', models.TextField()),
                ('objectif1', models.CharField(max_length=10)),
                ('objectif1a', models.CharField(max_length=30)),
                ('objectif1b', models.CharField(max_length=30)),
                ('objectif1c', models.CharField(max_length=30)),
                ('objectif2', models.CharField(max_length=10)),
                ('objectif2a', models.CharField(max_length=30)),
                ('objectif2b', models.CharField(max_length=30)),
                ('objectif2c', models.CharField(max_length=30)),
                ('objectif3', models.CharField(max_length=10)),
                ('objectif3a', models.CharField(max_length=30)),
                ('objectif3b', models.CharField(max_length=30)),
                ('objectif3c', models.CharField(max_length=30)),
                ('user', models.ForeignKey(related_name='profile', unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
