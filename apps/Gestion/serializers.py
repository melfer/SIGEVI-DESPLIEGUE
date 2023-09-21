from rest_framework import serializers
from .models import Categoria, Marca, Producto, MarcaCategoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    referencia = serializers.SerializerMethodField('get_referencia')
    proveedor = serializers.SerializerMethodField('get_proveedor')
    class Meta:
        model = Producto
        fields = '__all__'

    def get_referencia(self, obj):
        return [{'marca': obj.referencia.marca.nombre, 'categoria': obj.referencia.categoria.nombre}]
    
    def get_proveedor(self, obj):
        return [{'nombre': obj.proveedor.razonSocial, 'nit': obj.proveedor.NIT}] if obj.proveedor else None




class ProductoSerializerPreview(serializers.ModelSerializer):
    referencia = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ('id', 'nombre',
                  'referencia', 'cantidad', 'unidad')

    def get_referencia(self, obj):
        return [{'marca': obj.referencia.marca.nombre, 'categoria': obj.referencia.categoria.nombre}]


class MarcaCategoriaViewSerializer(serializers.ModelSerializer):
    marca = serializers.StringRelatedField(source="marca.nombre")

    class Meta:
        model = MarcaCategoria
        fields = '__all__'


class MarcaCategoriaSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source='marca.nombre', read_only=True)
    categoria_nombre = serializers.CharField(
        source='categoria.nombre', read_only=True)

    class Meta:
        model = MarcaCategoria
        fields = ['id', 'marca', 'marca_nombre', 'categoria',
                  'categoria_nombre', 'created_by', 'date_joined']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['marca'] = {
            'id': rep['marca'],
            'nombre': rep['marca_nombre']
        }
        rep['categoria'] = {
            'id': rep['categoria'],
            'nombre': rep['categoria_nombre']
        }
        del rep['marca_nombre']
        del rep['categoria_nombre']
        return rep
