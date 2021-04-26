# -*- coding: utf-8 -*-
# @Time    :2021/4/26 10:41 上午

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")
