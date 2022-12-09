from distutils.command import upload
from pyexpat import model
from django.db import models


class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    
class pyme(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100, null=False)
    pyme = models.ForeignKey(pyme, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
