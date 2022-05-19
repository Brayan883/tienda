from django.contrib import admin

from servicios.models import Servicio

# Register your models here.
@admin.register(Servicio)
class adminservicio(admin.ModelAdmin):
    list_display = ['titulo','contenido','imagen']
    list_display_links = ['titulo']
    list_filter = ['titulo']
    readonly_fields = ['created','updated']
    