# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatakelola', '0003_kebijakan_monitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32)),
                ('nama', models.CharField(max_length=32)),
                ('usermane', models.CharField(max_length=32)),
                ('NIP', models.CharField(max_length=16)),
                ('jenis_user', models.CharField(choices=[('OPD', 'OPD'), ('KOM', 'Diskominfo')], max_length=32)),
            ],
        ),
    ]