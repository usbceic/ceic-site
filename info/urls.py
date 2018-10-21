"""
Urls para la aplicación de información
"""

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [ # pylint: disable=invalid-name
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
