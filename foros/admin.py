from django.contrib import admin
from .models import Foro, Votacion

@admin.register(Foro)
class ForoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'club', 'creado_por']