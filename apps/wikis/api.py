#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
@version: ??
@author: chenwh
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: api.py.py
@time: 18-6-19 上午2:54
"""


from rest_framework import generics
from rest_framework.response import Response
from rest_framework_bulk import BulkModelViewSet
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q

from common.mixins import IDInFilterMixin
from common.utils import get_logger
from .models import WikiCategory
from . import serializers




logger = get_logger(__file__)
__all__ = [
    'CategoryViewSet'
]


class CategoryViewSet(IDInFilterMixin, BulkModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    filter_fields = ("name")
    search_fields = filter_fields
    ordering_fields = ("name")
    queryset = WikiCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = LimitOffsetPagination


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset