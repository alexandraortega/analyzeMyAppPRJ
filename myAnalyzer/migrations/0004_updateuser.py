# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-29 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAnalyzer', '0003_remove_users_userfolder'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('lastname', models.FileField(upload_to=b'')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
