from django.shortcuts import render 
def home(request):
    return render(request,'inicio.html')
def contacto(request):
     return render(request,'contacto.html')