# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 14:00
from __future__ import unicode_literals

from django.db import migrations


def convert_to_micro_amounts(apps, schema_editor):
    Quote = apps.get_model('quotes', 'Quote')

    for quote in Quote.objects.all():
        quote.quote *= 10**6
        quote.save()


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20170912_1733'),
    ]

    operations = [
        migrations.RunPython(convert_to_micro_amounts),
    ]
