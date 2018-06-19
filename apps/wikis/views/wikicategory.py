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
from ..models import WikiCategory
from users.models import User

from .. import forms

__all__ = ['CategoryListView', 'CategoryCreateView', 'CategoryUpdateView', 'CategoryDetailView']
logger = get_logger(__name__)


class CategoryListView(TemplateView):
    template_name = 'wikis/category_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Categorys'),
            'action': _('Category list')
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = WikiCategory
    form_class = forms.WikeCategoryForm
    template_name = 'wikis/category_create_update.html'
    success_url = reverse_lazy('wikis:category-list')
    success_message = create_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Category'),
            'action': _('Create category'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = WikiCategory
    form_class = forms.WikeCategoryForm
    template_name = 'wikis/category_create_update.html'
    success_url = reverse_lazy('wikis:category-list')
    success_message = update_success_msg

    def get_context_data(self, **kwargs):
        wiki = User.objects.all()
        group_wiki = [user.id for user in self.object.wiki.all()]
        context = {
            'app': _('Category'),
            'action': _('Update Category'),
            'wikis': wiki,
            'group_wiki': group_wiki
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class CategoryDetailView(DetailView):
    model = WikiCategory
    context_object_name = 'category'
    template_name = 'wikis/category_detail.html'

    def get_context_data(self, **kwargs):
        wikis = User.objects.exclude(id__in=self.object.wikis.all()).exclude(role=User.ROLE_APP)
        context = {
            'app': _('Users'),
            'action': _('User group detail'),
            'wikis': wikis,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)
#
#
# class CategoryGrantedAssetView(AdminUserRequiredMixin, DetailView):
#     model = Category
#     template_name = 'wikis/category_granted_asset.html'
#     context_object_name = 'category'
#     object = None
#
#     def get_context_data(self, **kwargs):
#         context = {
#             'app': _('Users'),
#             'action': _('User group granted asset'),
#         }
#         kwargs.update(context)
#         return super().get_context_data(**kwargs)
