# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20161206_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='profile_url',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]