from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'CategoriaProducto'
        verbose_name_plural = 'CategoriasProducto'
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    imagen = models.ImageField(upload_to='categoria')
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=100)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    categorias  = models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
   