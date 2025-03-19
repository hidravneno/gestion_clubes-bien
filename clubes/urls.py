from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 Ruta para la página principal
    path('crear/', views.crear_club, name='crear_club'),
    path('lista/', views.home, name='lista_clubes'),  # Ruta para listar clubes
]
