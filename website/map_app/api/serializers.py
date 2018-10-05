
from rest_framework import serializers
from map_app.models import Despesa, Orgao, Instituicao, Localizacao

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        exclude = ['data_update']

class OrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgao
        fields = '__all__'

class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'
