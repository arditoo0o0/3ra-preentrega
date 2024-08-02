from django import forms

class RegistroEstudiante(forms.Form):
    estudiante=form.Charfield()
    contraseña=form.Interfield()