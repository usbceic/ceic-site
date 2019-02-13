"""
Modelos
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Usuario(AbstractBaseUser):
    """
    Tabla de usuarios de ceic_site

    Los docs de django siempre recomiendan usar un modelos de Usuario
    personalizado en vez del default. Asi no se aniadan mas campos despues
    """
    username = models.CharField(max_length=100, verbose_name='Nombre de Usuario', unique=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(
        max_length=100, verbose_name='Dirección de Correo Electronico',
        unique=True)
    # TODO: Añadir regex de Carnet
    carnet = models.CharField(max_length=8, verbose_name='Número de Carnet', unique=True)
    phone_number = models.CharField(max_length=20, verbose_name='Número de Telefono', unique=True)

    def __str__(self):
        return self.username
