from django.contrib import admin
from .models import Producto, ImagenProducto

# Register your models here.
admin.site.register(Producto)
admin.site.register(ImagenProducto)