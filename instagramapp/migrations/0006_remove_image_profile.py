# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-18 12:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0005_auto_20191018_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
