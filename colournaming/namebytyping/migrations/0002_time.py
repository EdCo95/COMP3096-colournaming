# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-21 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namebytyping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_elapsed', models.IntegerField(default=-1)),
            ],
        ),
    ]