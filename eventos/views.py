from django.shortcuts import render, redirect
from .models import Evento
from .forms import CrearEventoForm
from .models import Evento  # Asegúrate de importar el modelo correcto

# ✅ Lista de eventos
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

# ✅ Crear evento
def crear_evento(request):
    if request.method == 'POST':
        form = CrearEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos') 
    else:
        form = CrearEventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

def lista_eventos(request):
    eventos = Evento.objects.all() 
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})