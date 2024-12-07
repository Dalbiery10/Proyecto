from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from aplicacion_productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página de inicio
    path('servicios/', views.servicios, name='servicios'),  # Servicios locales
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
    path('politicas/', views.politicas, name='politicas'),  # Políticas de privacidad
    path('articulos/', views.articulos, name='articulos'),  # Artículos y noticias
]
