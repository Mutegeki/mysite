# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-13 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycar', '0010_service_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='car',
        ),
    ]
