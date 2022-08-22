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

#----------- Formulario para el alta-----------
'''
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Reingres Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}
'''