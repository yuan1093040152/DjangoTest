# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


#创建表
class Article(models.Model):
#创建表字段
    #标题
    title = models.CharField(max_length=32,default= 'Tetle')
    #内容（允许为空）
    content = models.TextField(null=True)

    #修改后台数据库字段默认显示名称
    def __unicode__(self):
        return self.title


