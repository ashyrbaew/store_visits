from django.contrib import admin
from django.urls import path, include


api_endpoints = [
    path('', include('api.urls')),
]

urlpatterns = [
    path("", include(api_endpoints)),
    path('admin/', admin.site.urls),
]
