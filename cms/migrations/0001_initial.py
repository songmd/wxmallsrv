# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_img', models.ImageField(upload_to='ShowWindow')),
            ],
        ),
        migrations.CreateModel(
            name='ShowWindow',
            fields=[
                ('shop_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('shop_title', models.CharField(max_length=40)),
                ('shop_desc', models.CharField(max_length=40)),
                ('shop_addr', models.CharField(max_length=200)),
                ('shop_time', models.CharField(max_length=40)),
                ('shop_phone', models.CharField(max_length=40)),
                ('shop_latitude', models.FloatField()),
                ('shop_longitude', models.FloatField()),
                ('shop_icon', models.ImageField(upload_to='ShowWindow')),
            ],
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='show_window',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.ShowWindow'),
        ),
    ]
