# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-10 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('f2p', '0007_auto_20170909_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='nutrientsFruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbohydrates', models.FloatField()),
                ('proteins', models.FloatField()),
                ('energy', models.FloatField()),
                ('fats', models.FloatField()),
                ('sugar', models.FloatField()),
                ('potassium', models.FloatField()),
                ('iron', models.FloatField()),
                ('calcium', models.FloatField()),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f2p.Fruits')),
            ],
        ),
    ]
