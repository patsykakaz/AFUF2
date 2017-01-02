#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
# from django.views.decorators.csrf import csrf_exempt 
# import views
from USERMGMT.views import *

urlpatterns = [
    # url(r'^payment_response/$', views.payment_response, name="payment_response"),
    url(r'^automatic_response/$', automatic_response, name="automatic_payment_response"),
    url(r'^manual_response/$', manual_response, name="manual_payment_response"),
    url(r'login/$', loginView, name='loginView'),
    url(r'logout/$', logoutView, name='logoutView'),
    url(r'^register/$', register, name="register"),
    url(r'^payment/$', payment, name="payment"),
    url(r'^test/$', test, name="test"),
    # url(r'^lol/$', views.lol, name="lol"),
]