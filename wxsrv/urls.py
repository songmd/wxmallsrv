from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^callback$', views.callback, name='callback'),
    url(r'^orderquery$', views.order_query, name='orderquery'),
    url(r'^downloadbill$', views.download_bill, name='downloadbill'),
    url(r'^refund$', views.refund, name='refund'),
    url(r'^refundquery$', views.refund_query, name='refund_query'),
    url(r'^comment$', views.pull_comment, name='pull_comment'),
    # url(r'^user/(?P<user_id>[a-zA-Z0-9_]+)/$', views.user, name='user'),
]
