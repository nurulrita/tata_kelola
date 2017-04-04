# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tatakelola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=128)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tatakelola.Section'),
        ),
    ]