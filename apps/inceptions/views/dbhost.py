# coding:utf-8
from __future__ import absolute_import, unicode_literals

import csv
import json
import uuid
import codecs
import chardet
from io import StringIO


from django.conf import settings
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin

from common.mixins import JSONResponseMixin
from common.utils import get_object_or_none, get_logger, is_uuid
from common.const import create_success_msg, update_success_msg
from .. import forms
from ..models import DbHost
# from ..hands import AdminUserRequiredMixin


__all__ = [
    'DbHostListView', 'DbHostCreateView', 'DbHostUpdateView','DbHostDeleteView','DbHostDetailView'
]
logger = get_logger(__file__)


class DbHostListView(TemplateView):
    template_name = 'inceptions/category_list.html'

    def get_context_data(self, **kwargs):

        context = {
            'app': _('DbHosts'),
            'action': _('DbHost list'),

        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)




class DbHostCreateView(SuccessMessageMixin, CreateView):
    model = DbHost
    form_class = forms.DbHostCreateForm
    template_name = 'inceptions/category_create_update.html'
    success_url = reverse_lazy('inceptions:dbhost-list')


    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        return form

    def get_context_data(self, **kwargs):
        context = {
            'app': _('DbHosts'),
            'action': _('Create dbhost'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return create_success_msg % ({"name": cleaned_data["connection_name"]})






class DbHostUpdateView( SuccessMessageMixin, UpdateView):
    model = DbHost
    form_class = forms.DbHostUpdateForm
    template_name = 'inceptions/category_create_update.html'
    success_url = reverse_lazy('inceptions:dbhost-list')

    def get_context_data(self, **kwargs):
        context = {
            'app': _('DbHosts'),
            'action': _('Update dbhost'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return update_success_msg % ({"name": cleaned_data["connection_name"]})


class DbHostDeleteView( DeleteView):
    model = DbHost
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('inceptions:dbhost-list')


class DbHostDetailView(DetailView):
    model = DbHost
    context_object_name = 'dbhost'
    template_name = 'inceptions/dbhost_detail.html'

    def get_context_data(self, **kwargs):

        context = {
            'app': _('DbHosts'),
            'action': _('DbHost detail')

        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)




