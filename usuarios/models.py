from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('leader', 'Líder de Club'),
        ('member', 'Miembro'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='member')
