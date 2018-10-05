from django import forms
from map_app.models import Despesa, Orgao, Instituicao, Localizacao

class DespesaForm(forms.ModelForm):
    class Meta():
        model = Despesa
        exclude = ['data_update']


class OrgaoForm(forms.ModelForm):
    class Meta():
        model = Orgao
        fields = '__all__'

class InstituicaoForm(forms.ModelForm):
    class Meta():
        model = Instituicao
        fields = '__all__'

class LocalizacaoForm(forms.ModelForm):
    class Meta():
        model = Localizacao
        fields = '__all__'
