# Generated by Django 5.0.7 on 2024-07-27 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0002_alter_coleccion_eventos_alter_cuenta_correo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='cuenta',
            new_name='user',
        ),
    ]
