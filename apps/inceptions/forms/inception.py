# -*- coding: utf-8 -*-
#
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Inception
from common.utils import get_logger

logger = get_logger(__file__)
__all__ = ['InceptionCreateForm', 'InceptionUpdateForm', 'InceptionBulkUpdateForm']


class InceptionCreateForm(forms.ModelForm):
    class Meta:
        model = Inception
        fields = [
            'user', 'password', 'host', 'port',  'type',
            'purpose', 'is_active', 'protection_user', 'comment'

        ]
        widgets = {

            'port': forms.TextInput(),
            'user': forms.TextInput,
            'password': forms.PasswordInput,
            'host': forms.TextInput,
            'comment': forms.TextInput

        }

        help_texts = {
            'host': '* required',
            'password': '* required',
            'port': '* required',
            'user': '* required'

        }


class InceptionUpdateForm(forms.ModelForm):
    class Meta:
        model = Inception
        fields = [
            'user', 'password', 'host', 'port',  'type',
            'purpose', 'is_active', 'protection_user', 'comment'

        ]
        widgets = {

            'port': forms.TextInput(),
            'user': forms.TextInput,
            'password': forms.PasswordInput,
            'host': forms.TextInput,
            'comment': forms.TextInput

        }

        help_texts = {
            'host': '* required',
            'password': '* required',
            'port': '* required',
            'user': '* required'

        }


class InceptionBulkUpdateForm(forms.ModelForm):
    inceptions = forms.ModelMultipleChoiceField(
        required=True, help_text='* required',
        label=_('Select inceptions'), queryset=Inception.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'select2',
                'data-placeholder': _('Select assets')
            }
        )
    )
    port = forms.IntegerField(
        label=_('Port'), required=False, min_value=1, max_value=65535,
    )

    class Meta:
        model = Inception
        fields = [
            'user', 'password', 'host', 'port',  'type',
            'purpose', 'is_active', 'protection_user', 'comment'
        ]


    def save(self, commit=True):
        changed_fields = []
        for field in self._meta.fields:
            if self.data.get(field) not in [None, '']:
                changed_fields.append(field)

        cleaned_data = {k: v for k, v in self.cleaned_data.items()
                        if k in changed_fields}
        inceptions = cleaned_data.pop('inceptions')

        inceptions = Inception.objects.filter(id__in=[incepion.id for incepion in inceptions])
        inceptions.update(**cleaned_data)


        return inceptions