# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitarra', '0016_guitarra_preu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarra',
            name='preu',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
