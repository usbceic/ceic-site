"""
Modelos
"""
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser

from ..ceic_site.validators import validate_carnet

# Aquí se crean los modelos
class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Tabla de usuarios de ceic_site

    La tabla de usuarios está compuesta por los siguientes campos:
    - Nombre de Usuario (único por persona)
    - Primer Nombre
    - Primer Apellido
    - Correo Electronico (única por persona)
    - Carnet Estudiantil (único por persona)
    - Número Telefonico (único por persona)
    """
    # Campo de Usuario
    username = models.CharField(max_length=100, verbose_name='Nombre de Usuario', unique=True)
    # Campo de Primer Nombre
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    # Campo de Segundo Nombre
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    # Campo de Correo Electronico
    email = models.EmailField(
        max_length=100, verbose_name='Dirección de Correo Electronico',
        unique=True)
    # Campo de Carnet Estudiantil
    carnet = models.CharField(
        max_length=8, verbose_name='Número de Carnet', unique=True,
        validators=[validate_carnet])
    # Campo de número Telefonico
    phone_number = models.CharField(max_length=20, verbose_name='Número de Telefono', unique=True)

    # Campo para Verificación de Estado
    is_staff = models.BooleanField(verbose_name='Es Staff')
    is_active = models.BooleanField(verbose_name='Está Activo')

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELD = ["username", "first_name", "last_name", "email", "carnet", "phone_number"]

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
        