from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Club, MiembroClub, SolicitudMembresia
from django.contrib.auth.models import User

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

class EditarClubTestCase(TestCase):
    def setUp(self):
        self.lider = User.objects.create_user(username='lider', password='password')
        self.otro_usuario = User.objects.create_user(username='otro', password='password')
        self.club = Club.objects.create(nombre='Club Test', descripcion='Descripción', lider=self.lider)

    def test_lider_puede_editar_club(self):
        self.client.login(username='lider', password='password')
        response = self.client.get(reverse('editar_club', args=[self.club.id]))
        self.assertEqual(response.status_code, 200)

    def test_otro_usuario_no_puede_editar_club(self):
        self.client.login(username='otro', password='password')
        response = self.client.get(reverse('editar_club', args=[self.club.id]))
        self.assertEqual(response.status_code, 404)
