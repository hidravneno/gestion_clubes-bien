from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, MiembroClub, SolicitudMembresia, Reunion
from .forms import CrearClubForm, CrearReunionForm
from django.contrib.auth.decorators import login_required
from eventos.models import Evento  # Importar el modelo Evento

# Vista para listar clubes
@login_required
def lista_clubes(request):
    clubes = Club.objects.all()
    return render(request, 'clubes/index.html', {'clubes': clubes})

# Vista para crear un club
@login_required
def crear_club(request):
    if request.method == 'POST':
        form = CrearClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.lider = request.user  # Asigna al usuario actual como líder del club
            club.save()
            return redirect('lista_clubes')
    else:
        form = CrearClubForm()
    return render(request, 'clubes/crear_club.html', {'form': form})

# Vista para editar un club
@login_required
def editar_club(request, club_id):
    club = get_object_or_404(Club, id=club_id, lider=request.user)  # Solo el líder puede editar el club
    if request.method == 'POST':
        form = CrearClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('lista_clubes')
    else:
        form = CrearClubForm(instance=club)
    return render(request, 'clubes/editar_club.html', {'form': form, 'club': club})

# Vista para listar reuniones
@login_required
def lista_reuniones(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    reuniones = Reunion.objects.filter(club=club)
    return render(request, 'clubes/lista_reuniones.html', {'club': club, 'reuniones': reuniones})

# Vista para crear una reunión
@login_required
def crear_reunion(request, club_id):
    club = get_object_or_404(Club, id=club_id, lider=request.user)  # Solo el líder puede crear reuniones
    if request.method == 'POST':
        form = CrearReunionForm(request.POST)
        if form.is_valid():
            reunion = form.save(commit=False)
            reunion.club = club
            reunion.save()
            return redirect('lista_reuniones', club_id=club.id)
    else:
        form = CrearReunionForm()
    return render(request, 'clubes/crear_reunion.html', {'form': form, 'club': club})

# Vista para editar una reunión
@login_required
def editar_reunion(request, club_id, reunion_id):
    club = get_object_or_404(Club, id=club_id, lider=request.user)  # Solo el líder puede editar reuniones
    reunion = get_object_or_404(Reunion, id=reunion_id, club=club)
    if request.method == 'POST':
        form = CrearReunionForm(request.POST, instance=reunion)
        if form.is_valid():
            form.save()
            return redirect('lista_reuniones', club_id=club.id)
    else:
        form = CrearReunionForm(instance=reunion)
    return render(request, 'clubes/editar_reunion.html', {'form': form, 'club': club, 'reunion': reunion})

# Vista para eliminar una reunión
@login_required
def eliminar_reunion(request, club_id, reunion_id):
    club = get_object_or_404(Club, id=club_id, lider=request.user)  # Solo el líder puede eliminar reuniones
    reunion = get_object_or_404(Reunion, id=reunion_id, club=club)
    if request.method == 'POST':
        reunion.delete()
        return redirect('lista_reuniones', club_id=club.id)
    return render(request, 'clubes/eliminar_reunion.html', {'club': club, 'reunion': reunion})

# Vista para gestionar solicitudes
@login_required
def gestionar_solicitudes(request, club_id):
    club = get_object_or_404(Club, id=club_id, lider=request.user)  # Solo el líder puede gestionar solicitudes
    solicitudes = SolicitudMembresia.objects.filter(club=club)

    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        accion = request.POST.get('accion')  # 'aceptar' o 'rechazar'
        solicitud = get_object_or_404(SolicitudMembresia, id=solicitud_id, club=club)

        if accion == 'aceptar':
            solicitud.estado = 'aceptada'
            solicitud.save()
        elif accion == 'rechazar':
            solicitud.estado = 'rechazada'
            solicitud.save()

    return render(request, 'clubes/gestionar_solicitudes.html', {'club': club, 'solicitudes': solicitudes})

# Vista para listar miembros del club
@login_required
def lista_miembros(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    miembros = MiembroClub.objects.filter(club=club)
    return render(request, 'clubes/lista_miembros.html', {'club': club, 'miembros': miembros})

# Vista para mostrar los detalles de un club
@login_required
def detalle_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    miembros = MiembroClub.objects.filter(club=club)
    eventos = Evento.objects.filter(club=club)
    return render(request, 'clubes/detalle_club.html', {
        'club': club,
        'miembros': miembros,
        'eventos': eventos,
    })

# Vista para la página principal
def home(request):
    return render(request, 'clubes/index.html')  # Asegúrate de que el template exista