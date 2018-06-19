#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
@version: ??
@author: chenwh
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: models.py.py
@time: 18-6-19 上午2:21
"""


from __future__ import unicode_literals

from django.db import models

# Create your models here.

# from django.contrib.auth.models import User

# from users.models import User

from diting.settings import AUTH_USER_MODEL

class WikiCategory(models.Model):
    name = models.CharField(max_length=100,verbose_name='分类名称',unique=True)
    class Meta:
        db_table = 'wiki_category'
        verbose_name = 'wiki分类'
        verbose_name_plural = 'wiki分类'
    def __str__(self):
        return self.name



class WikiTag(models.Model):
    name = models.CharField(max_length=100,verbose_name='标签类型',unique=True)
    class Meta:
        db_table = 'wiki_tag'
        verbose_name = 'wiki标签'
        verbose_name_plural = 'wiki标签'
    def __str__(self):
        return self.name



class WikiPost(models.Model):
    title = models.CharField(max_length=70,verbose_name='标题',unique=True)
    content =  models.TextField(verbose_name='类容')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now_add=True,verbose_name='修改时间')
    category = models.ForeignKey(WikiCategory,verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(WikiTag, blank=True,verbose_name='标签')
    author = models.ForeignKey(AUTH_USER_MODEL,verbose_name='创建者',null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'wiki_post'
        verbose_name = 'wiki文章'
        verbose_name_plural = 'wiki文章'

    def __str__(self):
        return self.title


class WikiComment(models.Model):
    name = models.CharField(max_length=100,verbose_name='评论用户')
    email = models.EmailField(max_length=255,verbose_name='邮箱')
    url = models.URLField(blank=True,verbose_name='文章地址')
    text = models.TextField(verbose_name='文章类容')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    post = models.ForeignKey('WikiPost',verbose_name='文章id',null=True, on_delete=models.SET_NULL)
    class Meta:
        db_table = 'wiki_comment'

        verbose_name = 'wiki文章评论'
        verbose_name_plural = 'wiki文章评论'

    def __str__(self):
        return self.text[:20]