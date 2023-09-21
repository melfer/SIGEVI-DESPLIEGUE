from rest_framework.urlpatterns import format_suffix_patterns
from . import views as v
from django.urls import path 

urlpatterns = [
    #URL de clientes
    path('clientes/',v.ClienteIndex.as_view()),
    path('clientes/<int:pk>/',v.ClienteDetail.as_view()),
    path('clientes/search/<int:pk>/',v.ClienteSearch.as_view()),
    
    #URL de proveedores
    path('proveedores/',v.ProveedorIndex.as_view()),
    path('proveedores/<int:pk>/',v.ProveedorDetail.as_view()),
    path('proveedores/search/<pk>/',v.ProveedorSearch.as_view()	),
]