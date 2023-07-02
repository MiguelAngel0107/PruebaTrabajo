from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bacterias/', include('apps.bacterias.urls')),
    path("admin/", admin.site.urls),
]
