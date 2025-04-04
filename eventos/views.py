from django.shortcuts import render, redirect
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
            return redirect('lista_eventos')  # Redirige a la lista de eventos
    else:
        form = CrearEventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

# Add link to create event
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos, 'crear_evento_link': '<a href="{% url \'crear_evento\' %}">Crear Evento</a>'})