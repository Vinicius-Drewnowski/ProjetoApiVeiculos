from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VeiculoViewSet
from django.urls import path
from . import views


router = DefaultRouter()
router.register(r'veiculos', VeiculoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('editar/<int:pk>/', views.editar_veiculo, name='editar_veiculo'),
    path('deletar/<int:pk>/', views.deletar_veiculo, name='deletar_veiculo'),
    path('grafico/', views.grafico_veiculos_por_marca, name='grafico_veiculos_por_marca'),
]

