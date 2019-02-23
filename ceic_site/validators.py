"""
Validadores
"""
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

validate_carnet = RegexValidator(
	r'[0-9-]',
	message= "El Carnet Estudiantil debe contener solo números y guión.")

# ejemplo: RegexValidator('^(\w+\d+|\d+\w+)+$', 
# message="Password should be a combination of Alphabets and Numbers")]