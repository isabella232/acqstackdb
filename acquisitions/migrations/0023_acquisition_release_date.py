# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acquisitions', '0022_acquisition_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='acquisition',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]