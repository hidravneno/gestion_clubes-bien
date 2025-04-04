from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, MiembroClub, SolicitudMembresia
from .forms import CrearClubForm
from django.contrib.auth.decorators import login_required
from eventos.models import Evento  # Importar el modelo Evento

def home(request):
    clubes = Club.objects.all()
    return render(request, 'clubes/index.html', {'clubes': clubes})

@login_required
def crear_club(request):
    if request.method == 'POST':
        form = CrearClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.lider = request.user
            club.save()
            MiembroClub.objects.create(club=club, usuario=request.user, rol='leader')  # Agregar líder como miembro
            return redirect('lista_clubes')
    else:
        form = CrearClubForm()
    return render(request, 'clubes/crear_club.html', {'form': form})

@login_required
def gestionar_solicitudes(request, club_id):
    club = get_object_or_404(Club, id=club_id, lider=request.user)
    solicitudes = SolicitudMembresia.objects.filter(club=club, estado='pendiente')
    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        accion = request.POST.get('accion')
        solicitud = get_object_or_404(SolicitudMembresia, id=solicitud_id, club=club)
        if accion == 'aceptar':
            solicitud.estado = 'aceptada'
            solicitud.save()
            MiembroClub.objects.create(club=club, usuario=solicitud.usuario, rol='member')
        elif accion == 'rechazar':
            solicitud.estado = 'rechazada'
            solicitud.save()
    return render(request, 'clubes/gestionar_solicitudes.html', {'club': club, 'solicitudes': solicitudes})

@login_required
def lista_miembros(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    miembros = MiembroClub.objects.filter(club=club)
    return render(request, 'clubes/lista_miembros.html', {'club': club, 'miembros': miembros})

def detalle_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    miembros = MiembroClub.objects.filter(club=club)
    eventos = Evento.objects.filter(club=club)  # Filtrar eventos por el club
    return render(request, 'clubes/detalle_club.html', {'club': club, 'miembros': miembros, 'eventos': eventos})
