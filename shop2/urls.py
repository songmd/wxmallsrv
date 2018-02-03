from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>[a-zA-Z0-9_]+)/$', views.user, name='user'),
]
