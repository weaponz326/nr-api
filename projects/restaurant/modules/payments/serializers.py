from rest_framework import serializers

from .models import Payment
from modules.orders.serializers import OrderSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            'id',
            'created_at',
            'account',
            'order',
            'payment_code',
            'payment_date',
            'amount_paid',
        ]
