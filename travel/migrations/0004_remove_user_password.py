# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-12 04:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
