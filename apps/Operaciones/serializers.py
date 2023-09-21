from rest_framework import serializers
from .models import Cotizacion, DetalleCotizacion, Venta, ProductoVenta
from apps.Gestion.models import Producto

class CotizacionSerializer(serializers.ModelSerializer):
    cliente = serializers.SerializerMethodField()
    class Meta:
        model = Cotizacion
        fields = '__all__'
    def get_cliente(self, obj):
        return [{"id": obj.solicitante.identificacion, "nombre": obj.solicitante.nombre, "apellido": obj.solicitante.apellido}]

class DetalleCotizacionSerializer(serializers.ModelSerializer):
    producto = serializers.SerializerMethodField()
    class Meta:
        model = DetalleCotizacion
        fields = '__all__'

    def get_producto(self, obj):
        try:
            # Obtener el producto asociado al objeto DetalleCotizacion
            producto = obj.producto
        except Producto.DoesNotExist:
            # Si el objeto DetalleCotizacion es nuevo, el producto no existe aún
            # y debemos obtenerlo usando el id del producto en los datos de entrada
            producto = Producto.objects.get(
                id=self.context['request'].data['producto'])
        # Crear el diccionario con la información del producto
        return {
            'nombre': producto.nombre,
            'precio': producto.precio_compra,
            'referencia': {
                'marca': producto.referencia.marca.nombre,
                'categoria': producto.referencia.categoria.nombre
            }
        }

###Venta serializser
class VentaSerializer(serializers.ModelSerializer):
    cliente = serializers.SerializerMethodField()
    class Meta:
        model = Venta
        fields = '__all__'
    def get_cliente(self, obj):
        return [{"id": obj.cliente.identificacion, "nombre": obj.cliente.nombre, "apellido": obj.cliente.apellido}]
    
#### detalle de la venta
class ProductoVentaSerializer(serializers.ModelSerializer):
    producto = serializers.SerializerMethodField()
    class Meta:
        model = ProductoVenta
        fields = '__all__'
        
    def get_producto(self,obj):
        try:
            producto = obj.producto
        except Producto.DoesNotExist:
            producto = Producto.objects.get(
                id=self.context['request'].data['producto'])
        return {
            'nombre': producto.nombre,
            'precio': producto.precio_compra,
            'referencia': {
                'marca': producto.referencia.marca.nombre,
                'categoria': producto.referencia.categoria.nombre
            }
        }