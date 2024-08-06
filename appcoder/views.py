from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,"appcoder/inicio.html")

def cursos(request):
    return render(request,"appcoder/cursos.html")

def estudiantes(request):
    return render(request,"appcoder/estudiantes.html")

def profesores(request):
     if request.method == 'POST':
        
        nombre = request.POST.get('profesores')
        contraseña = request.POST.get('contraseña')
        
       
        profesores = profesores(nombre=nombre, contraseña=contraseña)
        profesores.save()
        
        return render(request, "appcoder/inicio.html")
    
     return render(request,"appcoder/profesores.html")

def entregables(request):
    return render(request,"appcoder/entregables.html")

from appcoder.models import Estudiante,Profesor

def estudianteformulario(request):
    return render (request,"appcoder/estudianteformulario.html")
def profesores_log(request):
    return render (request,"appcoder/profesores_log.html")
    
def RegistroEstudiante(request):
    if request.method == 'POST':
        
        nombre = request.POST.get('estudiante')
        contraseña = request.POST.get('contraseña')
        
       
        estudiante = Estudiante(nombre=nombre, contraseña=contraseña)
        estudiante.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render(request, "appcoder/RegistroEstudiante.html")

def busquedaestudiante(request):
    return render(request , "appcoder/busquedaestudiante.html")

from django.http import HttpResponse

def buscar(request):
  
    estudiantevalido = request.GET.get('estudiantevalido', 'Desconocido')  
    respuesta = f"{estudiantevalido} es parte de la academia"
    return HttpResponse(respuesta)


 