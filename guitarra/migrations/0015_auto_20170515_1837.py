# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitarra', '0014_auto_20170515_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tremolo',
            name='tremolo',
            field=models.CharField(max_length=100),
        ),
    ]
