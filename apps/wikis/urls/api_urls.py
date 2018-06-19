#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~
#
from __future__ import absolute_import

from django.conf.urls import url
from rest_framework_bulk.routes import BulkRouter
from .. import api

app_name = 'wikis'

router = BulkRouter()
router.register(r'v1/categorys', api.CategoryViewSet, 'category')


urlpatterns = []

urlpatterns += router.urls


print(router.urls)