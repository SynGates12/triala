# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitarra', '0009_guitarra_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitarra',
            name='estil',
        ),
        migrations.AddField(
            model_name='guitarra',
            name='estil',
            field=models.ManyToManyField(to='guitarra.Estil_musica'),
        ),
        migrations.RemoveField(
            model_name='guitarra',
            name='grup',
        ),
        migrations.AddField(
            model_name='guitarra',
            name='grup',
            field=models.ManyToManyField(to='guitarra.Grup'),
        ),
    ]
