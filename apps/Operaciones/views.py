from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from apps.Personas.models import Cliente
from .serializers import CotizacionSerializer, DetalleCotizacionSerializer, VentaSerializer, ProductoVentaSerializer
from .models import Cotizacion, DetalleCotizacion, Venta, ProductoVenta
from apps.Gestion.models import Producto
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from core.permissions import isCajero,isAdmin
# Cotizacion Controller
##### Lista todas las cotizaicones y Crea cotizaciones
class CotizacionIndex(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self, request, format=None):
        queryset = Cotizacion.objects.order_by('-date_joined')[:10]
        serializer = CotizacionSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        data = request.data.copy()
        q = Cliente.objects.get(identificacion=data.get('identificacion'))
        data['solicitante'] = q.identificacion
        data['created_by'] = request.user.username
        serializer = CotizacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Cotizacion creada'},status=status.HTTP_201_CREATED)
        return Response({'message': 'Error al crear cotizacion'}, status=status.HTTP_400_BAD_REQUEST)
### Muestra cotizaciones por id o identificacion, elimina cotizaciones
class CotizacionDetail(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self, request, pk, format=None):
        queryset = Cotizacion.objects.filter(Q(id__contains=pk) | Q(
            solicitante__identificacion__icontains=pk)).order_by('-date_joined')[:10]
        print('Busedando cotizacion')
        serializer = CotizacionSerializer(queryset, many=True)
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        queryset = get_object_or_404(Cotizacion, id=pk)
        queryset.delete()
        return Response({'message': 'Cotizacion eliminada'})
#### Controllers de Productos por cotizacion
#Consulta ultima cotizacion y guarda productos en la ultima cotizacion
class CotizacionUltimo(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self,request,format=None):
        q = Cotizacion.objects.filter(
            created_by=request.user.username).latest('date_joined')
        print(q)
        serializer = CotizacionSerializer(instance=q)
        print(serializer.data)
        return Response(serializer.data) 
    def post(self, request):
        print('save Method')
        q = Cotizacion.objects.filter(created_by=request.user.username).latest('date_joined')
        print('encontrada ultima cotizacion',q)
        data = request.data.copy()
        print(data,'data')
        search = get_object_or_404(
            Producto, id=data.get('id'))
        data['producto'] = search.id
        data['cotizacion'] = q.id
        serializer = DetalleCotizacionSerializer(data=data)
        if q.id == data.get('cotizacion'):
            q.total = q.total + data.get('subtotal')
            q.save()
        if serializer.is_valid():
            q = DetalleCotizacion(
                producto=search,
                cotizacion=q,
                cantidad=data.get('cantidad'),
                subtotal=data.get('subtotal')
            )
            q.save()
            return Response({'message': 'Producto agregado a la cotizacion'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error al agregar producto a la cotizacion'}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        q = Cotizacion.objects.filter(created_by=request.user.username).latest('date_joined')
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Consulta productos en una cotizacion cotizacion
class ProductoCotizacion(APIView):
    permission_classes=[isCajero | isAdmin]

    def get(self, request, pk, format=None):
        queryset = get_list_or_404(DetalleCotizacion, cotizacion__id=pk)
        serializer = DetalleCotizacionSerializer(queryset, many=True)
        return Response(serializer.data)

#Controladores de Ventas

##### ver una venta y crearla
class VentaIndex(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self, request, format=None):
        queryset = Venta.objects.order_by('-date_joined')[:10]
        serializer = VentaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()
        q = Cliente.objects.get(identificacion=data.get('identificacion'))
        print(q)
        data['cliente'] = q.identificacion
        data['created_by'] = request.user.username
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            row = Venta(
                created_by=request.user.username,
                cliente=q,
                total = 0
            )
            row.save()
            return Response({'message': 'Venta creada'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error al crear venta'}, status=status.HTTP_400_BAD_REQUEST)
    
##### ver una venta y eliminarla
class VentaDetail(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self, request, pk, format=None):
        queryset = Venta.objects.filter(Q(id__contains=pk) | Q(
            cliente__identificacion__contains=pk)).order_by('id')[:10]
        serializer = VentaSerializer(queryset, many=True)
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        queryset = Venta.objects.filter(Q(id=pk) | Q(
            cliente__identificacion__contains=pk)).latest('id')
        q = ProductoVenta.objects.filter(venta__id=pk)
        for i in q:
            producto = Producto.objects.get(id=i.producto.id)
            producto.cantidad = producto.cantidad+i.cantidad
            producto.save()
        queryset.delete()
        return Response({'message': 'Venta eliminada'})
    def put(self,request,pk,format=None):
        data = request.data.copy()
        print(data['producto'])
        q = get_object_or_404(ProductoVenta,id=data['producto'],venta__id=pk)
        print('producto',q)
        serializer = ProductoVentaSerializer(q,data=data)
        if serializer.is_valid():
            r = Venta.objects.get(id=pk)
            r.total = r.total - q.subtotal
            r.total = r.total + data['subtotal']
            r.save()
            serializer.save()
            return Response({'message':'Producto actualizado'},status=status.HTTP_201_CREATED)
        return Response({'message':'se ha producido un error'})
##### ver ultima venta y agregar productos a la venta
class VentaUltimo(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self,request):
        q = Venta.objects.filter(created_by=request.user.username).latest('date_joined')
        serializer = VentaSerializer(instance=q)
        return Response(serializer.data)
    def post(self,request):
        q = Venta.objects.filter(
            created_by=request.user.username).latest('date_joined')
        data = request.data.copy()
        search = get_object_or_404(
            Producto, id=data.get('id'))
        data['producto'] = search.id
        data['venta'] = q.id
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            q = ProductoVenta(
                producto=search,
                venta=q,
                cantidad=data.get('cantidad'),
                subtotal=data.get('subtotal'),
            )
            q.save()
            r = Producto.objects.get(id=search.id)
            r.cantidad = r.cantidad - data.get('cantidad')
            s = Venta.objects.get(id=q.venta.id)
            s.total = s.total + q.subtotal
            r.save()
            s.save()
            return Response({'message': 'Producto agregado a la Venta'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error al agregar producto a la Venta'}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        q = Venta.objects.filter(created_by=request.user.username).latest('date_joined')
        q.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VentaProductosDetails(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self,request,pk,format=None):
        queryset = get_list_or_404(ProductoVenta,venta__id=pk)
        serializer = ProductoVentaSerializer(queryset,many=True)
        return Response (serializer.data)
    
class VentaPorID(APIView):
    permission_classes=[isCajero | isAdmin]
    def get(self,request,pk,format=None):
        queryset = get_object_or_404(Venta,id=pk)
        serializer = VentaSerializer(queryset)
        return Response(serializer.data)

class EliminarProductoDeVenta(APIView):
    permission_classes=[isCajero | isAdmin]
    def delete(self,request,pk):
        q = get_object_or_404(ProductoVenta,id=pk)
        r = Producto.objects.get(id=q.producto.id)
        s = Venta.objects.get(id=q.venta.id)
        r.cantidad = r.cantidad + q.cantidad
        val = s.total - q.subtotal
        s.total = val
        s.save()
        r.save()
        q.delete()
        return Response({'message':'Producto eliminado de la venta'}, status=status.HTTP_204_NO_CONTENT)