"""
Validadores
"""
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Validador de clase Regex que se encarga de verificar patrones de Carnets Estudiantiles
validate_carnet = RegexValidator(
    r'^[0-9]{2}-[0-9]{5}$',
    message= "El Carnet Estudiantil debe contener solo números y guión.")
