from rest_framework.urlpatterns import format_suffix_patterns
from . import views as v
from django.urls import path

urlpatterns = [
    # URLS Marca
    path('marcas/', v.MarcaIndex.as_view()),
    path('marcas/<int:pk>/', v.MarcaDetail.as_view()),
    path('marcas/search/<str:name>/', v.MarcaSearch.as_view()),
    # URLS Categoria
    path('categorias/', v.CategoriaIndex.as_view()),
    path('categorias/<int:pk>/', v.CategoriaDetail.as_view()),
    path('categorias/search/<str:name>/', v.CategoriaSearch.as_view()),
    # URLS Marcas y Categorias
    path('categorias/<id>/detalles/', v.MarcaCategoriaIndex.as_view()),
    path('categorias/<id>/filtro/', v.FiltrarMarcasEnCategorias.as_view()),
    path('categorias/<categoria_id>/eliminar/<marca_id>/',
         v.EliminarMarcaEnCategoria.as_view()),
    path('categorias/search/<id>/marca/<nombre>/',
         v.BuscarMarcasEnCategorias.as_view()),
    path('categorias/find/<str:nombre>/',
         v.MarcaCategoriaDetail.as_view()),
    path('categorias/find/<str:nombre>/<str:marca>/',
         v.MarcaCategoriaDetailAdvanced.as_view()),

    # URLS Producto
    path('productos/', v.ProductoIndex.as_view()),
    path('productos/<int:pk>/', v.ProductoDetail.as_view()),
    path('productos/search/<str:name>/', v.ProductoSearch.as_view()),
    path('productos/report/', v.ProductoReport.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
