# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-25 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatakelola', '0018_auto_20170425_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyek',
            name='status',
            field=models.CharField(choices=[('T', 'Diterima'), ('DT', 'Ditolak')], max_length=9),
        ),
    ]
