# -*- coding: utf-8 -*-
# @Time    :2021/4/26 10:41 上午

from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test
import simplejson as json
from random import randint


# 数据库操作
def insert(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def insert_json(request):
    db_name = "db_dsp"
    table_name = "tb_dsp"
    tag = {
        "statement_id": 0,
        "series": [
            {
                "name": "dsp",
                "columns": ["tagKey"],
                "values": [["host"], ["requesttype"], ["status"], ["url"]]
            }
        ]
    }
    tag_desc = {
        "series": [
            {
                "name": "dsp",
                "columns": ["tagKey"],
                "values": [["host", "主机"], ["requesttype", "请求类型"], ["status", "状态码"], ["url", "链接"]]
            }
        ]
    }
    field = {
        "statement_id": 1,
        "series": [
            {
                "name": "dsp",
                "columns": ["fieldKey", "fieldType"],
                "values": [["cost", "float"], ["pv", "float"], ["up_100", "float"], ["up_1000", "float"]]
            }
        ]
    }
    field_desc = {
        "statement_id": 1,
        "series": [
            {
                "name": "dsp",
                "columns": ["fieldKey", "fieldType"],
                "values": [["cost", "float", "开销"], ["pv", "float", "每秒请求量"], ["up_100", "float", "每百次请求数"],
                           ["up_1000", "float", "每千次请求数"]]
            }
        ]
    }
    test1 = Test(name='luffy' + str(randint(1, 1000)), db_name=db_name,table_name=table_name,
                 tag=(tag), tag_desc=(tag_desc),field=(field), field_desc=(field_desc))

    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def show(request):
    response = ""
    obs = Test.objects.all()
    # for var in test_obs:
    #     # tag:{var.tag}
    #     temp = f"id : {var.id} name: {var.name} \n"
    #     response += temp
    # return HttpResponse("<p>" + response + "</p>")

    for ob in obs:
        print(ob.tag)
    context = {
        "name": "show",
        "obs": obs
    }
    return render(request, 'test_db/show.html', context)