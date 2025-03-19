from django import forms
from .models import Foro


class CrearForoForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['club', 'titulo', 'contenido', 'creado_por']

