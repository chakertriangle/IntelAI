# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-01 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPro3', '0006_auto_20191001_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=100),
        ),
    ]
