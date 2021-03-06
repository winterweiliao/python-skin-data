# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-12 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20170812_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='market_hash_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='market_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tradeflow',
            name='market_hash_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tradeflow',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
