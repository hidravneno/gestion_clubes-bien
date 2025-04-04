from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_club, name='crear_club'),
    path('lista/', views.home, name='lista_clubes'),
    path('<int:club_id>/solicitudes/', views.gestionar_solicitudes, name='gestionar_solicitudes'),
    path('<int:club_id>/miembros/', views.lista_miembros, name='lista_miembros'),
    path('<int:club_id>/', views.detalle_club, name='detalle_club'),  # Nueva ruta para detalles del club
]
