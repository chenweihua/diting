#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~
#
from __future__ import absolute_import

from django.conf.urls import url
from rest_framework_bulk.routes import BulkRouter
from .. import api

app_name = 'assets'

router = BulkRouter()
router.register(r'v1/idcs', api.CategoryViewSet, 'idc')
router.register(r'v1/cabinets', api.CategoryViewSet, 'cabinet')
router.register(r'v1/assets', api.CategoryViewSet, 'asset')
router.register(r'v1/assetgroups', api.CategoryViewSet, 'assetgroup')


urlpatterns = []

urlpatterns += router.urls
