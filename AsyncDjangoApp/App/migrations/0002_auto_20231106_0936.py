# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2023-11-06 09:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='App_tasks',
        ),
    ]
