# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_contestant_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='current_que_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contestant',
            name='first_login',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contestant',
            name='que_array',
            field=models.TextField(default=''),
        ),
    ]
