
from rest_framework import serializers
from map_app.models import Despesa, Orgao, Instituicao, Localizacao

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class OrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
