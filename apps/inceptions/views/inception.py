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
from ..models import Inception
# from ..hands import AdminUserRequiredMixin


__all__ = [
    'InceptionListView', 'InceptionCreateView', 'InceptionUpdateView',
    'InceptionBulkUpdateView', 'InceptionDetailView',
    'InceptionDeleteView', 'InceptionExportView', 'BulkImportInceptionView',
]
logger = get_logger(__file__)


class InceptionListView(TemplateView):
    template_name = 'inceptions/inception_list.html'

    def get_context_data(self, **kwargs):

        context = {
            'app': _('Inceptions'),
            'action': _('Inception list'),

        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)




class InceptionCreateView(SuccessMessageMixin, CreateView):
    model = Inception
    form_class = forms.InceptionCreateForm
    template_name = 'inceptions/inception_create.html'
    success_url = reverse_lazy('iinceptions:inception-list')

    # def form_valid(self, form):
    #     print("form valid")
    #     inception = form.save()
    #     inception.created_by = self.request.user.username or 'Admin'
    #     inception.date_created = timezone.now()
    #     inception.save()
    #     return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        return form

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Inceptions'),
            'action': _('Create inception'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return create_success_msg % ({"name": cleaned_data["hostname"]})




class InceptionBulkUpdateView( ListView):
    model = Inception
    form_class = forms.InceptionBulkUpdateForm
    template_name = 'inceptions/inception_bulk_update.html'
    success_url = reverse_lazy('inceptions:inception-list')
    id_list = None
    form = None

    def get(self, request, *args, **kwargs):
        inceptions_id = self.request.GET.get('inceptions_id', '')
        self.id_list = [i for i in inceptions_id.split(',')]

        if kwargs.get('form'):
            self.form = kwargs['form']
        elif inceptions_id:
            self.form = self.form_class(
                initial={'inceptions': self.id_list}
            )
        else:
            self.form = self.form_class()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return self.get(request, form=form, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Inceptions'),
            'action': _('Bulk update inception'),
            'form': self.form,
            'inceptions_selected': self.id_list,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class InceptionUpdateView( SuccessMessageMixin, UpdateView):
    model = Inception
    form_class = forms.InceptionUpdateForm
    template_name = 'inceptions/inception_update.html'
    success_url = reverse_lazy('inceptions:inception-list')

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Inceptions'),
            'action': _('Update inception'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        return update_success_msg % ({"name": cleaned_data["hostname"]})


class InceptionDeleteView( DeleteView):
    model = Inception
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('inceptions:inception-list')


class InceptionDetailView(DetailView):
    model = Inception
    context_object_name = 'inception'
    template_name = 'inceptions/inception_detail.html'

    def get_context_data(self, **kwargs):

        context = {
            'app': _('Inceptions'),
            'action': _('Inception detail')

        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class InceptionExportView(View):
    def get(self, request):
        spm = request.GET.get('spm', '')
        inceptions_id_default = [Inception.objects.first().id] if Inception.objects.first() else []
        inceptions_id = cache.get(spm, inceptions_id_default)
        fields = [
            field for field in Inception._meta.fields
            if field.name not in [
                'date_created'
            ]
        ]
        filename = 'inceptions-{}.csv'.format(
            timezone.localtime(timezone.now()).strftime('%Y-%m-%d_%H-%M-%S')
        )
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        response.write(codecs.BOM_UTF8)
        inceptions = Inception.objects.filter(id__in=inceptions_id)
        writer = csv.writer(response, dialect='excel', quoting=csv.QUOTE_MINIMAL)

        header = [field.verbose_name for field in fields]
        writer.writerow(header)

        for inception in inceptions:
            data = [getattr(inception, field.name) for field in fields]
            writer.writerow(data)
        return response

    def post(self, request, *args, **kwargs):
        try:
            inceptions_id = json.loads(request.body).get('inceptions_id', [])

        except ValueError:
            return HttpResponse('Json object not valid', status=400)
        spm = uuid.uuid4().hex
        cache.set(spm, inceptions_id, 300)
        url = reverse_lazy('inceptions:inception-export') + '?spm=%s' % spm
        return JsonResponse({'redirect': url})


class BulkImportInceptionView( JSONResponseMixin, FormView):
    form_class = forms.FileForm

    def form_valid(self, form):

        f = form.cleaned_data['file']
        det_result = chardet.detect(f.read())
        f.seek(0)  # reset file seek index

        file_data = f.read().decode(det_result['encoding']).strip(codecs.BOM_UTF8.decode())
        csv_file = StringIO(file_data)
        reader = csv.reader(csv_file)
        csv_data = [row for row in reader]
        fields = [
            field for field in Inception._meta.fields
            if field.name not in [
                'date_created'
            ]
        ]
        header_ = csv_data[0]
        mapping_reverse = {field.verbose_name: field.name for field in fields}
        attr = [mapping_reverse.get(n, None) for n in header_]
        if None in attr:
            data = {'valid': False,
                    'msg': 'Must be same format as '
                           'template or export file'}
            return self.render_json_response(data)

        created, updated, failed = [], [], []
        inceptions = []
        for row in csv_data[1:]:
            if set(row) == {''}:
                continue

            inception_dict_raw = dict(zip(attr, row))
            inception_dict = dict()


            inception = None
            inception_id = inception_dict.pop('id', None)
            if inception_id:
                inception = get_object_or_none(Inception, id=inception_id)
            if not inception:
                try:
                    if len(Inception.objects.filter(hostname=inception_dict.get('hostname'))):
                        raise Exception(_('already exists'))
                    with transaction.atomic():
                        inception = Inception.objects.create(**inception_dict)

                        created.append(inception_dict['hostname'])
                        inceptions.append(inception)
                except Exception as e:
                    failed.append('%s: %s' % (inception_dict['hostname'], str(e)))
            else:
                for k, v in inception_dict.items():
                    if v != '':
                        setattr(inception, k, v)
                try:
                    inception.save()
                    updated.append(inception_dict['hostname'])
                except Exception as e:
                    failed.append('%s: %s' % (inception_dict['hostname'], str(e)))

        data = {
            'created': created,
            'created_info': 'Created {}'.format(len(created)),
            'updated': updated,
            'updated_info': 'Updated {}'.format(len(updated)),
            'failed': failed,
            'failed_info': 'Failed {}'.format(len(failed)),
            'valid': True,
            'msg': 'Created: {}. Updated: {}, Error: {}'.format(
                len(created), len(updated), len(failed))
        }
        return self.render_json_response(data)