from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Cambiado de 'index' a 'home'
    path('crear/', views.crear_club, name='crear_club'),  # Crear un nuevo club
    path('lista/', views.lista_clubes, name='lista_clubes'),  # Lista de clubes
    path('<int:club_id>/editar/', views.editar_club, name='editar_club'),  # Editar club

    # Rutas para reuniones
    path('<int:club_id>/reuniones/', views.lista_reuniones, name='lista_reuniones'),  # Lista de reuniones
    path('<int:club_id>/reuniones/crear/', views.crear_reunion, name='crear_reunion'),  # Crear reunión
    path('<int:club_id>/reuniones/<int:reunion_id>/editar/', views.editar_reunion, name='editar_reunion'),  # Editar reunión
    path('<int:club_id>/reuniones/<int:reunion_id>/eliminar/', views.eliminar_reunion, name='eliminar_reunion'),  # Eliminar reunión
]