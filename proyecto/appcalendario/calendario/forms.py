from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario, Evento, Coleccion, Cuenta  # Asegúrate de que el modelo Cuenta está importado

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['correo', 'clave']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'dni']


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha']


class ColeccionForm(forms.ModelForm):
    class Meta:
        model = Coleccion
        fields = ['titulo', 'descripcion']

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    dni = forms.CharField(max_length=10, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'dni', 'password1', 'password2', 'email')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )