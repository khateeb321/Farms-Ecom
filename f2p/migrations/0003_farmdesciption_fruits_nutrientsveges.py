# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-04 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('f2p', '0002_veges'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmDesciption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('veges_label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f2p.Veges')),
            ],
        ),
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('img', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='nutrientsVeges',
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
                ('vege', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f2p.Veges')),
            ],
        ),
    ]
