import json
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth import authenticate, login
import requests
from .wxpay import WeixinPay

# {"return_code": "SUCCESS", "return_msg": "OK", "appid": "wx773060da4bef94cc", "mch_id": "1498624892",
#  "nonce_str": "NsbBIuH5hotgYuWH", "sign": "95244E140C61782449E8D0F4F1485A2C", "result_code": "SUCCESS",
#  "transaction_id": "4200000069201802100373632281", "out_trade_no": "201802101138", "out_refund_no": "20180101",
#  "refund_id": "50000106042018021003556967366", "refund_channel": null, "refund_fee": "1", "coupon_refund_fee": "0",
#  "total_fee": "1", "cash_fee": "1", "coupon_refund_count": "0", "cash_refund_fee": "1"}

wpay = WeixinPay('wx773060da4bef94cc',
                 '1498624892',
                 '2sadf12312asdasd23wgfnbgd22desad',
                 'http://127.0.0.1:8000/wxsrv/callback',
                 key='/Users/hero101/9lcert/apiclient_key.pem',
                 cert='/Users/hero101/9lcert/apiclient_cert.pem')

def pull_comment(request):
    resp = {}
    resp = wpay.pull_comment('20180201000000','20180211000000')
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def refund_query(request):
    resp = {}
    resp = wpay.refund_query(out_trade_no='201802101138',
                       out_refund_no='20180101')
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")

def refund(request):
    resp = {}
    resp = wpay.refund(out_trade_no='201802101138',
                       out_refund_no='20180101',
                       total_fee=1,
                       refund_fee=1)
    print(resp)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def order_query(request):
    resp = {}
    resp = wpay.order_query(out_trade_no='201802101138')
    return HttpResponse(json.dumps(resp), content_type="application/json")


def download_bill(request):
    resp = {}
    resp = wpay.download_bill('20180201')
    return HttpResponse(json.dumps(resp), content_type="application/json")


def callback(request):
    pass


def index(request):
    resp = {}
    code = request.GET.get('code')
    print(code)
    print(request.user)
    user = authenticate(username='admin', password='mass432522')
    if user is not None:
        login(request, user)
    if code is not None:
        url = "https://api.weixin.qq.com/sns/jscode2session"
        args = dict()
        # 庭阶少儿
        # args.setdefault("appid", 'wx19adc662e6a39894')
        # args.setdefault("secret", '5a2f1c7a16e074b4d4c0f0a0d73dd670')

        # 九庐家居
        args.setdefault("appid", 'wx773060da4bef94cc')
        args.setdefault("secret", 'f3235f0ca506380edca7a3507148abf5')
        args.setdefault("js_code", code)
        args.setdefault("grant_type", "authorization_code")
        sess = requests.Session()
        resp = sess.get(url, params=args)
        data = json.loads(resp.content.decode("utf-8"))
        print(data)
        # data = Map(json.loads(resp.content.decode("utf-8")))
        print(resp)

        resp = wpay.jsapi(out_trade_no='201802101138',
                          body='腾讯-游戏',
                          total_fee=1,
                          trade_type='JSAPI',
                          openid=data['openid'],
                          limit_pay='no_credit')

        print(resp)
    code2 = request.GET.get('code2')
    print(code2)

    print(request.POST)

    return HttpResponse(json.dumps(resp), content_type="application/json")
