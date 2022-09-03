from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'id',
            'updated_at',
            'account',
            'customer',
            'reservation_code',
            'reservation_date',
            'number_guests',
            'number_tables',
            'arrival_date',
            'reservation_status',
        ]
