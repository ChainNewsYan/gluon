# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 05:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0007_repository_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RepositoryState',
            new_name='RepositoryStats',
        ),
    ]
