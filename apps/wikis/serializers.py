# -*- coding: utf-8 -*-
#
from rest_framework import serializers
from rest_framework_bulk.serializers import BulkListSerializer

from common.mixins import BulkSerializerMixin
from .models import WikiCategory, WikiTag, WikiPost


__all__ = [
    'CategorySerializer', 'PostSerializer', 'TagSerializer'
]


class CategorySerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    资产的数据结构
    """
    class Meta:
        model = WikiCategory
        list_serializer_class = BulkListSerializer
        fields = '__all__'
        validators = []  # If not set to [], partial bulk update will be error

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)

        return fields


class TagSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    资产的数据结构
    """
    class Meta:
        model = WikiTag
        list_serializer_class = BulkListSerializer
        fields = '__all__'
        validators = []  # If not set to [], partial bulk update will be error

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)

        return fields


class PostSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    资产的数据结构
    """
    class Meta:
        model = WikiPost
        list_serializer_class = BulkListSerializer
        fields = '__all__'
        validators = []  # If not set to [], partial bulk update will be error

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)

        return fields



