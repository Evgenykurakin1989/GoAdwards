# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20170126_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='max_cpc_limit',
            field=models.PositiveIntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='target_cpa',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
