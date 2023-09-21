from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('apps.CustomUser.urls')),
    path('api/v1/personas/', include('apps.Personas.urls')),
    path('api/v1/gestion/', include('apps.Gestion.urls')),
    path('api/v1/operaciones/', include('apps.Operaciones.urls')),
]
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]