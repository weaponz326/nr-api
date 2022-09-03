from rest_framework import serializers
from .models import AccountUser, Access, Invitation

from accounts.serializers import AccountSerializer


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = [
            'id',
            'created_at',
            'account',
            'personal_id',
            'personal_name',
            'access_level',
        ]

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = [
            'id',
            'created_at',
            'admin_access',
            'portal_access',
            'settings_access',
            'menu_access',
            'staff_access',
            'tables_access',
            'customers_access',
            'deliveries_access',
            'payments_access',
            'roster_access',
            'reservations_access',
            'orders_access',
            'kitchen_stock_access',
        ]

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = [
            'id',
            'created_at',
            'account',
            'invitee_id',
            'invitee_name',
            'invitation_status',
            'date_sent',
            'date_confirmed',
        ]
