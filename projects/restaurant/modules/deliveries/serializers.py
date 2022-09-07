from rest_framework import serializers

from .models import Delivery
from modules.orders.serializers import OrderSerializer


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = [
            'id',
            'created',
            'account',
            'order',
            'delivery_code',
            'delivery_date',
            'customer_location',
            'delivery_status',
        ]

class DeliveryDepthSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Delivery
        fields = [
            'id',
            'created',
            'account',
            'order',
            'delivery_code',
            'delivery_date',
            'customer_location',
            'delivery_status',
        ]
