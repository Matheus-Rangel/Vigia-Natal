from django.contrib import admin
from django.urls import path, include
from map_app import views as map_views
from django.contrib.auth import views as auth_views
from map_app.api import views_despesa, views_localizacao, views_instituicao_orgao
urlpatterns = [
    path('despesa/id/<int:pk>', views_despesa.DespesaRetriveAPIView.as_view(), name='despesa_id'),
    path('despesa/ano/<int:ano>', views_despesa.DespesaAnoListAPIView.as_view(), name='despesa_ano'),
    path('despesa/<int:ano>/<int:orgao>', views_despesa.DespesaOrgaoListAPIView.as_view(), name = 'despesa_orgao'),
    path('despesa/<int:ano>/<int:instituicao>', views_despesa.DespesaInstituicaoListAPIView.as_view(), name = 'despesa_instituicao'),
    #path('despesa/<int:ano>/<int:localizacao>', views_despesa.DespesaLocalizacaoListAPIView.as_view(), name = 'despesa_localizacao'),
    path('despesa/create', views_despesa.DespesaCreateAPIView.as_view(), name = 'despesa_create'),

    path('instituicoes', views_instituicao_orgao.InstituicaoListAPIView.as_view(), name = 'instituicao_list'),
    path('instituicao/pk/<int:pk>', views_instituicao_orgao.InstituicaoRetriveAPIView.as_view(), name = 'instituicao_id_retrive'),
    path('instituicao/<int:pk>/orgaos', views_instituicao_orgao.InstituicaoOrgaosListAPIView.as_view(), name = 'instituicao_orgao'),
    path('instituicao/nome/<nome>', views_instituicao_orgao.InstituicaoNomeRetriveAPIView.as_view(), name = 'instituicao_nome_retrive'),
    path('instituicao/create', views_instituicao_orgao.InstituicaoCreateAPIView.as_view(), name = 'instituicao_create'),

    path('orgaos', views_instituicao_orgao.OrgaoListAPIView.as_view(), name = 'orgaos_retrive'),
    path('orgao/pk/<int:pk>', views_instituicao_orgao.OrgaoRetriveAPIView.as_view(), name = 'orgao_id_retrive'),
    path('orgao/nome/<nome>', views_instituicao_orgao.OrgaoNomeRetriveAPIView.as_view(), name = 'orgao_nome_retrive'),
    path('orgao/nome/<nome>/instituicao/<int:instituicao>', views_instituicao_orgao.OrgaoNomeInstituicaoRetriveAPIView.as_view(), name = 'orgao_nome_instituicao_retrive'),
    path('orgao/create', views_instituicao_orgao.OrgaoCreateAPIView.as_view(), name = 'orgao_create'),

    path('localizacao/<int:pk>', views_localizacao.LocalizacaoAPIView.as_view(), name = 'localizacao_api'),
    path('localizacao', views_localizacao.LocalizacaoListAPIView.as_view(), name = 'localizacao_list_api'),
]
