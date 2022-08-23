from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AppForm_Vehiculos
from app_final.models import Tecnicos, Sucuarsales, Vehiculo
from app_final.forms import AppForm_Tecnicos, AppForm_Sucuarsales
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
#----------------Registro------------------#
def register(request):

    if request.method  == 'POST':
        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            #return render(request,'home.html', {'mensaje','Usuario creado'})
            return render(request,'home.html')
    
    else:
        form = UserCreationForm()
        #form = UserRegisterForm()
    
    return render(request,'register.html', {'form':form})
#----------------Login------------------#

def login_request(request):

    if request.method== "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request,'home.html', {'mensaje':f'Bienvenido {usuario}'})

            else:

                return render(request,'home.html', {'mensaje':f'Error datos incorrectos'})

        else:

                return render(request,'home.html', {'mensaje':f'Formulario erroneo'})

    form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})

#----------------paginas sin clases------------------#
def home(self):

    return render(self,'home.html')

def about(self):

   return render(self,'about.html')

def padre(self):

    return render(self,'padre.html')


#----------------clases------------------#
@login_required
def tecnicos(self):

    return render(self,'tecnicos.html')

@login_required
def sucursales(self):

    return render(self,'sucursales.html')

@login_required
def vehiculos(self):

    return render(self,'vehiculos.html')


#----------------FORMULARIO TECNICOS------------------#


def formulario_tecnicos(request):

    print('method:', request.method)
    print('post:', request.POST)
    
    if request.method == 'POST':

        miFormularioTec = AppForm_Tecnicos(request.POST)

        if miFormularioTec.is_valid():

            data = miFormularioTec.cleaned_data
            
            tecnico = Tecnicos(nombre=data['nombre'], apellido=data['apellido'], turno=data['turno'], fecha_ingreso=data['fecha_ingreso'])
            
            tecnico.save()
            
            return render(request, 'home.html')
    else:
        
        miFormularioTec = AppForm_Tecnicos()


    return render(request,'form_ingresoTec.html', {'miFormularioTec':miFormularioTec})


def buscatec(request):

    return render(request,'form_buscatec.html')


def buscartec(request):

    if request.GET["turno"]:

        turno = request.GET["turno"]

        tec = Tecnicos.objects.filter(turno__icontains=turno)

        return render(request, "form_resultbuscatec.html", {"tec": tec, "nombre":turno})
    
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)


#----------------FORMULARIO SUCURSALES------------------#


def formulario_sucursales(request):

    print('method:', request.method)
    print('post:', request.POST)
    
    if request.method == 'POST':

        miFormularioSuc = AppForm_Sucuarsales(request.POST)

        if miFormularioSuc.is_valid():

            data = miFormularioSuc.cleaned_data
            
            sucursal = Sucuarsales(rsoc=data['rsoc'], zona=data['zona'])
            
            sucursal.save()
            
            return render(request, 'home.html')
    else:
        
        miFormularioSuc = AppForm_Sucuarsales()


    return render(request,'form_ingresoSuc.html', {'miFormularioSuc':miFormularioSuc})


def buscasuc(request):

    return render(request,'form_buscasuc.html')


def buscarsuc(request):

    if request.GET["zona"]:

        zona = request.GET["zona"]

        rsoc = Sucuarsales.objects.filter(zona__icontains=zona)

        return render(request, "form_resultbuscasuc.html", {"zona": zona, "rsoc":rsoc})

    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)
    

#----------------FORMULARIO VEHICULOS------------------#


def formulario_vehiculos(request):

    print('method:', request.method)
    print('post:', request.POST)
    
    if request.method == 'POST':

        miFormularioVehi = AppForm_Vehiculos(request.POST)

        if miFormularioVehi.is_valid():

            data = miFormularioVehi.cleaned_data
            
            vehiculos = Vehiculo(marca=data['marca'], modelo=data['modelo'])
            
            vehiculos.save()
            
            return render(request, 'home.html')
    else:
        
        miFormularioVehi = AppForm_Vehiculos()


    return render(request,'form_ingresoVehi.html', {'miFormularioVehi':miFormularioVehi})


def buscavehi(request):

    return render(request,'form_buscavehi.html')


def buscarvehi(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]

        modelo = Vehiculo.objects.filter(marca__icontains=marca)

        return render(request, "form_resultbusvehi.html", {"marca": marca, "modelo": modelo})

    else:

        respuesta = 'No enviaste datos'
