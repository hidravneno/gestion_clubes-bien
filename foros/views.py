from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearForoForm
from .models import Foro  

def lista_foros(request):
    foros = Foro.objects.all()
    return render(request, 'foros/lista_foros.html', {'foros': foros})

def crear_foro(request):
    if request.method == 'POST':
        form = CrearForoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_foros')
    else:
        form = CrearForoForm()
    return render(request, 'foros/crear_foro.html', {'form': form})

def detalle_foro(request, foro_id):
    foro = get_object_or_404(Foro, id=foro_id)
    return render(request, 'foros/detalle_foro.html', {'foro': foro})

def editar_foro(request, foro_id):
    foro = get_object_or_404(Foro, id=foro_id)
    if request.method == 'POST':
        form = CrearForoForm(request.POST, instance=foro)
        if form.is_valid():
            form.save()
            return redirect('lista_foros')
    else:
        form = CrearForoForm(instance=foro)
    return render(request, 'foros/editar_foro.html', {'form': form})

def eliminar_foro(request, foro_id):
    foro = get_object_or_404(Foro, id=foro_id)
    if request.method == 'POST':
        foro.delete()
        return redirect('lista_foros')
    return render(request, 'foros/eliminar_foro.html', {'foro': foro})
