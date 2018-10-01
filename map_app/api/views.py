from rest_framework.views.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from map_app.models import Despesa, Instituicao, Localizacao, Orgao
from serializers import DespesaSerializer, InstituicaoSerializer, LocalizacaoSerializer, OrgaoSerializer


class DespesaAnoListAPIView(ListAPIView):
    serializer_class = DespesaSerializer
    def get_queryset(self):
        ano = self.kwargs['ano']
        return Despesa.objects.filter(data_inicio__year = ano)

class DespesaOrgaoListAPIView(ListAPIView):
    serializer_class = DespesaSerializer
    def get_queryset(self):
        o = self.kwargs['orgao']
        ano = self.kwargs['ano']
        return Despesa.objects.filter(orgao = o, data_inicio__year = ano)

class DespesaInstituicaoListAPIView(ListAPIView):
    serializer_class = DespesaSerializer
    def get_queryset(self):
        i = self.kwargs['instituicao']
        ano = self.kwargs['ano']
        orgaos = Orgao.objects.filter(instituicao = i)
        despesas = []
        for o in orgaos:
            despesas += Despesa.objects.filter(orgao = o, data_inicio__year = ano)
        return despesas

class DespesaLocalizacaoListAPIView(ListAPIView)::
    serializer_class = DespesaSerializer
    def get_queryset(self):
        l = self.kwargs['localizacao']
        ano = self.kwargs['ano']
        return Despesa.objects.filter(data_inicio__year = ano, localizacao = l)


class LocalizacaoAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = LocalizacaoSerializer

class InstituicaoAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = InstituicaoSerializer

class DespesaAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = DespesaSerializer

class OrgaoAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = OrgaoSerializer
