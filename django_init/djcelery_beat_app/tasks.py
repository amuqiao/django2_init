# -*- coding: utf-8 -*-
# @Time    :2021/5/18 5:48 下午

import time
from django_init import celery_app


@celery_app.task
def print_date():
    """定时打印时间"""
    timestamp = time.time()
    # 将时间戳转换为本地时间字符串
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    print(f"django_celery_beat 定时任务: 打印当前时间{time_str}")
