# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namebytyping', '0004_auto_20160303_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test_type',
            field=models.CharField(default='n/a', max_length=200),
        ),
    ]