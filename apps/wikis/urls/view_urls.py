from __future__ import absolute_import

from django.conf.urls import url

from .. import views

app_name = 'wikis'

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name='category-list'),
    url(r'^category$', views.CategoryListView.as_view(), name='category-list'),
    url(r'^category/(?P<pk>[0-9a-zA-Z\-]{36})$', views.CategoryDetailView.as_view(), name='category-detail'),
    url(r'^category/create$', views.CategoryCreateView.as_view(), name='category-create'),
    url(r'^category/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.CategoryUpdateView.as_view(), name='category-update'),
    # url(r'^category/(?P<pk>[0-9a-zA-Z\-]{36})/assets', views.CategoryGrantedAssetView.as_view(), name='category-granted-asset'),

]
