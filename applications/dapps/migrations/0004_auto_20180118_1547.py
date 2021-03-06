# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0003_auto_20180118_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='bitcointalk',
            field=models.URLField(default='', max_length=255, verbose_name='BitcoinTalk'),
        ),
        migrations.AddField(
            model_name='social',
            name='instagram',
            field=models.URLField(default='', max_length=255, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='social',
            name='linkedin',
            field=models.URLField(default='', max_length=255, verbose_name='LinkedIn'),
        ),
        migrations.AddField(
            model_name='social',
            name='telegram',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='social',
            name='youtube',
            field=models.URLField(default='', max_length=255),
        ),
    ]
