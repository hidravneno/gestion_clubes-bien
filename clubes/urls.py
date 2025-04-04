from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Registrar la vista 'home' como 'index'
    path('crear/', views.crear_club, name='crear_club'),  # Crear un nuevo club
    path('lista/', views.home, name='lista_clubes'),  # Lista de clubes
    path('<int:club_id>/solicitudes/', views.gestionar_solicitudes, name='gestionar_solicitudes'),  # Gestionar solicitudes
    path('<int:club_id>/miembros/', views.lista_miembros, name='lista_miembros'),  # Lista de miembros
    path('<int:club_id>/', views.detalle_club, name='detalle_club'),  # Detalles del club
    path('<int:club_id>/editar/', views.editar_club, name='editar_club'),  # Editar club
]