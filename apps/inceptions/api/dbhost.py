# -*- coding: utf-8 -*-
#

from rest_framework import generics
from rest_framework.response import Response
from rest_framework_bulk import BulkModelViewSet
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q

from common.mixins import IDInFilterMixin
from common.utils import get_logger
# from ..hands import IsSuperUser, IsValidUser, IsSuperUserOrAppUser
from ..models import DbHost
from .. import serializers




logger = get_logger(__file__)
__all__ = [
    'DbHostViewSet', 'DbHostListUpdateApi'
]


class DbHostViewSet(IDInFilterMixin, BulkModelViewSet):
    """
    API endpoint that allows Inception to be viewed or edited.
    """
    filter_fields = ("host", "port")
    search_fields = filter_fields
    ordering_fields = ("host", "port","user")
    queryset = DbHost.objects.all()
    serializer_class = serializers.InceptionSerializer
    pagination_class = LimitOffsetPagination


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class DbHostListUpdateApi(IDInFilterMixin, ListBulkCreateUpdateDestroyAPIView):
    """
    Inception bulk update api
    """
    queryset = DbHost.objects.all()
    serializer_class = serializers.InceptionSerializer



