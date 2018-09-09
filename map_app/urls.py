from django.urls import path
from map_app import views

urlpatterns = [
    path('', views.index, name = 'map_index'),
]
