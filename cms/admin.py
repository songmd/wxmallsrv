# Register your models here.
from django.contrib import admin

from .models import ShowWindow, GoodsDetail


class DetailInline(admin.TabularInline):
    model = GoodsDetail
    extra = 3


class ShowWindowAdmin(admin.ModelAdmin):
    inlines = [DetailInline]
    list_display = ('shop_id', 'shop_title', 'shop_desc', 'shop_phone')

admin.site.register(ShowWindow, ShowWindowAdmin)
