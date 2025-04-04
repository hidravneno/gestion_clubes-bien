from django.db import models
from django.core.exceptions import ValidationError
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

class MiembroClub(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('leader', 'Líder de Club'),
        ('member', 'Miembro'),
    )
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, choices=ROLES, default='member')
    fecha_union = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.rol == 'leader' and MiembroClub.objects.filter(club=self.club, rol='leader').exists():
            raise ValidationError('El club ya tiene un líder.')
        super().save(*args, **kwargs)

class SolicitudMembresia(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    )
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
