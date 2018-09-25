from django.shortcuts import render
from django.utils import timezone

from map_app.models import Despesa, Orgao
from map_app.forms import DespesaForm, OrgaoForm


from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, DetailView, ListView,
                                    CreateView, UpdateView)
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class DespesaListView(ListView):
    model = Despesa
    def get_queryset(self):
        return Despesa.objects.all()

class OrgaoListView(ListView):
    model = Orgao
    def get_queryset(self):
        return Orgao.objects.all()

class DespesaDetailView(DetailView):
    model = Despesa

class OrgaoDetailView(DetailView):
    model = Orgao
    def get_context_data(self, **kwargs):
        context = super(OrgaoDetailView, self).get_context_data(**kwargs)
        context['despesa_list'] = Despesa.objects.filter(orgao = self.kwargs['pk'])
        return context

class CreateDespesaView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/Despesa_info.html'
    form_class = DespesaForm
    model = Despesa

class CreateOrgaoView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_info.html'
    form_class = OrgaoForm
    model = Orgao

class DespesaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/Despesa_info.html'
    form_class = DespesaForm
    model = Despesa

class OrgaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_info.html'
    form_class = OrgaoForm
    model = Orgao
