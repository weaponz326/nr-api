from rest_framework import serializers

from .models import Account, CustomBaseModel


# # TODO: custom base serializer not working
# class CustomBaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomBaseModel
#         fields = ['id', 'created_at', 'updated_at']

# class UserSerializer(CustomBaseSerializer):
#     class Meta:
#         model = Account
#         fields = [
#             'name',
#             'location',
#             'about',
#             'logo'
#         ]

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'created_at',
            'updated_at',
            'name',
            'location',
            'about',
            'logo',
            'creator_id',
            'creator_name',
        ]
