# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_auto_20180608_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
