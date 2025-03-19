from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # http://127.0.0.1:8000/usuarios/
    path('clubes/', include('clubes.urls')),     # http://127.0.0.1:8000/clubes/
    path('eventos/', include('eventos.urls')),   # ✅ http://127.0.0.1:8000/eventos/
    path('foros/', include('foros.urls')),
    path('', include('clubes.urls'), name='home'),
]
