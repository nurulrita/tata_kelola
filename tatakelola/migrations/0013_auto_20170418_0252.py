# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-18 02:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tatakelola', '0012_auto_20170417_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='opd',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monitor',
            name='proyek',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tatakelola.Proyek'),
        ),
    ]