# -*- coding: utf-8 -*-
#
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import DbHost
from common.utils import get_logger

logger = get_logger(__file__)
__all__ = ['DbHostCreateForm', 'DbHostUpdateForm']


class DbHostCreateForm(forms.ModelForm):
    class Meta:
        model = DbHost
        fields = [
            'connection_name', 'computer_room', 'db_host', 'port',  'username',
            'password', 'before', 'after', 'url'

        ]
        widgets = {

            'connection_name': forms.TextInput(),
            'db_host': forms.TextInput,
            'port': forms.PasswordInput,
            'username': forms.TextInput,
            'password': forms.TextInput

        }

        help_texts = {
            'connection_name': '* required',
            'db_host': '* required',
            'username': '* required',
            'password': '* required'

        }


class DbHostUpdateForm(forms.ModelForm):
    class Meta:
        model = DbHost
        fields = [
            'connection_name', 'computer_room', 'db_host', 'port',  'username',
            'password', 'before', 'after', 'url'

        ]
        widgets = {

            'connection_name': forms.TextInput(),
            'db_host': forms.TextInput,
            'port': forms.PasswordInput,
            'username': forms.TextInput,
            'password': forms.TextInput

        }

        help_texts = {
            'connection_name': '* required',
            'db_host': '* required',
            'username': '* required',
            'password': '* required'

        }


