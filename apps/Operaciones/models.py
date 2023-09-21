from django.db import models
from apps.Personas.models import Cliente
from apps.Gestion.models import Producto


class Cotizacion(models.Model):
    created_by = models.CharField(max_length=50, default="root")
    date_joined = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    total = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"


class DetalleCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    producto = models.ForeignKey(
        Producto, on_delete=models.PROTECT, null=True, blank=True)
    cantidad = models.IntegerField(default=0)
    subtotal = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "DetalleCotizacion"
        verbose_name_plural = "DetallesCotizaciones"

class Venta(models.Model):
    created_by = models.CharField(max_length=50, default="root")
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    total = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    

class ProductoVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=0)
    subtotal = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)