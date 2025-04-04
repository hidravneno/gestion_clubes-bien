from django import forms
from .models import Foro, Club


class CrearForoForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['club', 'titulo', 'contenido', 'creado_por']

    def __init__(self, *args, **kwargs):
        super(CrearForoForm, self).__init__(*args, **kwargs)
        self.fields['club'].queryset = Club.objects.all().order_by('nombre') 
        self.fields['club'].label_from_instance = lambda obj: obj.nombre