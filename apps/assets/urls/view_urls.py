from __future__ import absolute_import

from django.conf.urls import url

from .. import views

app_name = 'assets'

urlpatterns = [
    url(r'^idc$', views.IdcListView.as_view(), name='idc-list'),
    url(r'^idc/(?P<pk>[0-9a-zA-Z\-]{36})$', views.IdcDetailView.as_view(), name='idc-detail'),
    url(r'^idc/create$', views.IdcCreateView.as_view(), name='idc-create'),
    url(r'^idc/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.IdcUpdateView.as_view(), name='idc-update'),
    # url(r'^idc/(?P<pk>[0-9a-zA-Z\-]{36})/assets', views.IdcGrantedAssetView.as_view(), name='idc-granted-asset'),

    url(r'^cabinet$', views.CabinetListView.as_view(), name='cabinet-list'),
    url(r'^cabinet/(?P<pk>[0-9a-zA-Z\-]{36})$', views.CabinetDetailView.as_view(), name='cabinet-detail'),
    url(r'^cabinet/create$', views.CabinetCreateView.as_view(), name='cabinet-create'),
    url(r'^cabinet/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.CabinetUpdateView.as_view(), name='cabinet-update'),

    url(r'^asset$', views.AssetListView.as_view(), name='asset-list'),
    url(r'^asset/(?P<pk>[0-9a-zA-Z\-]{36})$', views.AssetDetailView.as_view(), name='asset-detail'),
    url(r'^asset/create$', views.AssetCreateView.as_view(), name='asset-create'),
    url(r'^asset/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.AssetUpdateView.as_view(), name='asset-update'),

    url(r'^assetgroup$', views.AssetgroupListView.as_view(), name='assetgroup-list'),
    url(r'^assetgroup/(?P<pk>[0-9a-zA-Z\-]{36})$', views.AssetgroupDetailView.as_view(), name='assetgroup-detail'),
    url(r'^assetgroup/create$', views.AssetgroupCreateView.as_view(), name='assetgroup-create'),
    url(r'^assetgroup/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.AssetgroupUpdateView.as_view(), name='assetgroup-update'),

]
