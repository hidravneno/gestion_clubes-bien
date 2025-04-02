# filepath: \\wsl.localhost\Ubuntu\home\jp\development\gestion_clubes-bien\usuarios\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_usuario, name='registro_usuario'),  # Ruta base para usuarios/
    path('registro/', views.registrar_usuario, name='register'),  # Ruta para registro
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Ruta para login
    path('logout/', views.logout_view, name='logout'),  # Ruta para logout
]