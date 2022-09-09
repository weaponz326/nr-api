from turtle import update
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from .models import Delivery
from .serializers import DeliveryDepthSerializer, DeliverySerializer
from modules.orders.models import Order
from accounts.paginations import TablePagination


# Create your views here.

class DeliveryView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'account_name', 'account_number', 'bank_name']
    ordering = ['-created_at']
    
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        delivery = Delivery.objects.filter(account=account)
        results = self.paginate_queryset(delivery, request, view=self)
        serializer = DeliveryDepthSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        if Delivery.objects.filter(id=request.data.get('id')).exists():
            return Response("exists")
        else:
            serializer = DeliverySerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(id=request.data.get('id'))
                return Response(serializer.data)
            return Response(serializer.errors)

class DeliveryDetailView(APIView):
    def get(self, request, id, format=None):
        if Delivery.objects.filter(id=id).exists():
            delivery = Delivery.objects.get(id=id)
            serializer = DeliveryDepthSerializer(delivery)
            return Response(serializer.data)
        else:
            return Response('not exist')

    def put(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        serializer = DeliverySerializer(delivery, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)