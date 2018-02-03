# Create your models here.
from django.db import models


class ShowWindow(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    shop_title = models.CharField(max_length=40)
    shop_desc = models.CharField(max_length=40)
    shop_addr = models.CharField(max_length=200)
    shop_time = models.CharField(max_length=40)
    shop_phone = models.CharField(max_length=40)
    shop_latitude = models.FloatField()
    shop_longitude = models.FloatField()
    shop_icon = models.ImageField(upload_to='ShowWindow')

    def __str__(self):
        return self.shop_title + '(' + self.shop_id + ')'


class GoodsDetail(models.Model):
    show_window = models.ForeignKey(ShowWindow)
    goods_img = models.ImageField(upload_to='ShowWindow')

    def __str__(self):
        return self.goods_img.name
