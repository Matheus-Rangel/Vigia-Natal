from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from map_app.models import Despesa, Instituicao, Localizacao, Orgao
from map_app.api.serializers import DespesaSerializer, InstituicaoSerializer, LocalizacaoSerializer, OrgaoSerializer


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

class DespesaLocalizacaoListAPIView(ListAPIView):
    serializer_class = DespesaSerializer
    def get_queryset(self):
        l = self.kwargs['localizacao']
        ano = self.kwargs['ano']
        return Despesa.objects.filter(data_inicio__year = ano, localizacao = l)

class InstituicaoListAPIView(ListAPIView):
    serializer_class = InstituicaoSerializer
    def get_queryset(self):
        return Instituicao.objects.all()

class InstituicaoOrgaosListAPIView(ListAPIView):
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.filter(instituicao = self.kwargs['pk'])

class LocalizacaoListAPIView(ListAPIView):
    serializer_class = LocalizacaoSerializer
    def get_queryset(self):
        return Localizacao.objects.all()

class OrgaoListAPIView(ListAPIView):
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.all()

class LocalizacaoAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = LocalizacaoSerializer
    def get_queryset(self):
        return Localizacao.objects.filter(pk = self.kwargs['pk'])

class InstituicaoAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = InstituicaoSerializer
    def get_queryset(self):
        return Instituicao.objects.filter(pk = self.kwargs['pk'])

class DespesaAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = DespesaSerializer
    def get_queryset(self):
        return Despesa.objects.filter(pk = self.kwargs['pk'])

class OrgaoAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.filter(pk = self.kwargs['pk'])
