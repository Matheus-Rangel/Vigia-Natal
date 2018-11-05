from map_app.models import Orgao, Despesa
from map_app.forms import OrgaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

class OrgaoListView(ListView):
    model = Orgao
    def get_queryset(self):
        return Orgao.objects.all()

class OrgaoDetailView(DetailView):
    model = Orgao
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['despesa_list'] = Despesa.objects.filter(orgao = self.kwargs['pk'])
        return context

class OrgaoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_detail.html'
    form_class = OrgaoForm
    model = Orgao

class OrgaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/orgao_detail.html'
    form_class = OrgaoForm
    model = Orgao