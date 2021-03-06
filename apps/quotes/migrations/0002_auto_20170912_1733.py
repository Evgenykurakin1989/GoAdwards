# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='monthly_adwords_spend',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Monthly Google Adwords Spend'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Quote'),
        ),
    ]
