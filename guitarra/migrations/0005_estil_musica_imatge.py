# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitarra', '0004_auto_20170511_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='estil_musica',
            name='imatge',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]