from django.db import models
from apps.Personas.models import Proveedor



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Digite nombre de Categoría",
                              unique=True, error_messages={'unique': 'ya existe esta categoria'})
    date_joined = models.DateTimeField(auto_now=True)   
    created_by = models.CharField(max_length=50, verbose_name="Creado por: ",default="root")
    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Digite nombre de la Marca",
                              unique=True, error_messages={'unique': 'Ya existe esta marca en el sistema'})
    date_joined = models.DateTimeField(auto_now=True)
    created_by = models.CharField(
        max_length=50, verbose_name="Creado por: ", default="root")
  
    def __str__(self):
        return self.nombre

class MarcaCategoria(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=10, default="root")
    date_joined = models.DateTimeField(auto_now=True)


class Producto(models.Model):
    class unidades(models.TextChoices):
        unidad = "Unidad"
        docena = "Docena"
        resma = "Resma"
        caja = "Caja"
    nombre = models.CharField(
        max_length=50, verbose_name="Ingrese nombre del producto")
    cantidad = models.IntegerField(verbose_name="Indique Cantidad de Producto")
    unidad = models.CharField(max_length=12, choices=unidades.choices,
                              default="Unidad", verbose_name="Unidades de medida del producto")
    precio_compra = models.IntegerField(
        verbose_name="Indique el Valor del producto")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT,
                                  null=True, blank=True, verbose_name="Indique el Proveedor: ")
    referencia = models.ForeignKey(MarcaCategoria, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(
        max_length=50, verbose_name="Creado por: ", default="root")

    def __str__(self):
        return self.nombre
