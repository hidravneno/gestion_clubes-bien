from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.registrar_usuario, name='registro_usuario'),  # ✅ Ruta base para usuarios/
    path('registro/', views.registrar_usuario, name='registro_usuario'),  # Ruta para registro
    path('login/', CustomLoginView.as_view(), name='login'),
]
