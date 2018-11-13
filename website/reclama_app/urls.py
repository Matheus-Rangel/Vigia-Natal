from django.urls import path
from .views import ReclamaNatalView 

urls = [
    path('', ReclamaNatalView.as_view(), name = 'atualizar')
]