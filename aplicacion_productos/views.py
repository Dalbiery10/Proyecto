from django.shortcuts import render
from django.template import loader
from .models import productos
from django.http import HttpResponse
from django.urls import path
# Create your views here.


# Create your views here.
def Productos(request):
    misProductos = productos.objects.all().values()
    template = loader.get_template('primertemplate.html')
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))

#def BienvenidaProductos(request):
    #template= loader.get_template('primertemplate.html')
    ##return HttpResponse(template.render())

