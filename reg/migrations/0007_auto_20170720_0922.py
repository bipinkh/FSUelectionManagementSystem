# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0006_auto_20170719_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.FileField(upload_to='student-photo'),
        ),
    ]