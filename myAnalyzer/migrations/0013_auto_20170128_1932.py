# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-28 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myAnalyzer', '0012_auto_20170128_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
