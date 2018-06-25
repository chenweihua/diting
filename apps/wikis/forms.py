#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
@version: ??
@author: chenwh
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: 
@software: PyCharm
@file: forms.py.py
@time: 18-6-19 上午2:25
"""

from django.utils.translation import gettext_lazy as _
from django import forms

from .models import *



class WikeCategoryForm(forms.ModelForm):
    class Meta:
        model = WikiCategory
        fields = [
            "name"
        ]

        help_texts = {
            'name': '* required',

        }

        widgets = {
            'name': forms.TextInput(),
        }

class WikeTagForm(forms.ModelForm):
    class Meta:
        model = WikiTag
        fields = [
            "name"
        ]

        help_texts = {
            'name': '* required',

        }

        widgets = {
            'name': forms.TextInput(),
        }

class WikePostForm(forms.ModelForm):
    class Meta:
        model = WikiPost
        fields = [
            "title", "content",  "category", "tags", "author",
        ]

        help_texts = {
            'title': '* required',
            "content": '* required',
            "category": '* required',
            "author":  '* required',

        }

        widgets = {
            'title': forms.TextInput(),
            "content": forms.Textarea(
                attrs={'cols': 80, 'rows': 10}
            ),
            "category": forms.Select(
                attrs={
                    'class': 'select2', 'data-placeholder': _('Catgory')
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    'data-placeholder': _('Join Tags')
                }

            ),
            "author": forms.Select(
                attrs={
                    'class': 'select2', 'data-placeholder': _('User')
                }
            )
        }


class WikiCommentForm(forms.ModelForm):
    class Meta:
        model = WikiComment
        fields = [
            "name", "email", "url", "text",  "post",
        ]

        help_texts = {
            'name': '* required',
            "email": '* required',
            "text": '* required',
            "post": '* required',

        }

        widgets = {
            'name': forms.TextInput(),
            "content": forms.Textarea(
                attrs={'cols': 80, 'rows': 4}
            ),
            "category": forms.Select(
                attrs={
                    'class': 'select2', 'data-placeholder': _('Catgory')
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    'data-placeholder': _('Join tag')
                }

            ),
            "author": forms.Select(
                attrs={
                    'class': 'select2', 'data-placeholder': _('user')
                }
            )
        }