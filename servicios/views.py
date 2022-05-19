from django.shortcuts import render
from servicios.models import Servicio
def servicios(request):
     servicios_db = Servicio.objects.all()
     context = {
          'servicio':servicios_db
     }
     return render(request,'servicios/servicios.html',context)
    