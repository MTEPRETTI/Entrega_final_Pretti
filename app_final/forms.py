from django import forms

#----------- INGRESO -----------

class AppForm_Tecnicos(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    turno = forms.CharField()
    fecha_ingreso = forms.DateField()

class AppForm_Sucuarsales(forms.Form):

    zona = forms.CharField()
    rsoc = forms.CharField()

class AppForm_Vehiculos(forms.Form):
    
    marca = forms.CharField()
    modelo = forms.CharField()


#----------- BUSQUEDA -----------

class Busca_Tecnicos(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    turno = forms.CharField()
    fecha_ingreso = forms.DateField()

class Busca_Sucursales(forms.Form):
    
    zona = forms.CharField()
    rsoc = forms.CharField()

class Busca_Vehiculos(forms.Form):    

    marca = forms.CharField()
    modelo = forms.CharField()