# Create your models here.
from django.db import models


class ShopInfo(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    shop_title = models.CharField(max_length=40)
    shop_desc = models.CharField(max_length=40)
    shop_addr = models.CharField(max_length=200)
    shop_time = models.CharField(max_length=40)
    shop_phone = models.CharField(max_length=40)
    shop_latitude = models.FloatField()
    shop_longitude = models.FloatField()
    shop_icon = models.ImageField(upload_to='shops')

    def __str__(self):
        return self.shop_title + '(' + self.shop_id + ')'


class Banner(models.Model):
    shop_info = models.ForeignKey(ShopInfo)
    banner_img = models.ImageField(upload_to='shops')

    def __str__(self):
        return self.banner_img.name


class ShopDetail(models.Model):
    shop_info = models.ForeignKey(ShopInfo)
    detail_img = models.ImageField(upload_to='shops')

    def __str__(self):
        return self.detail_img.name


class Notice(models.Model):
    shop_info = models.ForeignKey(ShopInfo)
    notice_content = models.CharField(max_length=240)

    def __str__(self):
        return self.notice_content


class GoodsInfo(models.Model):
    shop_info = models.ForeignKey(ShopInfo)
    goods_desc = models.CharField(max_length=40)
    goods_price = models.FloatField()
    goods_orignal_price = models.FloatField(blank=True, null=True)
    goods_img = models.ImageField(upload_to='shops')

    def __str__(self):
        return self.goods_desc


class GoodsDetail(models.Model):
    goods_info = models.ForeignKey(GoodsInfo)
    goods_img = models.ImageField(upload_to='shops')

    def __str__(self):
        return self.goods_img.name


class User2Shop(models.Model):
    user_id = models.CharField(max_length=40)
    shop_id = models.ForeignKey(ShopInfo)

    def __str__(self):
        return '%s   %s' % (self.user_id, self.shop_id)
