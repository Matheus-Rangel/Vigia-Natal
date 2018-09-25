from django.urls import path
from map_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('despesa/list', views.DespesaListView.as_view(), name = 'despesa_list'),
    path('orgao/list', views.OrgaoListView.as_view(), name = 'orgao_list'),
    path('despesa/<int:pk>/', views.DespesaDetailView.as_view(), name = 'despesa_detail'),
    path('orgao/<int:pk>/', views.OrgaoDetailView.as_view(), name = 'orgao_detail'),
    path('despesa/cadastrar/', views.CreateDespesaView.as_view(), name = 'despesa_create'),
    path('orgao/cadastrar/', views.CreateOrgaoView.as_view(), name = 'orgao_create'),
    path('despesa/<int:pk>/update', views.DespesaUpdateView.as_view(), name = 'despesa_update'),
    path('orgao/<int:pk>/update', views.OrgaoUpdateView.as_view(), name = 'orgao_update')
]
