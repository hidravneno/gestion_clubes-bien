from django.shortcuts import render, redirect
from .forms import CrearEventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = CrearEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = CrearEventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})
