# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook_access_token',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='locale',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
