from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),  # ✅ Ruta base para eventos/
    path('crear/', views.crear_evento, name='crear_evento'),  # http://127.0.0.1:8000/eventos/crear/
]
