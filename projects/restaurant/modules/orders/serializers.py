from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'id',
            'created_at',
            'account',
            'customer',
            'order_code',
            'order_date',
            'customer_name',
            'order_type',
            'order_status',
            'order_total',
        ]

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'created_at',
            'order',
            'menu_item',
            'quantity',
        ]
