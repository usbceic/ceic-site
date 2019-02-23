"""
Validadores
"""
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

validate_carnet = RegexValidator(
	r'[0-9-]',
	message= "El Carnet Estudiantil debe contener solo números y guión.")