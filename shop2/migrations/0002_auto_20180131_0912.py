# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-31 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='goods_orignal_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
