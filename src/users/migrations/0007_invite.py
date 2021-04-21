# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import app


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20180522_0931'),
        ('users', '0006_auto_20180522_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('hash', models.CharField(default=app.utils.create_hash, max_length=100,
                                          unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True,
                                                      verbose_name=b'DateCreated')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                   to='api.Organisation')),
            ],
        ),
    ]
