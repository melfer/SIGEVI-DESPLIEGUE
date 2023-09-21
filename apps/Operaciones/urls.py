from rest_framework.urlpatterns import format_suffix_patterns
from . import views as v
from django.urls import path

urlpatterns = [
    # URL de Corizacion
    # Ver Cotizacion
    path('cotizacion/', v.CotizacionIndex.as_view()),
    # Detalles de Cotizacion, eliminar
    path('cotizacion/detail/<int:pk>/', v.CotizacionDetail.as_view()),
    #Operaciones de eliminar y obtener ultima cotizacion
    path('cotizaciones/latest/', v.CotizacionUltimo.as_view()),
    # URLS para detalles de Cotizacion
    # Ver Productos en Cotizacion
    path('cotizacion/producto/<int:pk>/', v.ProductoCotizacion.as_view()),

    #URLs para ventas
    #ver ventas
    path('ventas/', v.VentaIndex.as_view()),
    #detalles de venta, actualizar unidades de una venta procesada
    path('ventas/detail/<int:pk>/', v.VentaDetail.as_view()),	
    #Operaciones de eliminar y obtener ultima venta
    path('ventas/latest/', v.VentaUltimo.as_view()),
    # URLS para detalles de venta
    #Ver productos en venta
    path('ventas/consulta/<pk>/', v.VentaProductosDetails.as_view()),
    #Consultar venta por ID
    path('ventas/<int:pk>/',v.VentaPorID.as_view()),
    #Eliminar Producto de una Venta
    path('ventas/deleteProduct/<int:pk>/',v.EliminarProductoDeVenta.as_view()),
    
]
