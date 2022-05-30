from django.urls import path, include
from rest_framework import routers
from .views import StoreViewSet, StoreVisitViewSet


app_name = "visits"

router = routers.DefaultRouter()
router.register(r'store-list', StoreViewSet, basename='shops')
router.register(r'store-visit', StoreVisitViewSet, basename='visit')


urlpatterns = [
    path('api/', include(router.urls)),
]