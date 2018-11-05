from django.urls import path
from map_app.views import home, despesa, orgao, instituicao, localizacao

urlpatterns = [
    path('', home.HomeView.as_view(), name = 'home'),
    path('dados_gerais', home.DadosGeraisView.as_view(), name = 'dados_gerais'),
    
    path('despesa/list', despesa.DespesaListView.as_view(), name = 'despesa_list'),
    path('despesa/<int:pk>', despesa.DespesaDetailView.as_view(), name = 'despesa_detail'),
    path('despesa/cadastrar', despesa.DespesaCreateView.as_view(), name = 'despesa_create'),
    path('despesa/<int:pk>/update', despesa.DespesaUpdateView.as_view(), name = 'despesa_update'),
    
    path('orgao/list', orgao.OrgaoListView.as_view(), name = 'orgao_list'),
    path('orgao/<int:pk>', orgao.OrgaoDetailView.as_view(), name = 'orgao_detail'),
    path('orgao/cadastrar', orgao.OrgaoCreateView.as_view(), name = 'orgao_create'),
    path('orgao/<int:pk>/update', orgao.OrgaoUpdateView.as_view(), name = 'orgao_update'),

    path('instituicao/list', instituicao.InstituicaoListView.as_view(), name = 'instituicao_list'),
    path('instituicao/<int:pk>', instituicao.InstituicaoDetailView.as_view(), name = 'instituicao_detail'),
    path('instituicao/cadastrar', instituicao.InstituicaoCreateView.as_view(), name = 'instituicao_create'),
    path('instituicao/<int:pk>/update', instituicao.InstituicaoUpdateView.as_view(), name = 'instituicao_update'),

    path('localizacao/cadastrar', localizacao.LocalizacaoCreateView.as_view(), name = 'localizacao_create'),
    path('localizacao/<int:pk>/update', localizacao.LocalizacaoCreateView.as_view(), name = 'localizacao_update'),
]
