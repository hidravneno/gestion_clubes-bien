from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventoForm
from .models import Evento  # Asegúrate de importar el modelo correcto

# ✅ Lista de eventos
def lista_eventos(request):
    eventos = Evento.objects.all()  # Obtiene todos los eventos
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

# ✅ Crear evento
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el evento en la base de datos
            return redirect('lista_eventos')  # Redirige a la lista de eventos
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

# Detalles de evento
def detalle_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})