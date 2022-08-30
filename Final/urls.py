"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from app_final.views import about, home, sucursales, tecnicos, vehiculos, padre, formulario_tecnicos, buscatec, buscartec, formulario_sucursales, buscasuc, buscarsuc, formulario_vehiculos, buscavehi, buscarvehi, login_request, register, sin_acceso, ReadTecnicos, ReadVehiculos, ReadSucursales, DelTecnicos, DelVehiculos, DelSucursales

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('tecnicos/', tecnicos, name="tecnicos"),
    path('sucursales/', sucursales, name="sucursales"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('padre/', padre, name="padre"),
    path('formulariotec/', formulario_tecnicos, name="formtec"),
    path('buscatec/', buscatec,name='buscatec'), 
    path('buscartec/', buscartec,name='buscartec'), 
    path('formulariosuc/', formulario_sucursales, name="formsuc"),
    path('buscasuc/', buscasuc,name='buscasuc'), 
    path('buscarsuc/', buscarsuc,name='buscarsuc'), 
    path('formulariovehi/', formulario_vehiculos, name="formvehi"),
    path('buscavehi/', buscavehi,name='buscavehi'), 
    path('buscarvehi/', buscarvehi,name='buscarvehi'), 
    path('login/', login_request,name='login'), 
    path('register/', register,name='register'), 
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'), 
    path('bienvenida/', register,name='register'), 
    path('sin_acceso/', sin_acceso, name='sin_acceso'),
    path('readtec/', ReadTecnicos, name='readtec'),
    path('readveh/', ReadVehiculos, name='readveh'),
    path('readsuc/', ReadSucursales, name='readsuc'),
    path('deltec/<tecnico_nombre>', DelTecnicos, name='deltec'),
    path('delveh/<vehiculo_modelo>', DelVehiculos, name='delveh'),
    path('delsuc/<sucursal_zona>', DelSucursales, name='delsuc'),
        
]
