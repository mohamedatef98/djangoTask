# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20170930_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='isFavorite',
            field=models.BooleanField(default=False),
        ),
    ]
