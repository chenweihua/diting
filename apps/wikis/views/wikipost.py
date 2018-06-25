# ~*~ coding: utf-8 ~*~

from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext as _
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin

from common.utils import get_logger
from common.const import create_success_msg, update_success_msg
from ..models import WikiPost
from users.models import User

from .. import forms

__all__ = ['PostListView', 'PostCreateView', 'PostUpdateView', 'PostDetailView']
logger = get_logger(__name__)


class PostListView(TemplateView):
    template_name = 'wikis/post_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Posts'),
            'action': _('Post list')
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class PostCreateView(SuccessMessageMixin, CreateView):
    model = WikiPost
    form_class = forms.WikePostForm
    template_name = 'wikis/post_create_update.html'
    success_url = reverse_lazy('wikis:post-list')
    success_message = create_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Post'),
            'action': _('Create post'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = WikiPost
    form_class = forms.WikePostForm
    template_name = 'wikis/post_create_update.html'
    success_url = reverse_lazy('wikis:post-list')
    success_message = update_success_msg

    def get_context_data(self, **kwargs):

        context = {
            'app': _('Post'),
            'action': _('Update Post'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class PostDetailView(DetailView):
    model = WikiPost
    context_object_name = 'post'
    template_name = 'wikis/post_detail.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Post'),
            'action': _('Post  detail'),

        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)
#
#
# class PostGrantedAssetView(AdminUserRequiredMixin, DetailView):
#     model = Post
#     template_name = 'wikis/post_granted_asset.html'
#     context_object_name = 'post'
#     object = None
#
#     def get_context_data(self, **kwargs):
#         context = {
#             'app': _('Users'),
#             'action': _('User group granted asset'),
#         }
#         kwargs.update(context)
#         return super().get_context_data(**kwargs)
