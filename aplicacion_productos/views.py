from multiprocessing import AuthenticationError
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

from django.shortcuts import render

# Vista de la página de inicio
def index(request):
    return render(request, 'PaginaPrincipal.html')

# Vista para la página de Servicios Locales
def servicios(request):
    return render(request, 'servicios.html')

# Vista para la página de Contacto
def contacto(request):
    return render(request, 'contacto.html')

# Vista para la página de Políticas de Privacidad
def politicas(request):
    return render(request, 'politicas.html')

# Vista para la página de Artículos y Noticias
def articulos(request):
    return render(request, 'articulos.html')


#def BienvenidaProductos(request):
    #template= loader.get_template('primertemplate.html')
    ##return HttpResponse(template.render())

# views.py

from django.contrib.auth import login
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        # Aquí agregas la lógica para verificar el login
        user = AuthenticationError(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/admin/')  # Redirige al área de administración
        else:
            # Maneja el error si las credenciales son incorrectas
            pass
