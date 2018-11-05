from map_app.models import Despesa
from map_app.forms import DespesaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

class DespesaListView(ListView):
    model = Despesa
    def get_queryset(self):
        return Despesa.objects.all()

class DespesaDetailView(DetailView):
    model = Despesa

class DespesaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/despesa_detail.html'
    form_class = DespesaForm
    model = Despesa

class DespesaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/despesa_detail.html'
    form_class = DespesaForm
    model = Despesa