from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  # Importa login y logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.urls import reverse_lazy

def registrar_usuario(request):
    """
    Vista para registrar un nuevo usuario.
    """
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente después del registro
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('home')  # Redirige al usuario a la página de inicio
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

class CustomLoginView(LoginView):
    """
    Vista personalizada para el inicio de sesión.
    """
    template_name = 'usuarios/login.html'  # Plantilla para el login
    redirect_authenticated_user = True  # Redirige si el usuario ya está autenticado
    success_url = reverse_lazy('home')  # Redirige al home después del login

def logout_view(request):
    """
    Vista para cerrar sesión del usuario.
    """
    logout(request)  # Cierra la sesión del usuario
    return redirect('home')  # Redirige al usuario a la página de inicio