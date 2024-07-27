from django.db import models
from django.contrib.auth.models import User

class Cuenta(models.Model):
    correo = models.EmailField()
    clave = models.CharField(max_length=100)  # Ajusta según tus necesidades


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos')

class Coleccion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    eventos = models.ManyToManyField(Evento, related_name='colecciones')