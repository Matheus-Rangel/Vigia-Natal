from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from map_app.models import Instituicao, Orgao
from map_app.api.serializers import InstituicaoSerializer, OrgaoSerializer

class InstituicaoListAPIView(ListAPIView):
    serializer_class = InstituicaoSerializer
    def get_queryset(self):
        return Instituicao.objects.all()

class InstituicaoOrgaosListAPIView(ListAPIView):
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.filter(instituicao = self.kwargs['pk'])

class InstituicaoRetriveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = InstituicaoSerializer
    def get_queryset(self):
        return Instituicao.objects.filter(id = self.kwargs['pk'])

class InstituicaoNomeRetriveAPIView(RetrieveAPIView):
    lookup_field = 'nome'
    serializer_class = InstituicaoSerializer
    def get_queryset(self):
        return Instituicao.objects.filter(nome = self.kwargs['nome'])

class InstituicaoCreateAPIView(CreateAPIView):
    serializer_class = InstituicaoSerializer
    def get_queryset(self):
        return Instituicao.objects.all()


