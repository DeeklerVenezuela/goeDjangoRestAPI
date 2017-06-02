# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-02 13:15
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=20)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('price', models.FloatField(default=0.0)),
                ('currency', models.CharField(default='$', max_length=50)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Provider')),
            ],
        ),
    ]
