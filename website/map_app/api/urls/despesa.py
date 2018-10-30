from django.contrib import admin
from django.urls import path
from map_app.api.views import despesa 
urlpatterns = [
    path('id/<int:pk>', despesa.DespesaRetriveAPIView.as_view(), name='despesa_id'),
    path('ano/<int:ano>', despesa.DespesaAnoListAPIView.as_view(), name='despesa_ano'),
    path('<int:ano>/orgao/<int:orgao>', despesa.DespesaOrgaoListAPIView.as_view(), name = 'despesa_orgao'),
    path('<int:ano>/instituicao/<int:instituicao>', despesa.DespesaInstituicaoListAPIView.as_view(), name = 'despesa_instituicao'),
    #path('<int:ano>/<int:localizacao>', despesa.DespesaLocalizacaoListAPIView.as_view(), name = 'despesa_localizacao'),
    path('create', despesa.DespesaCreateAPIView.as_view(), name = 'despesa_create'),
]