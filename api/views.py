from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Store, StoreVisitLog
from .serializers import StoreSerializer, StoreVisitLogSerializer


class StoreViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def filter_queryset(self, queryset):
        phone_number = self.request.query_params.get('phone')
        return queryset.filter(
            employee__phone=phone_number
        )


class StoreVisitViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = StoreVisitLogSerializer
    permission_classes = [AllowAny]
    queryset = StoreVisitLog.objects.none()

    def create(self, request, *args, **kwargs):
        phone = request.GET.get('phone')

        serializer = self.get_serializer(data=request.data, context={'phone': phone})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

