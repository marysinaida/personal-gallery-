# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-16 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='category/'),
            preserve_default=False,
        ),
    ]
