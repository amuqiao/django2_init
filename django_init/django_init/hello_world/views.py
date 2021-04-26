# -*- coding: utf-8 -*-
# @Time    :2021/4/26 10:41 上午

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")


def hello_2(request):
    context = {'hello': 'Hello World 2!'}
    return render(request, 'hello_world/index.html', context)
