from rest_framework.serializers import ModelSerializer
from .models import Cliente, Proveedor


class ClienteSerializerPreview(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('identificacion', 'nombre', 'apellido', 'esFrecuente')

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProveedorSerializerPreview(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('NIT', 'razonSocial')
        
class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'