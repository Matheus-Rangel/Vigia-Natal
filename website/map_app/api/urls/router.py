from django.contrib import admin
from django.urls import path, include
from map_app.api.views import instituicao
urlpatterns = [
    path('despesa/', include('map_app.api.urls.despesa')),
    path('instituicao/', include('map_app.api.urls.instituicao')),
    path('localizacao/', include('map_app.api.urls.localizacao')),
    path('orgao/', include('map_app.api.urls.orgao')),
]