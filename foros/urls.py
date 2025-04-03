from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_foros, name='lista_foros'),  # Lista de foros
    path('crear/', views.crear_foro, name='crear_foro'),  # Crear foro
    path('<int:foro_id>/', views.detalle_foro, name='detalle_foro'),  # Ver foro
    path('<int:foro_id>/editar/', views.editar_foro, name='editar_foro'),  # Editar foro
    path('<int:foro_id>/eliminar/', views.eliminar_foro, name='eliminar_foro'),  # Eliminar foro
]
