from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import home
from django.urls import path, include

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('update/', include('updates.urls')),
    path('status/', include('status.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
