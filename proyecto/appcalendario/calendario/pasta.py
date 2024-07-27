from django.contrib.auth.models import User
from tu_app.models import Usuario

# Encuentra el superusuario (modifica 'admin' si tu superusuario tiene un nombre de usuario diferente)
superuser = User.objects.get(username='admin')

# Verifica si el superusuario ya tiene una instancia de Usuario
if not hasattr(superuser, 'usuario'):
    Usuario.objects.create(
        user=superuser,
        dni='0000000000',  # Usa un DNI de prueba
        nombre='Super',
        apellido='User'
    )

print("Instancia de Usuario creada para el superusuario.")