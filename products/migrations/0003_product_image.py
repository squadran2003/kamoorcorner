# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170517_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default='', upload_to='uploads'),
        ),
    ]