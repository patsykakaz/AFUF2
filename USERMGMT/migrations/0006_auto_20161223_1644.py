# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERMGMT', '0005_auto_20161216_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_naissance',
            field=models.CharField(max_length=255, null=True, verbose_name='date de naissance'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='semestre',
            field=models.CharField(blank=True, max_length=255, verbose_name='semestre commenc\xe9 en novembre 2016'),
        ),
    ]