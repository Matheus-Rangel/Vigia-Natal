from django import forms
from map_app.models import Obra, Orgao

class ObraForm(forms.ModelForm):

    class Meta():
        model = Obra
        exclude = ['data_update']


class OrgaoForm(forms.ModelForm):

    class Meta():
        model = Orgao
