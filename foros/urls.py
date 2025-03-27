from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_foros, name='lista_foros'),  # Ruta para lista de foros
    path('crear/', views.crear_foro, name='crear_foro'),  # Ruta para crear foro
]
