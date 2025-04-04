from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Club, MiembroClub, SolicitudMembresia

class ClubesTestCase(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(username='testuser', password='password')
        self.club = Club.objects.create(nombre='Club de Prueba', descripcion='Descripción', categoria='academico', lider=self.usuario)

    def test_crear_club(self):
        self.assertEqual(Club.objects.count(), 1)

    def test_solicitud_membresia(self):
        solicitud = SolicitudMembresia.objects.create(club=self.club, usuario=self.usuario)
        self.assertEqual(solicitud.estado, 'pendiente')

class MiembroClubTestCase(TestCase):
    def test_unico_lider(self):
        miembro = MiembroClub.objects.create(club=self.club, usuario=self.usuario, rol='leader')
        with self.assertRaises(ValidationError):
            MiembroClub.objects.create(club=self.club, usuario=self.usuario, rol='leader')
