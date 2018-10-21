"""
Formularios para los usuarios del sistema
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    """
    Formulario para creación de usuarios que usa los campos customizados
    """
    class Meta(UserCreationForm.Meta):
        # pylint: disable=missing-docstring,too-few-public-methods
        model = Usuario
        fields = ('username', 'email')


class UsuarioChangeForm(UserChangeForm):
    """
    Formulario para la modificación de usuarios
    """
    class Meta:
        # pylint: disable=missing-docstring,too-few-public-methods
        model = Usuario
        fields = ('username', 'email')
