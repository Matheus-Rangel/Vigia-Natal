from django.contrib import admin
from django.urls import path
from map_app.api.views import orgao
urlpatterns = [
    path('', orgao.OrgaoListAPIView.as_view(), name = 'orgao_list'),
    path('pk/<int:pk>', orgao.OrgaoRetriveAPIView.as_view(), name = 'orgao_id_retrive'),
    path('nome/<nome>', orgao.OrgaoNomeRetriveAPIView.as_view(), name = 'orgao_nome_retrive'),
    path('nome/<nome>/instituicao/<int:instituicao>', orgao.OrgaoNomeInstituicaoRetriveAPIView.as_view(), name = 'orgao_nome_instituicao_retrive'),
    path('create', orgao.OrgaoCreateAPIView.as_view(), name = 'orgao_create'),
]