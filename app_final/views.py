from django.shortcuts import render
from django.http import HttpResponse
from app_final.models import Tecnicos, Sucuarsales, Vehiculo

# Create your views here.

#----------------paginas sin clases------------------#
def home(self):

    return render(self,'home.html')

def about(self):

   return render(self,'about.html')

def padre(self):

    return render(self,'padre.html')


#----------------clases------------------#
def tecnicos(self):

    return render(self,'tecnicos.html')

def sucursales(self):

    return render(self,'sucursales.html')

def vehiculos(self):

    return render(self,'vehiculos.html')

