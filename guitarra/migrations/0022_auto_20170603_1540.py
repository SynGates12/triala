# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-03 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitarra', '0021_guitarra_descripcio_guitarra'),
    ]

    operations = [
        migrations.AddField(
            model_name='grup',
            name='amplis',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='grup',
            name='pedals',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
