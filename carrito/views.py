from django.shortcuts import render , redirect

from tiendaonline.models import Producto
from .carrito_producto import  Carro

def agregar_producto(request , producto_id):
    carro = Carro(request)
    producto_db = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto_db)
    return redirect("tienda")

def eliminar_producto(request , producto_id):
    carro = Carro(request)
    producto_db = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto_db)
    return redirect("tienda")

def restar_producto(request , producto_id):
    carro = Carro(request)
    producto_db = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto_db)
    return redirect("tienda")

def limpiar_carro(request , producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")