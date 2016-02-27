# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('namebytyping', '0002_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, null=True)),
                ('path', models.FilePathField(path='.')),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius', models.IntegerField(default=20)),
                ('position_x', models.IntegerField(default=0)),
                ('position_y', models.IntegerField(default=0)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='namebytyping.Image')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('gender', models.IntegerField(choices=[(0, 'female'), (1, 'male')], default=0)),
                ('nationality', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='input_type',
            field=models.IntegerField(choices=[(0, 'spoken'), (1, 'typed')], default=0),
        ),
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='namebytyping.User'),
        ),
    ]
