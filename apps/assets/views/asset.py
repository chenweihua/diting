from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.edit import (
    CreateView, UpdateView, FormMixin, FormView
)

from ..utils import AdminUserRequiredMixin

from ..models import *
from ..forms import *


class AssetCreateView(AdminUserRequiredMixin, SuccessMessageMixin, CreateView):
    success_url = ...
    template_name = ...
    form_class = AssetForm

    def get_context_data(self, **kwargs):
        context = super(Asset, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            assetInfoFrom = AssetInfoForm(self.request.POST, prefix='assetInfoFrom')
        else:
            assetInfoFrom = AssetInfoForm(prefix='assetInfoFrom')

        context['assetInfoFrom'] = assetInfoFrom

        return context
    def form_valid(self, form):
        asset = form.save(commit=False)
        context = self.get_context_data()
        assetInfo = context['assetInfoFrom'].save()
        asset.save()

        return super(AssetCreateView, self).form_valid(form)
