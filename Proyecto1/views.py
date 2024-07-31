from django.http import HttpResponse
import datetime
from django.template import loader , Template , Context

def primer_template(request):
    Nombre ="Bruno"
    Apellido ="Lopez sobrador"
    contexto= {"nombr":Nombre, "apel":Apellido}
    Plantilla= loader.get_template("template2.html")
    documento=Plantilla.render(contexto)
    return HttpResponse(documento)
