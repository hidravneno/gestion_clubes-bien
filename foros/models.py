from django.db import models
from clubes.models import Club
from usuarios.models import Usuario

class Foro(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    creado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Votacion(models.Model):
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
    opcion = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)
