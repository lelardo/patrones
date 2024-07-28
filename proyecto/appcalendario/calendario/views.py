from django.contrib.auth.forms import AuthenticationForm

from .models import Cuenta, Usuario, Evento, Coleccion
from .forms import CuentaForm, UsuarioForm, EventoForm, ColeccionForm, CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def crear_cuenta(request):
    if request.method == "POST":
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cuentas')
    else:
        form = CuentaForm()
    return render(request, 'crear_cuenta.html', {'form': form})

def listar_cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'listar_cuentas.html', {'cuentas': cuentas})

def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def crear_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})

def crear_coleccion(request):
    if request.method == "POST":
        form = ColeccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_colecciones')
    else:
        form = ColeccionForm()
    return render(request, 'crear_coleccion.html', {'form': form})

def listar_colecciones(request):
    colecciones = Coleccion.objects.all()
    return render(request, 'listar_colecciones.html', {'colecciones': colecciones})

def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Verificar si ya existe un Usuario asociado al User
            usuario, created = Usuario.objects.get_or_create(
                user=user,
                defaults={
                    'nombre': form.cleaned_data.get('first_name'),
                    'apellido': form.cleaned_data.get('last_name'),
                    'dni': form.cleaned_data.get('dni')
                }
            )
            if not created:
                # Si ya existe, actualizar los datos
                usuario.nombre = form.cleaned_data.get('first_name')
                usuario.apellido = form.cleaned_data.get('last_name')
                usuario.dni = form.cleaned_data.get('dni')
                usuario.save()
            login(request, user)
            return redirect('pagina_inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pagina_inicio')  # Redirigir a la página de inicio después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


