"""
Modelos
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    """
    Tabla de usuarios de ceic_site

    Los docs de django siempre recomiendan usar un modelos de Usuario
    personalizado en vez del default. Asi no se aniadan mas campos despues
    """

    def __str__(self):
        return self.username
