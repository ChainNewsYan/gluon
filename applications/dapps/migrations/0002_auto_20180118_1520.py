# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 07:20
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dapp',
            name='ico_status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='Planned', max_length=100, no_check_for_status=True),
        ),
        migrations.AddField(
            model_name='dapp',
            name='license',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='MIT', max_length=100, no_check_for_status=True),
        ),
        migrations.AddField(
            model_name='dapp',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='demo', max_length=100, no_check_for_status=True),
        ),
    ]
