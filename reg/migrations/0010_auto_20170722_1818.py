# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0009_auto_20170722_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='voter_id',
            field=models.IntegerField(),
        ),
    ]
