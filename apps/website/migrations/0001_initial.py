# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_user_alert_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='The email address to which to send an email upon a new user registering.  Leave blank to not send an email.')),
            ],
        ),
    ]
