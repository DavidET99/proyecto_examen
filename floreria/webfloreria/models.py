from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User  

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  
    categoria = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.nombre

class ControlUsuarios(AbstractUser):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.username
    


