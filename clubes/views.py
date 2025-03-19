from django.shortcuts import render, redirect
from .forms import CrearClubForm
from .models import Club

def home(request):
    clubes = Club.objects.all()  # Obtén todos los clubes
    return render(request, 'clubes/index.html', {'clubes': clubes})

def crear_club(request):
    if request.method == 'POST':
        form = CrearClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clubes')
    else:
        form = CrearClubForm()
    return render(request, 'clubes/crear_club.html', {'form': form})
