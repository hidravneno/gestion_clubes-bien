from django import forms
from .models import Club, Reunion

class CrearClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['nombre', 'descripcion', 'categoria']  # Excluye 'lider'

class CrearReunionForm(forms.ModelForm):
    class Meta:
        model = Reunion
        fields = ['titulo', 'descripcion', 'fecha', 'hora', 'ubicacion', 'club']