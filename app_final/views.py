from django.shortcuts import render
from app_final.models import Tecnicos, Sucuarsales, Vehiculo
# Create your views here.

#----------------paginas sin clases------------------#
def inicio(self):

    return render(self,'inicio.html')

def about(self):

   return render(self,'about.html')

#----------------clases------------------#
def tecnicos(self):

    return render(self,'tec.html')

def sucursales(self):

    return render(self,'suc.html')

def vehiculos(self):

    return render(self,'vehic.html')

