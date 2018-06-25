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
from ..models import WikiTag
from users.models import User

from .. import forms

__all__ = ['TagListView', 'TagCreateView', 'TagUpdateView', 'TagDetailView']
logger = get_logger(__name__)


class TagListView(TemplateView):
    template_name = 'wikis/tag_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Tags'),
            'action': _('Tag list')
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class TagCreateView(SuccessMessageMixin, CreateView):
    model = WikiTag
    form_class = forms.WikeTagForm
    template_name = 'wikis/tag_create_update.html'
    success_url = reverse_lazy('wikis:tag-list')
    success_message = create_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Tag'),
            'action': _('Create tag'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class TagUpdateView(SuccessMessageMixin, UpdateView):
    model = WikiTag
    form_class = forms.WikeTagForm
    template_name = 'wikis/tag_create_update.html'
    success_url = reverse_lazy('wikis:tag-list')
    success_message = update_success_msg

    def get_context_data(self, **kwargs):

        context = {
            'app': _('Tag'),
            'action': _('Update Tag'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class TagDetailView(DetailView):
    model = WikiTag
    context_object_name = 'tag'
    template_name = 'wikis/tag_detail.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Tag'),
            'action': _('Tag  detail'),

        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)
#
#
# class TagGrantedAssetView(AdminUserRequiredMixin, DetailView):
#     model = Tag
#     template_name = 'wikis/tag_granted_asset.html'
#     context_object_name = 'tag'
#     object = None
#
#     def get_context_data(self, **kwargs):
#         context = {
#             'app': _('Users'),
#             'action': _('User group granted asset'),
#         }
#         kwargs.update(context)
#         return super().get_context_data(**kwargs)
