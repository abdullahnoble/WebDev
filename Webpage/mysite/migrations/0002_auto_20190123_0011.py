# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-22 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='research',
            new_name='designation',
        ),
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(default='xyz', max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='profilepic',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
