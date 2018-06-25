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
from ..models import WikiComment
from users.models import User

from .. import forms

__all__ = ['CommentListView', 'CommentCreateView', 'CommentUpdateView', 'CommentDetailView']
logger = get_logger(__name__)


class CommentListView(TemplateView):
    template_name = 'wikis/comment_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Comments'),
            'action': _('Comment list')
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class CommentCreateView(SuccessMessageMixin, CreateView):
    model = WikiComment
    form_class = forms.WikiCommentForm
    template_name = 'wikis/comment_create_update.html'
    success_url = reverse_lazy('wikis:comment-list')
    success_message = create_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Comment'),
            'action': _('Create comment'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class CommentUpdateView(SuccessMessageMixin, UpdateView):
    model = WikiComment
    form_class = forms.WikiCommentForm
    template_name = 'wikis/comment_create_update.html'
    success_url = reverse_lazy('wikis:comment-list')
    success_message = update_success_msg

    def get_context_data(self, **kwargs):

        context = {
            'app': _('Comment'),
            'action': _('Update Comment'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class CommentDetailView(DetailView):
    model = WikiComment
    context_object_name = 'comment'
    template_name = 'wikis/comment_detail.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Comment'),
            'action': _('Comment  detail'),

        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)
#
#
# class CommentGrantedAssetView(AdminUserRequiredMixin, DetailView):
#     model = Comment
#     template_name = 'wikis/comment_granted_asset.html'
#     context_object_name = 'comment'
#     object = None
#
#     def get_context_data(self, **kwargs):
#         context = {
#             'app': _('Users'),
#             'action': _('User group granted asset'),
#         }
#         kwargs.update(context)
#         return super().get_context_data(**kwargs)
