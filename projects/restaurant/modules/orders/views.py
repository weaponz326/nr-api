from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from .models import Order, OrderItem
from .serializers import OrderDepthSerializer, OrderSerializer, OrderItemSerializer
from accounts.paginations import TablePagination


# Create your views here.

class OrderView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'account_name', 'account_number', 'bank_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        order = Order.objects.filter(account=account)
        results = self.paginate_queryset(order, request, view=self)
        serializer = OrderSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderDepthSerializer(order)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# order item

class OrderItemView(APIView):
    def get(self, request, format=None):
        order = self.request.query_params.get('order', None)
        item = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if order_type == delivery

        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class OrderItemDetailView(APIView):
    def get(self, request, id, format=None):
        item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = OrderItem.objects.get(id=id)
        serializer = OrderItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = OrderItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)