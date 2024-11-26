from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
def Productos(request):
    return HttpResponse("Nuestra primera vista!")
def BienvenidaProductos(request):
    template= loader.get_template('primertemplate.html')
    return HttpResponse(template.render())

