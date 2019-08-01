# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 14:09
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_modifiers', '0006_modifierprocesslog_is_dry_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordactionlog',
            name='modifier_data',
            field=jsonfield.fields.JSONField(help_text='Collection of variables used in modifiers. Helpful for debugging.', null=True),
        ),
        migrations.AddField(
            model_name='keywordevent',
            name='modifier_data',
            field=jsonfield.fields.JSONField(help_text='Collection of variables used in modifiers. Helpful for debugging.', null=True),
        ),
    ]
