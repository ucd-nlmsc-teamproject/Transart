# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headline', models.CharField(blank=True, max_length=500)),
                ('SubHeadline', models.CharField(blank=True, max_length=1000)),
                ('Url', models.URLField(blank=True, max_length=400, null=True, unique=True)),
                ('DateTime', models.DateTimeField(db_index=True, verbose_name='date published')),
                ('Keywords', models.CharField(max_length=5000)),
                ('Content', models.TextField(blank=True)),
                ('Type', models.CharField(db_index=True, max_length=100)),
                ('Source', models.CharField(max_length=100)),
            ],
        ),
    ]
