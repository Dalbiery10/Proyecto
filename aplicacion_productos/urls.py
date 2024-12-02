from django.urls import path
from . import views
urlpatterns = [
path('', views.Productos, name='Productos'),
]