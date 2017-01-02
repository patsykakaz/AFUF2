#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from USERMGMT.forms import LoginForm


def loginForm(request):
    return {
        "loginForm": LoginForm()
    }