from django.shortcuts import render, redirect
from .forms import CrearForoForm

def crear_foro(request):
    if request.method == 'POST':
        form = CrearForoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_foros')
    else:
        form = CrearForoForm()
    return render(request, 'foros/crear_foro.html', {'form': form})
