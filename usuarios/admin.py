"""
Admin de la aplicación `usuarios`
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    """
    Configuración para acciones del admin correspondientes al
    modelo `Usuario`
    """
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['email', 'username', ]


admin.site.register(Usuario, UsuarioAdmin)
