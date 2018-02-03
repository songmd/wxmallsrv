# Register your models here.
from django.contrib import admin

from nested_inline.admin import NestedTabularInline, NestedModelAdmin

from .models import ShopInfo, Banner, Notice, GoodsInfo, GoodsDetail, ShopDetail,User2Shop

# from guardian.admin import GuardedModelAdmin

class BannerInline(NestedTabularInline):
    model = Banner
    extra = 1

class NoticeInline(NestedTabularInline):
    model = Notice
    extra = 1

class ShopDetailInline(NestedTabularInline):
    model = ShopDetail
    extra = 1


class GoodsDetailInline(NestedTabularInline):
    model = GoodsDetail
    extra = 1

class GoodsInfoInline(NestedTabularInline):
    model = GoodsInfo
    inlines = [GoodsDetailInline]
    extra = 1


class ShopInfoAdmin(NestedModelAdmin, admin.ModelAdmin):
    inlines = [BannerInline,NoticeInline,ShopDetailInline,GoodsInfoInline]
    list_display = ('shop_id', 'shop_title', 'shop_desc', 'shop_phone')
    def get_queryset(self, request):
        qs = super(ShopInfoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user2shop__user_id__contains=request.user)


    def get_actions(self, request):
        actions = super(ShopInfoAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['delete_selected']
        return actions


admin.site.register(ShopInfo, ShopInfoAdmin)
admin.site.register(User2Shop)
# admin.site.register(GoodsInfo,GoodsInfoAdmin)
# admin.site.register(GoodsDetail)
