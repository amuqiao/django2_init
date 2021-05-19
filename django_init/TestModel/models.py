from django.db import models
# from django.contrib.postgres.fields import JSONField

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)
    db_name = models.CharField("数据库名", max_length=255, null=True)
    table_name = models.CharField("表名", max_length=255, null=True)
    tag = models.JSONField('tag', null=True, blank=True)
    tag_desc = models.JSONField('tag_desc', null=True, blank=True)
    field = models.JSONField('field', null=True, blank=True)
    field_desc = models.JSONField('field_desc', null=True, blank=True)
