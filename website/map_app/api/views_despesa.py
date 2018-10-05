from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from map_app.models import Despesa, Orgao
from map_app.api.serializers import DespesaSerializer
from rest_framework.permissions import IsAuthenticated
import datetime


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

class DespesaRetriveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = DespesaSerializer
    def get_queryset(self):
        return Despesa.objects.filter(id = self.kwargs['pk'])

class DespesaCreateAPIView(CreateAPIView):
    serializer_class = DespesaSerializer
    def perform_create(self, serializer):
        serializer.save(data_update = datetime.datetime.now())
    def get_queryset(self):
        return Despesa.objects.all()
