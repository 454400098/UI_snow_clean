# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snow', '0004_auto_20180419_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinput',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinput',
            name='loc',
            field=models.CharField(max_length=20),
        ),
    ]
