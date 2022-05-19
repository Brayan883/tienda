from xml.dom.minidom import Document
from django.urls import path
from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/',views.contacto, name='contacto')
]
urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)