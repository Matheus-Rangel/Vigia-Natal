from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from map_app.models import  Orgao
from map_app.api.serializers import OrgaoSerializer

class OrgaoRetriveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.filter(id = self.kwargs['pk'])

class OrgaoListAPIView(ListAPIView):
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.all()

class OrgaoNomeRetriveAPIView(RetrieveAPIView):
    lookup_field = 'nome'
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.filter(nome = self.kwargs['nome'])

class OrgaoNomeInstituicaoRetriveAPIView(RetrieveAPIView):
    lookup_field = 'nome'
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.filter(nome = self.kwargs['nome'], instituicao = self.kwargs['instituicao'])


class OrgaoCreateAPIView(CreateAPIView):
    serializer_class = OrgaoSerializer
    def get_queryset(self):
        return Orgao.objects.all()
