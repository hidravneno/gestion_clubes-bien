from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_foro, name='crear_foro'),
]
