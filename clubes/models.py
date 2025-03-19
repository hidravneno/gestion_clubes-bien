from django.db import models
from usuarios.models import Usuario

class Club(models.Model):
    CATEGORIAS = (
        ('academico', 'Académico'),
        ('deportivo', 'Deportivo'),
        ('cultural', 'Cultural'),
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    lider = models.ForeignKey(Usuario, on_delete=models.CASCADE)
