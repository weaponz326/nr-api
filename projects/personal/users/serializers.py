from rest_framework import serializers

from .models import CustomBaseModel, User


class CustomBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomBaseModel
        fields = ['id', 'created_at', 'updated_at']

class UserSerializer(CustomBaseSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'location',
            'about',
            'photo'
        ]
