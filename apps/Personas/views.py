from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Cliente, Proveedor
from .serializers import (ClienteSerializer, ProveedorSerializer,
                          ClienteSerializerPreview, ProveedorSerializerPreview)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.permissions import isCajero, isAdmin, isBodeguista
from django.db.models import Q

# ClienteControllers


class ClienteIndex(APIView):
    permission_classes = [isCajero | isAdmin]
    def get(self, request):
        clientes = Cliente.objects.order_by('-date_joined')[:10]
        serializer = ClienteSerializerPreview(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        myData = request.data.copy()
        myData['created_by'] = request.user.username
        serializer = ClienteSerializer(data=myData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):
    permission_classes = [isCajero | isAdmin]
    def get_data(self, pk):
        return get_object_or_404(Cliente, identificacion=pk)

    def get(self, request, pk):
        cliente = self.get_data(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk):
        cliente = self.get_data(pk)
        serializer = ClienteSerializer(
            cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = self.get_data(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClienteSearch(APIView):
    permission_classes = [isCajero | isAdmin]
    def get(self, request, pk):
        clientes = get_list_or_404(Cliente, identificacion__icontains=pk)[:10]
        serializer = ClienteSerializerPreview(clientes, many=True)
        return Response(serializer.data)

# ProveedorControllers


class ProveedorIndex(APIView):
    permission_classes = [isBodeguista | isAdmin | isCajero]
    def get(self, request):
        objects = Proveedor.objects.order_by('-date_joined')[:10]
        if not Proveedor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProveedorSerializerPreview(objects, many=True)
            return Response(serializer.data)

    def post(self, request):
        myData = request.data.copy()
        myData['created_by'] = request.user.username
        serializer = ProveedorSerializer(data=myData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProveedorDetail(APIView):
    permission_classes = [isBodeguista | isAdmin | isCajero]
    def get_single_data(self,pk):
        return get_object_or_404(Proveedor, NIT=pk)

    def get(self, request, pk):
        objects = self.get_single_data(pk)
        serializer = ProveedorSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk):
        objects = self.get_single_data(pk)
        serializer = ProveedorSerializer(objects, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objects = self.get_single_data(pk)
        objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProveedorSearch(APIView):
    permission_classes = [isBodeguista | isAdmin | isCajero]
    def get(self, request, pk):
        objects = Proveedor.objects.filter(
            Q(NIT__istartswith=pk) | Q(razonSocial__istartswith=pk))[:10]
        serializer = ProveedorSerializerPreview(objects, many=True)
        return Response(serializer.data)