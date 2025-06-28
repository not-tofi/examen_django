# aplicacion/admin.py
"""Módulo que define el panel de administración de la aplicación.
"""

from django.contrib import admin
from .models import Area, Espacio, Entrenador, Actividad, Evento, Socio

admin.site.register(Area)
admin.site.register(Espacio)
admin.site.register(Entrenador)
admin.site.register(Actividad)
admin.site.register(Evento)
admin.site.register(Socio)
