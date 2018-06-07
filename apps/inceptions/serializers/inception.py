# -*- coding: utf-8 -*-
#
from rest_framework import serializers
from rest_framework_bulk.serializers import BulkListSerializer

from common.mixins import BulkSerializerMixin
from ..models import Inception


__all__ = [
    'InceptionSerializer', 'InceptionGrantedSerializer', 'MyInceptionGrantedSerializer',
]


class InceptionSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    """
    资产的数据结构
    """
    class Meta:
        model = Inception
        list_serializer_class = BulkListSerializer
        fields = '__all__'
        validators = []  # If not set to [], partial bulk update will be error

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)

        return fields


class InceptionGrantedSerializer(serializers.ModelSerializer):
    """
    被授权资产的数据结构
    """

    # nodes = NodeTMPSerializer(many=True, read_only=True)

    class Meta:
        model = Inception
        fields = (
            'user', 'password', 'host', 'port', 'type',
            'purpose', 'is_active', 'protection_user', 'comment'
        )




class MyInceptionGrantedSerializer(InceptionGrantedSerializer):
    """
    普通用户获取授权的资产定义的数据结构
    """

    class Meta:
        model = Inception
        fields = (
            'user', 'password', 'host', 'port',  'type',
            'purpose', 'is_active', 'protection_user', 'comment'
        )