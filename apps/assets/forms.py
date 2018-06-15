#! /usr/bin/env python
# ~*~ coding: utf-8 ~*~

from django import forms

from .models import *



class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            "hostname", 'manager_ip', 'idc' ,'wlan_ip', 'asset_type', 'status', 'env', 'port', 'adminuser', 'category', 'business'
        ]

        help_texts = {
            'hostname': '* required',
            'manager_ip': '* required',
            'idc': '* required',
            'status': '* required',
            'port': '* required',
        }

        widgets = {
            'hostname': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'manager_ip': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'wlan_ip': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'asset_type': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'idc': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'status': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'env': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'port': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'adminuser': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'business': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'category': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'})
        }



class AssetInfoForm(forms.ModelForm):
    class Meta:
        model = AssetInfo

        fields = [
            "os", 'vendor', 'cpu_model', 'memory', 'disk', 'sn', 'asset_no', 'price', 'buy_time', 'cpu_num',
            'postion', 'remark'
        ]



        help_texts = {
            'username': '* required',
            'name': '* required',
            'email': '* required',
        }

        widgets = {
            'asset_no': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'os': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'vendor': forms.Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'cpu_model': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'cpu_num': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'memory': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'disk': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'sn': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'price': forms.DecimalField(),
            "buy_time": forms.DateTimeField(input_formats="Y-%m-%d %H:%M:%S"),
            'position': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'物理机写位置，虚机写宿主'}),
            'remark': forms.Textarea(
                attrs={'cols': 80, 'rows': 4}
            ),
        }





class IdcForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(IdcForm, self).clean()
        value = cleaned_data.get('name')
        try:
            Idc.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except Idc.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Idc

        fields = ['name', 'address', 'tel', 'contact', 'contact_phone', 'ip_range', 'jigui', 'bandwidth'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'ip_range': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'jigui': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'bandwidth': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
        }


class CabinetForm(forms.ModelForm):

    class Meta:
        model = Cabinet

        fields = ['idc', 'cabient_code', 'cabient_name', 'remark', 'assets'
        ]

        widgets = {
            'idc': forms.Select(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'cabient_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),
            'cabient_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:450px;'}),

            'assets': forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    'data-placeholder': "Select Assets"
                }
            ),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'style': 'width:450px;'}),

        }

class GroupForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(GroupForm, self).clean()
        value = cleaned_data.get('name')
        try:
            AssetGroup.objects.get(name=value)
            self._errors['name'] = self.error_class(["%s的信息已经存在" % value])
        except AssetGroup.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = AssetGroup
        fields = [
            "name", 'remark', "assets"
        ]

        widgets ={
            'name': forms.TextInput,
            'remark': forms.Textarea(
                attrs={}
            ),
            'assets': forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    'data-placeholder':  "Select Assets"
                }
            )
        }


class FileForm(forms.Form):
    file = forms.FileField()
