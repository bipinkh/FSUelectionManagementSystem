# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0011_auto_20170722_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]