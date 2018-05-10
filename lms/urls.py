from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('contas.urls')),
    path('', include('curriculo.urls')),
    path('', include('restrito.urls'))
]
