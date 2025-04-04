from django.db import models
from clubes.models import Club

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)  # Relación con Club


