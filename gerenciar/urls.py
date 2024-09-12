"""
URL configuration for gestao_salas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),  # Define a view 'home' como a página inicial  # Adiciona a URL para o perfil  # Outras rotas...
    path('salas/', views.listar_salas, name='listar_salas'),
    path('salas/criar/', views.criar_sala, name='criar_sala'),  # Certifique-se de que 'criar_sala' existe em views.py
    path('salas/editar/<int:id>/', views.editar_sala, name='editar_sala'),
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/nova/', views.criar_reserva, name='criar_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/cancelar/<int:id>/', views.cancelar_reserva, name='cancelar_reserva'),
   


]
    

