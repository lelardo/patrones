# Generated by Django 5.0.7 on 2024-07-27 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0003_rename_cuenta_usuario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='dni',
        ),
    ]
