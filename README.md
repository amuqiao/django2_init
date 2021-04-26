# django_init

Django项目开发模板

安装`Django`环境,在`django_init`目录下创建`django_init`项目
```
cd django_init
source venv/bin/active
django-admin startproject django_init

(venv) ➜  django_init git:(main) ✗ tree
.
├── django_init
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

```
启动服务
```
python3 manage.py runserver 0.0.0.0:8001
```


配置
```python
# 允许所有主机访问
ALLOWED_HOSTS = ['0.0.0.0']
```