from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_usuario, name='registro_usuario'),  # ✅ Ruta base para usuarios/
    path('registro/', views.registrar_usuario, name='registro_usuario'),  # Ruta para registro
]
