from django.contrib import admin
from django.urls import path
from map_app.api.views import instituicao
urlpatterns = [
    path('', instituicao.InstituicaoListAPIView.as_view(), name = 'instituicao_list'),
    path('pk/<int:pk>', instituicao.InstituicaoRetriveAPIView.as_view(), name = 'instituicao_id_retrive'),
    path('<int:pk>/orgaos', instituicao.InstituicaoOrgaosListAPIView.as_view(), name = 'instituicao_orgao'),
    path('nome/<nome>', instituicao.InstituicaoNomeRetriveAPIView.as_view(), name = 'instituicao_nome_retrive'),
    path('create', instituicao.InstituicaoCreateAPIView.as_view(), name = 'instituicao_create'),
]