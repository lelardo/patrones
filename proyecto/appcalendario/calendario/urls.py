from . import views
from django.urls import path, include

from .views import registro

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),  # Página de inicio
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('listar_cuentas/', views.listar_cuentas, name='listar_cuentas'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('listar_eventos/', views.listar_eventos, name='listar_eventos'),
    path('crear_coleccion/', views.crear_coleccion, name='crear_coleccion'),
    path('listar_colecciones/', views.listar_colecciones, name='listar_colecciones'),
    path('registro/', registro, name='registro'),




]
