from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")

def cursos(request):
    return render(request,"appcoder/cursos.html")

def estudiantes(request):
    return render(request,"appcoder/estudiantes.html")

def profesores(request):
    return render(request,"appcoder/Profesores.html")

def entregables(request):
    return render(request,"appcoder/entregables.html")

from appcoder.models import Estudiante

def estudianteformulario(request):
    return render (request,"appcoder/estudianteformulario.html")
    
def RegistroEstudiante(request):
    if request.method == 'POST':
        # Asegúrate de usar las claves correctas que coincidan con los nombres de los campos del formulario.
        nombre = request.POST.get('estudiante')
        contraseña = request.POST.get('contraseña')
        
        # Crea una instancia de Estudiante con los datos del formulario.
        estudiante = Estudiante(nombre=nombre, contraseña=contraseña)
        estudiante.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render(request, "appcoder/RegistroEstudiante.html")

 