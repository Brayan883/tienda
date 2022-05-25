from django.shortcuts import render
from tiendaonline.models import Producto

def tienda(request):
    Producto_db =  Producto.objects.all()
    context = {
        'producto':Producto_db
    }
    return render(request,'tiendaonline/tienda.html',context)