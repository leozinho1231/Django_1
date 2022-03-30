from django.urls import path

from .views import *

urlpatterns = [
    path("usuarios/", UsuariosAPIView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>/', UsuariosAPIView.as_view(), name='usuariosParameters'),
    path("materias/", MateriasAPIView.as_view(), name='materias'),
    path('materias/<int:pk>/', MateriasAPIView.as_view(), name='materiasParameters'),
]




