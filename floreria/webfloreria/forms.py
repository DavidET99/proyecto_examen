from django import forms
import re
from .models import Productos
from .models import ControlUsuarios
from django.core.exceptions import ValidationError

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'imagen','categoria']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].required = True 

class ProductoUpdateForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'imagen','categoria']

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre y apellido no deben contener caracteres especiales ni números.")
        return nombre

    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad < 18:
            raise ValidationError("Debes ser mayor de 18 años para registrarte.")
        return edad

    class Meta:
        model = ControlUsuarios
        fields = ['username', 'password', 'nombre', 'edad', 'correo', 'telefono', 'direccion']

class PhoneLoginForm(forms.Form):
    telefono = forms.CharField(label="Teléfono", max_length=20)