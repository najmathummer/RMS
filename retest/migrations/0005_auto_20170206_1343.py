# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0004_auto_20170205_2321'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Retest',
        ),
    ]