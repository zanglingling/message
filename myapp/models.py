# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Messsge(models.Model):
    username = models.CharField(u'姓名', max_length=30)
    email = models.EmailField(u'邮箱')
    address = models.CharField(u'地址', max_length=50)
    message = models.CharField(u'留言', max_length=100)
    creat_time = models.DateTimeField(u'留言时间', auto_now=True)

    class Meta:
        verbose_name = u'留言'
        verbose_name_plural = u'留言集'
