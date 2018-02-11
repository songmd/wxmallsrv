import json

from django.http import HttpResponse

from .models import ShopInfo


# Create your views here.
def user(request, user_id):
    resp = {}
    sw = ShopInfo.objects.get(pk=user_id)
    resp['id'] = sw.shop_id
    resp['title'] = sw.shop_title
    resp['desc'] = sw.shop_desc
    resp['addr'] = sw.shop_addr
    resp['time'] = sw.shop_time
    resp['phone'] = sw.shop_phone
    resp['latitude'] = sw.shop_latitude
    resp['longitude'] = sw.shop_longitude
    resp['icon'] = request.build_absolute_uri(sw.shop_icon.url)

    resp['banners'] = [request.build_absolute_uri(banner.banner_img.url) for banner in
                           sw.banner_set.all()]
    resp['notices'] = [notice.notice_content for notice in sw.notice_set.all()]

    resp['shopdetail'] = [request.build_absolute_uri(shopdetail.detail_img.url) for shopdetail in
                           sw.shopdetail_set.all()]
    resp['goods'] = []
    resp['show'] = True
    for goods in sw.goodsinfo_set.all():
        goodsinfo = {}
        goodsinfo['desc'] = goods.goods_desc
        goodsinfo['price'] = goods.goods_price
        if goods.goods_orignal_price:
            goodsinfo['original_price'] = goods.goods_orignal_price
        goodsinfo['img'] = request.build_absolute_uri(goods.goods_img.url)
        goodsinfo['detailimg'] = [request.build_absolute_uri(detail.goods_img.url) for detail in
                           goods.goodsdetail_set.all()]
        resp['goods'].append(goodsinfo)

    return HttpResponse(json.dumps(resp), content_type="application/json")
