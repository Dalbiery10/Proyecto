from django.contrib import admin
from .models import Productos

# Register your models here.
#admin.site.register(Productos)
class productosAdmin(admin.ModelAdmin):
    list_display=("codigoProducto", "descripcionProducto", "estatus",)
admin.site.register(Productos, productosAdmin)