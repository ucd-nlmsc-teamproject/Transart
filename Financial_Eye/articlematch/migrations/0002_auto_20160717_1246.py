# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-17 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articlematch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlematch',
            name='Match_News',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articlematch',
            name='News',
            field=models.IntegerField(),
        ),
    ]
