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

def Estudiante(request):
    if request.method =='POST':
        Estudiante==estudiantes(nombre=request.POST['estudiante']),contraseña==request.POST['Contraseña']
        Estudiante.save()
        
        return render(request,"appcoder/inicio.html")
    return render (request,appcoder/curso_formulario.html)

