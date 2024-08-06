from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre= models.CharField(max_length=30)
    comision= models.IntegerField()
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    contraseña=models.CharField(max_length=30)
    
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    contraseña=models.CharField(max_length=40)
    
    
class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_de_entrega=models.DateField()
    entregado=models.BooleanField()