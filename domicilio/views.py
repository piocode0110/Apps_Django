from django.shortcuts import render

# Create your views here.
from personas.models import Domicilio

def domicilio(request):
    mensajes = {'msg1': 'Valor mensaje 1', 'msg2': 'Valor mensaje 2'}
    return render(request, 'domicilio.html', mensajes)    

# def domicilio(request):
#     no_domicilio = Domicilio.objects.count()
#     domicilio = Domicilio.objects.all()
#     return render(request, 'domicilio.html', {'no_domicilio': no_domicilio, 'domicilio': domicilio})

