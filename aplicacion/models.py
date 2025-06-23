from django.db import models
from django.utils import timezone

class Area(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField(blank=True, null=True) 
    categoria = models.CharField(max_length=50) 
    activo = models.BooleanField(default=True) 


    def __str__(self):
        return {self.nombre}


class Espacio_Fisico(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo_area = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.area.nombre}"
        

class Entrenador(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return {self.nombre}

class Actividad(models.Model):
    tipo_Actividad = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    espacio_fisico = models.ForeignKey(Espacio_Fisico, on_delete=models.CASCADE)
    actividades = models.ManyToManyField(Actividad, related_name='eventos', blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"


class Socio(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    actividades = models.ManyToManyField(Actividad, related_name='socios', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"