"""
Modelos
"""
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Tabla de usuarios de ceic_site

    Los docs de django siempre recomiendan usar un modelos de Usuario
    personalizado en vez del default. Asi no se aniadan mas campos despues
    """
    username = models.CharField(max_length=100, verbose_name='Nombre de Usuario', unique=True)
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(
        max_length=100, verbose_name='Dirección de Correo Electronico',
        unique=True)
    # TODO: Añadir regex de Carnet
    carnet = models.CharField(max_length=8, verbose_name='Número de Carnet', unique=True)
    phone_number = models.CharField(max_length=20, verbose_name='Número de Telefono', unique=True)

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