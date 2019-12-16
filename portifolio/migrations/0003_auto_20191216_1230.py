# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-16 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0002_category_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
        migrations.AddField(
            model_name='image',
            name='category_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/'),
            preserve_default=False,
        ),
    ]
