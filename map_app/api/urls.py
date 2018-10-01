from django.contrib import admin
from django.urls import path, include
from map_app import views as map_views
from django.contrib.auth import views as auth_views
from api import views
urlpatterns = [
    path('despesa/<int:pk>', views.DespesaAPIView.as_view(), name='despesa_api')
    path('despesa/<int:ano>', views.DespesaAnoListAPIView.as_view(), name='despesa_ano_api')
    path('despesa/<int:ano>/<int:orgao>', views.DespesaOrgaoListAPIView.as_view(), name = 'despesa_orgao_api')
    path('despesa/<int:ano>/<int:instituicao>', views.DespesaInstituicaoListAPIView.as_view(), name = 'despesa_instituicao_api')
    path('despesa/<int:ano>/<int:localizacao>', views.DespesaLocalizacaoListAPIView.as_view(), name = 'despesa_localizacao_api')

    path('instituicoes', views.InstituicaoListAPIView.as_view(), name = 'instituicoes_api')
    path('instituicao/<int:pk>', views.InstituicaoAPIView.as_view(), name = 'instituicao_api')
    path('instituicao/<int:pk>/orgaos', views.InstituicaoAPIView.as_view(), name = 'instituicao_api')

    path('orgao/<int:pk>', views.OrgaoAPIView.as_view(), name = 'orgao_api')

    path('localizacao/<int:pk>', view.LocalizacaoAPIView.as_view(), name = 'localizacao_api')
    path('localizacao')

]
