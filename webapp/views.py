from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from personas.models import Persona


#IMPORTAMOS LOS DATOS DE BD A DJANGO. COMO LA CANTIDAD DE PERSONA Y DOMICILIO

def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})