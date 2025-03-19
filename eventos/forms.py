from django import forms
from .models import Evento

class CrearEventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion', 'descripcion']
