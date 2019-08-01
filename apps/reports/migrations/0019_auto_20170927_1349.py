# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0018_auto_20170927_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='conversion_type',
            field=models.CharField(choices=[('cpa', 'Conversions by Lead Value'), ('conversion_margin', 'New - Conversions by Margins')], default='cpa', max_length=17),
        ),
    ]
