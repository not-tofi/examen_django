# aplicacion/models.py
"""
Módulo que define los modelos de la aplicación.
"""

from django.db import models
from django.utils import timezone

class Area(models.Model):
    """Modelo que representa un área dentro del gimnasio.   """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.nombre}"


class Espacio(models.Model):
    """Modelo que representa un espacio físico dentro del gimnasio."""
    nombre = models.CharField(max_length=100, unique=True)
    tipo_area = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.area}"

class Entrenador(models.Model):
    """Modelo que representa un entrenador del gimnasio."""
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

class Actividad(models.Model):
    """Modelo que representa una actividad del gimnasio."""
    nombre = models.CharField(max_length=100)
    tipo_Actividad = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"

class Evento(models.Model):
    """Modelo que representa un evento del gimnasio."""
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    espacio_fisico = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    actividades = models.ManyToManyField(Actividad, related_name='eventos', blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha:('%Y-%m-%d %H:%M')}"

class Socio(models.Model):
    """Modelo que representa un socio del gimnasio."""
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    actividades = models.ManyToManyField(Actividad, related_name='socios', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
