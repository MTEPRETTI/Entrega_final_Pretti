from datetime import date
from django.db import models

# Create your models here.
class Tecnicos(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)
    fecha_ingreso = models.DateField()

class Sucursales(models.Model):

    zona = models.CharField(max_length=40)
    rsoc = models.CharField(max_length=40)

class Vehiculo(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    