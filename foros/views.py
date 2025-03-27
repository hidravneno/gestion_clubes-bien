from django.shortcuts import render, redirect
from .forms import CrearForoForm
from .models import Foro  # Asegúrate de tener un modelo llamado Foro

def lista_foros(request):
    foros = Foro.objects.all()  # Obtén todos los foros de la BD
    return render(request, 'foros/lista_foros.html', {'foros': foros})

def crear_foro(request):
    if request.method == 'POST':
        form = CrearForoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_foros')  # Redirección correcta
    else:
        form = CrearForoForm()
    return render(request, 'foros/crear_foro.html', {'form': form})
