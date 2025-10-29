from django.contrib import admin
from .models import Producto, Categoria

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'categoria', 'precio_unitario', 'stock_actual', 'fecha_vencimiento']
    search_fields = ['nombre_producto', 'categoria']
    list_filter = ['categoria', 'fecha_vencimiento']
    list_editable = ['precio_unitario', 'stock_actual']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'id_producto', 'descripcion']
    search_fields = ['nombre', 'id_producto__nombre_producto']
    list_filter = ['nombre']