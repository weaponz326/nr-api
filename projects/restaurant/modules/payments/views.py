from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from .models import Payment
from .serializers import PaymentDepthSerializer, PaymentSerializer
from accounts.paginations import TablePagination


# Create your views here.

class PaymentView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'payment_code', 'amount_paid', 'order.order_code', 'order.customer_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payment = Payment.objects.filter(account=account)
        results = self.paginate_queryset(payment, request, view=self)
        serializer = PaymentDepthSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PaymentDetailView(APIView):
    def get(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        serializer = PaymentDepthSerializer(payment)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
