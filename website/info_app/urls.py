from django.urls import path
from .views import InfoNatalView 

urls = [
    path('', InfoNatalView.as_view(), name = 'informacoes')
]