# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_imports', '0003_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.CharField(max_length=255),
        ),
    ]
