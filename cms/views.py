# Create your views here.
import json

from django.http import HttpResponse

from .models import ShowWindow


def index(request):
    resp = {}
    sw = ShowWindow.objects.get(pk='songmd')
    resp['id'] = sw.shop_id
    resp['title'] = sw.shop_title
    resp['desc'] = sw.shop_desc
    resp['addr'] = sw.shop_addr
    resp['time'] = sw.shop_time
    resp['phone'] = sw.shop_phone
    resp['latitude'] = sw.shop_latitude
    resp['longitude'] = sw.shop_longitude
    resp['icon'] = request.build_absolute_uri(sw.shop_icon.url)
    resp['goodsdetail'] = [request.build_absolute_uri(goodsdetail.goods_img.url) for goodsdetail in
                           sw.goodsdetail_set.all()]
    # print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")
    # return HttpResponse(json.dumps(sw), content_type="application/json")

def user(request, user_id):
    resp = {}
    sw = ShowWindow.objects.get(pk=user_id)
    resp['id'] = sw.shop_id
    resp['title'] = sw.shop_title
    resp['desc'] = sw.shop_desc
    resp['addr'] = sw.shop_addr
    resp['time'] = sw.shop_time
    resp['phone'] = sw.shop_phone
    resp['latitude'] = sw.shop_latitude
    resp['longitude'] = sw.shop_longitude
    resp['icon'] = request.build_absolute_uri(sw.shop_icon.url)
    resp['goodsdetail'] = [request.build_absolute_uri(goodsdetail.goods_img.url) for goodsdetail in
                           sw.goodsdetail_set.all()]
    # print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")