from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='ID categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre categoria')


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='ID producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre producto')
    descripcionProducto = models.CharField(max_length=200, verbose_name='Descripcion producto')
    cantidadProducto = models.IntegerField(verbose_name='Cantidad producto')
    fechRegProducto = models.DateTimeField(verbose_name='Fecha de registro')
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Usuario(models.Model):
    rutUsuario = models.CharField(max_length=20, primary_key=True, verbose_name='Rut usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre usuario') 
    claveUsuario = models.CharField(max_length=20, verbose_name='Clave usuario')