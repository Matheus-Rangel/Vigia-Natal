from map_app.models import Orgao, Instituicao
from map_app.forms import InstituicaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

class InstituicaoListView(ListView):
    model = Instituicao
    def get_queryset(self):
        return Instituicao.objects.all()

class InstituicaoDetailView(DetailView):
    model = Instituicao
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orgao_list'] = Orgao.objects.filter(instituicao = self.kwargs['pk'])
        return context

class InstituicaoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/instituicao_detail.html'
    form_class = InstituicaoForm
    model = Instituicao

class InstituicaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/instituicao_detail.html'
    form_class = InstituicaoForm
    model = Instituicao