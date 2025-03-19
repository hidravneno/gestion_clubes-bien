from django import forms
from .models import Club

class CrearClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['nombre', 'descripcion', 'categoria']
