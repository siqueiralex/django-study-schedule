from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("custom_auth.urls")),
    path("administrador/", include("administrador.urls", namespace="administrador")),
    
    path("admin/", admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
