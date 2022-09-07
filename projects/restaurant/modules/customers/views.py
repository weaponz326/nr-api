from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from .models import Customer
from .serializers import CustomerSerializer
from accounts.paginations import TablePagination


# Create your views here.

class CustomerView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'account_name', 'account_number', 'bank_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        customer = Customer.objects.filter(account=account)
        results = self.paginate_queryset(customer, request, view=self)
        serializer = CustomerSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomerDetailView(APIView):
    def get(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
