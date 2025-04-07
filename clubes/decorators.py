from django.http import Http404
from functools import wraps
from .models import Club

def lider_requerido(func):
    @wraps(func)
    def wrapper(request, club_id, *args, **kwargs):
        try:
            # Verifica que el usuario sea el líder del club
            club = Club.objects.get(id=club_id, lider=request.user)
        except Club.DoesNotExist:
            raise Http404("No tienes permiso para realizar esta acción.")
        return func(request, club_id, *args, **kwargs)
    return wrapper