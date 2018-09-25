from django import forms
from map_app.models import Despesa, Orgao

class DespesaForm(forms.ModelForm):

    class Meta():
        model = Despesa
        exclude = ['data_update']


class OrgaoForm(forms.ModelForm):

    class Meta():
        model = Orgao
        fields = '__all__'
