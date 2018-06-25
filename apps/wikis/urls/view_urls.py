from __future__ import absolute_import

from django.conf.urls import url

from .. import views

app_name = 'wikis'

urlpatterns = [
    url(r'^category$', views.CategoryListView.as_view(), name='category-list'),
    url(r'^category/(?P<pk>[0-9a-zA-Z\-]{36})$', views.CategoryDetailView.as_view(), name='category-detail'),
    url(r'^category/create$', views.CategoryCreateView.as_view(), name='category-create'),
    url(r'^category/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.CategoryUpdateView.as_view(), name='category-update'),
    # url(r'^category/(?P<pk>[0-9a-zA-Z\-]{36})/assets', views.CategoryGrantedAssetView.as_view(), name='category-granted-asset'),

    url(r'^comment$', views.CommentListView.as_view(), name='comment-list'),
    url(r'^comment/(?P<pk>[0-9a-zA-Z\-]{36})$', views.CommentDetailView.as_view(), name='comment-detail'),
    url(r'^comment/create$', views.CommentCreateView.as_view(), name='comment-create'),
    url(r'^comment/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.CommentUpdateView.as_view(), name='comment-update'),

    url(r'^post$', views.PostListView.as_view(), name='post-list'),
    url(r'^post/(?P<pk>[0-9a-zA-Z\-]{36})$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^post/create$', views.PostCreateView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.PostUpdateView.as_view(), name='post-update'),

    url(r'^tag$', views.TagListView.as_view(), name='tag-list'),
    url(r'^tag/(?P<pk>[0-9a-zA-Z\-]{36})$', views.TagDetailView.as_view(), name='tag-detail'),
    url(r'^tag/create$', views.TagCreateView.as_view(), name='tag-create'),
    url(r'^tag/(?P<pk>[0-9a-zA-Z\-]{36})/update$', views.TagUpdateView.as_view(), name='tag-update'),

]
