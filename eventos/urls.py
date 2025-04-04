from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),  # Página de lista de eventos
    path('crear/', views.crear_evento, name='crear_evento'),  # Página para crear un evento
]
