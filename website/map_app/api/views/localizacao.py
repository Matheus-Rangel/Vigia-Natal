from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from map_app.models import Despesa, Instituicao, Localizacao, Orgao
from map_app.api.serializers import DespesaSerializer, InstituicaoSerializer, LocalizacaoSerializer, OrgaoSerializer

class LocalizacaoListAPIView(ListAPIView):
    serializer_class = LocalizacaoSerializer
    def get_queryset(self):
        return Localizacao.objects.all()

class LocalizacaoAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = LocalizacaoSerializer
