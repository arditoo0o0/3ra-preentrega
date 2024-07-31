from django.contrib import admin
from django.urls import path
from appcoder.views import cursos,estudiantes,profesores,inicio,entregables

urlpatterns = [
    path('',inicio,name='inicio'),
    path('pagina-de-cursos',cursos,name="cursos"),
    path('estudiantes',estudiantes,name='estudiantes'),
    path('profesores',profesores,name='profesores'),
    path('entregables',entregables,name='entregables'),
]

Nuevos_estudiantes=[
    path('estudiante-formulario/', views.estudiante_formulario, name='Nuevostudiante')
]

urlpatterns += Nuevos_estudiantes