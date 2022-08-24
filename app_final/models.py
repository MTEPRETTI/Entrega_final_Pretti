from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tecnicos(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)
    fecha_ingreso = models.DateField()
    #user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Turno: {self.turno} - Ingreso: {self.fecha_ingreso}'

class Sucuarsales(models.Model):

    zona = models.CharField(max_length=40)
    rsoc = models.CharField(max_length=40)
    def __str__(self):
        return f'Zona: {self.zona} - Sucursal: {self.rsoc}'

class Vehiculo(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    def __str__(self):
        return f'Marca: {self.marca} - Modelo: {self.modelo}'