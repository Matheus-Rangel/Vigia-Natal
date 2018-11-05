from map_app.models import Localizacao
from map_app.forms import LocalizacaoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

class LocalizacaoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/localizacao_detail.html'
    form_class = LocalizacaoForm
    model = Localizacao

class LocalizacaoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'map_app/localizacao_detail.html'
    form_class = LocalizacaoForm
    model = Localizacao