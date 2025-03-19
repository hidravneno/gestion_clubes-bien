from django.db import models
from clubes.models import Club

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

