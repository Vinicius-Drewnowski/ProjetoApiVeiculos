from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('veiculos.urls')),            # Página inicial /home
    path('api/', include('veiculos.api.urls')),    # API /api/veiculos/
]