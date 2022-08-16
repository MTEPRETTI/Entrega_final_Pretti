from django.shortcuts import render
from django.http import HttpResponse
from app_final.models import Tecnicos, Sucursales, Vehiculo
from app_final.forms import AppForm_Tecnicos, AppForm_Sucursales, AppForm_Vehiculos

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

#----------------FORMULARIOS------------------#
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


def formulario_sucursales(request):

    print('method:', request.method)
    print('post:', request.POST)
    
    if request.method == 'POST':

        miFormularioSuc = AppForm_Sucursales(request.POST)

        if miFormularioSuc.is_valid():

            data = miFormularioSuc.cleaned_data
            
            sucursal = Sucursales(rsoc=data['rsoc'], zona=data['zona'])
            
            sucursal.save()
            
            return render(request, 'home.html')
    else:
        
        miFormularioSuc = AppForm_Sucursales()


    return render(request,'form_ingresoSuc.html', {'miFormularioSuc':miFormularioSuc})


def buscasuc(request):

    return render(request,'form_buscasuc.html')


def buscarsuc(request):

    if request.GET["zona"]:

        zona = request.GET["zona"]

        suc = Sucursales.objects.filter(zona__icontains=zona)

        return render(request, "form_resultbuscatec.html", {"suc": suc, "nombre":zona})
    
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)
    