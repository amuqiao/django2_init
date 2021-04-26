# -*- coding: utf-8 -*-
# @Time    :2021/4/26 10:41 上午

from django.http import HttpResponse
from TestModel.models import Test


# 数据库操作
def insert(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def show(request):
    response = ""
    test_obs = Test.objects.all()
    for var in test_obs:
        response += f"id : {var.id} name: {var.name}\n"
    return HttpResponse("<p>" + response + "</p>")
