from django.contrib import admin

from tiendaonline.models import CategoriaProducto, Producto

# Register your models here.
@admin.register(CategoriaProducto)
class AdminCProducto(admin.ModelAdmin):
    list_display = ['nombre']
    list_display_links = ['nombre']
    list_filter = ['nombre']
@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ['nombre','descripcion','precio','imagen']
    list_display_links = ['nombre']
    list_filter = ['nombre']