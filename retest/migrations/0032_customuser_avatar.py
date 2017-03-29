# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retest', '0031_auto_20170326_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/images/avatars/', verbose_name='profile picture'),
        ),
    ]