# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-18 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0004_auto_20191018_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
