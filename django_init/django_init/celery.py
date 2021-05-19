# -*- coding: utf-8 -*-
import os
from celery import Celery
# 设置django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_init.settings')

app = Celery('django_init')

# 使用CELERY作为前缀，在settings中写配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现任务,发现任务文件每个app下的task.py
app.autodiscover_tasks()
