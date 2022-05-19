from django.urls import path
from tiendaonline import  views
urlpatterns = [
     path('',views.tienda,name='tienda'),
]