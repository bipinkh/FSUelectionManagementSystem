# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0008_auto_20170722_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='symbol',
            field=models.FileField(upload_to='candidate-symbol'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='voter_id',
            field=models.IntegerField(blank=True),
        ),
    ]
