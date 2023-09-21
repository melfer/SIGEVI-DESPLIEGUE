from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404

from apps.Personas.models import Proveedor
from .models import Marca, Categoria, MarcaCategoria, Producto
from .serializers import MarcaSerializer, CategoriaSerializer, MarcaCategoriaSerializer, ProductoSerializer, ProductoSerializerPreview, MarcaCategoriaViewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.permissions import isBodeguista, isAdmin, isCajero


# MarcaController
class MarcaIndex(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, format=None):
        marcas = Marca.objects.order_by('-date_joined')[:10]
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        myData = request.data.copy()
        myData['created_by'] = request.user.username
        serializer = MarcaSerializer(data=myData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarcaDetail(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get_object(self, pk):
        return get_object_or_404(Marca, id=pk)

    def get(self, request, pk, format=None):
        marca = self.get_object(pk)
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        marca = self.get_object(pk)
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        marca = self.get_object(pk)
        marca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MarcaSearch(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, name, format=None):
        marcas = get_list_or_404(Marca, nombre__icontains=name)[:10]
        serializer = MarcaSerializer(marcas, many=True)
        return Response(serializer.data)

# CategoriaController


class CategoriaIndex(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, format=None):
        categorias = Categoria.objects.order_by('-date_joined')[:10]
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        myData = request.data.copy()
        myData['created_by'] = request.user.username
        serializer = CategoriaSerializer(data=myData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetail(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get_object(self, pk):
        return get_object_or_404(Categoria, id=pk)

    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriaSearch(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, name, format=None):
        categorias = Categoria.objects.filter(nombre__icontains=name)[:10]
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)


class MarcaCategoriaIndex(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, id):
        queryset = get_list_or_404(MarcaCategoria, categoria=id)
        serializer = MarcaCategoriaViewSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        myData = request.data.copy()
        print(myData)
        myData['created_by'] = request.user.username
        myData['categoria'] = id
        serialize = MarcaCategoriaSerializer(data=myData)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class EliminarMarcaEnCategoria(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def delete(self, request, categoria_id, marca_id):
        queryset = get_object_or_404(
            MarcaCategoria, categoria=categoria_id, id=marca_id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FiltrarMarcasEnCategorias(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, id):
        categoria = get_object_or_404(Categoria, pk=id)
        marcas_categorias = categoria.marcacategoria_set.all()
        marcas_ids = marcas_categorias.values_list('marca__id', flat=True)
        queryset = get_list_or_404(Marca.objects.exclude(id__in=marcas_ids))
        serializer = MarcaSerializer(queryset, many=True)
        return Response(serializer.data)


class BuscarMarcasEnCategorias(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, id, nombre):
        categoria = get_object_or_404(Categoria, pk=id)
        marcas_categorias = categoria.marcacategoria_set.all()
        marcas_ids = marcas_categorias.values_list('marca__id', flat=True)
        queryset = Marca.objects.filter(
            nombre__icontains=nombre).exclude(id__in=marcas_ids)
        serializer = MarcaSerializer(queryset, many=True)
        return Response(serializer.data)

# Marcas Por categoria


class MarcaCategoriaDetail(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, nombre):
        object_data = MarcaCategoria.objects.filter(
            categoria__nombre__icontains=nombre)
        serializer = MarcaCategoriaSerializer(object_data, many=True)
        return Response(serializer.data)


class MarcaCategoriaDetailAdvanced(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, nombre, marca):
        object_data = MarcaCategoria.objects.filter(
            categoria__nombre__icontains=nombre, marca__nombre__icontains=marca)
        serializer = MarcaCategoriaSerializer(object_data, many=True)
        return Response(serializer.data)

# ProductoControllers


class ProductoIndex(APIView):
    permission_classes = [isBodeguista | isAdmin  ]
    def get(self, request, format=None):
        productos = Producto.objects.order_by('-date_joined')[:10]
        serializer = ProductoSerializerPreview(productos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        myData = request.data.copy()
        print(myData)
        if request.data.get('proveedor') == None:
            qproveedor = None
        else:
            qproveedor = Proveedor.objects.get(NIT=myData['proveedor'])
        qmarcaCategoria = MarcaCategoria.objects.get(
            id=myData['referencia_id'])
        serializer = ProductoSerializer(data=myData)
        if serializer.is_valid():
            q = Producto(
                nombre=myData['nombre'],
                cantidad=myData['cantidad'],
                unidad=myData['unidades'],
                precio_compra=myData['precio_compra'],
                proveedor=qproveedor,
                referencia=qmarcaCategoria,
                created_by=request.user.username
            )
            q.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetail(APIView):
    permission_classes = [isBodeguista | isAdmin]
    def get(self, request, pk, format=None):
        producto = get_object_or_404(Producto, id=pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        producto = get_object_or_404(Producto, id=pk)
        serializer = ProductoSerializer(producto,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = get_object_or_404(Producto, id=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductoSearch(APIView):
    permission_classes = [isBodeguista | isAdmin | isCajero]
    def get(self, request, name, format=None):
        productos = get_list_or_404(Producto, nombre__icontains=name)[:10]
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
class ProductoReport(APIView):
    permission_classes = [isBodeguista | isAdmin ]
    def get(self,request,format=None):
        productos = get_list_or_404(Producto,cantidad__lte=20)
        serializer = ProductoSerializer(productos,many=True)
        return Response(serializer.data)