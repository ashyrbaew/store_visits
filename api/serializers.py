from rest_framework import serializers
from .models import Store, StoreVisitLog


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'store_name')


class StoreVisitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreVisitLog
        fields = '__all__'

    def validate(self, attrs):
        if attrs['store'].employee.phone != self.context['phone']:
            raise serializers.ValidationError(
             'Переданный номер не привязан к торговой точке'
            )

        return attrs
