# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitarra', '0005_estil_musica_imatge'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitarra',
            name='descripcio_guitarra',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='guitarra',
            name='nom_guitarra',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
