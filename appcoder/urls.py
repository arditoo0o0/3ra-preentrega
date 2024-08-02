from django.contrib import admin
from django.urls import path
from appcoder.views import cursos,estudiantes,profesores,inicio,entregables,estudianteformulario,RegistroEstudiante

urlpatterns = [
    path('',inicio,name='inicio'),
    path('pagina-de-cursos',cursos,name="cursos"),
    path('estudiantes',estudiantes,name='estudiantes'),
    path('profesores',profesores,name='profesores'),
    path('entregables',entregables,name='entregables'),
    path('estudiante_formulario' ,estudianteformulario, name='estudianteform'),
    path('registroestudiante/' ,RegistroEstudiante, name='RegistroEstudiante'),
    ]