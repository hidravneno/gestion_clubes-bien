from django.shortcuts import render, redirect
from .forms import CrearClubForm
from .models import Club
from django.contrib.auth.decorators import login_required  # Asegúrate de importar esto

def home(request):
    clubes = Club.objects.all()  # Obtén todos los clubes
    return render(request, 'clubes/index.html', {'clubes': clubes})

@login_required
def crear_club(request):
    if request.method == 'POST':
        form = CrearClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)  # No guardes aún en la base de datos
            club.lider = request.user       # Asigna el usuario autenticado como líder
            club.save()                     # Ahora guarda el club
            return redirect('lista_clubes')
    else:
        form = CrearClubForm()
    return render(request, 'clubes/crear_club.html', {'form': form})
