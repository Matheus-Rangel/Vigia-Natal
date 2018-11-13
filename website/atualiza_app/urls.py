from django.urls import path
from .views import AtualizaNatalView

urls = [
    path('', AtualizaNatalView.as_view(), name = 'atualizar')
]