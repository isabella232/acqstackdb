# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('acquisitions', '0008_role'), ('acquisitions', '0009_role_acquisition'), ('acquisitions', '0010_auto_20160622_0918')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acquisitions', '0007_auto_20160617_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, choices=[('P', 'Product Lead'), ('A', 'Acquisition Lead'), ('T', 'Technical Lead')], max_length=100, null=True)),
                ('teammate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='acquisition',
            name='roles',
            field=models.ManyToManyField(to='acquisitions.Role'),
        ),
    ]
