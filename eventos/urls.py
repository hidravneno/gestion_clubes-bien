from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),  # Lista de eventos
    path('crear/', views.crear_evento, name='crear_evento'),  # Crear evento
]
