# APP: info - urls
# DESCRIPCION: Todas los templates relacionado con información deberán de conectarse aqui

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
	# Conecta template del Home
    path('', 
        TemplateView.as_view(template_name='home.html'),
        name='home'),
]