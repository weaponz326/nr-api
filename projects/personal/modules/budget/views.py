import datetime
from django.shortcuts import render
from django.db.models import Sum

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.filters import OrderingFilter

from .models import Budget, Income, Expenditure
from .serializers import BudgetSerializer, IncomeSerializer, ExpenditureSerializer
from users.paginations import TablePagination


# Create your views here.

class BudgetView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['budget_name', 'budget_type']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        budget = Budget.objects.filter(user=user)
        results = self.paginate_queryset(budget, request, view=self)
        serializer = BudgetSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BudgetDetailView(APIView):
    def get(self, request, id, format=None):
        budget = Budget.objects.get(id=id)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        budget = Budget.objects.get(id=id)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        budget = Budget.objects.get(id=id)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# income
# --------------------------------------------------------------------------------------------------

class IncomeView(APIView):
    def get(self, request, format=None):
        budget = self.request.query_params.get('budget', None)
        income = Income.objects.filter(budget=budget)
        serializer = IncomeSerializer(income, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class IncomeDetailView(APIView):
    def get(self, request, id, format=None):
        income = Income.objects.get(id=id)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        income = Income.objects.get(id=id)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        income = Income.objects.get(id=id)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# income
# --------------------------------------------------------------------------------------------------

class ExpenditureView(APIView):
    def get(self, request, format=None):
        budget = self.request.query_params.get('budget', None)
        expenditure = Expenditure.objects.filter(budget=budget)
        serializer = ExpenditureSerializer(expenditure, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenditureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ExpenditureDetailView(APIView):
    def get(self, request, id, format=None):
        expenditure = Expenditure.objects.get(id=id)
        serializer = ExpenditureSerializer(expenditure)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        expenditure = Expenditure.objects.get(id=id)
        serializer = ExpenditureSerializer(expenditure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        expenditure = Expenditure.objects.get(id=id)
        expenditure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------------------------------------------------------------
# dashboard

class BudgetCountView(APIView):
    def get(self, request, format=None):
        count = Budget.objects\
            .filter(user__id=self.request.query_params.get('user', None))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .count()            
        content = {'count': count}
        return Response(content)

class IncomeTotalView(APIView):
    def get(self, request, format=None):
        total = Income.objects\
            .filter(budget__user__id=self.request.query_params.get('user', None))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .aggregate(Sum('amount'))            
        content = {'total': total}
        return Response(content)

class ExpenditureTotalView(APIView):
    def get(self, request, format=None):
        total = Expenditure.objects\
            .filter(budget__user__id=self.request.query_params.get('user', None))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .aggregate(Sum('amount'))            
        content = {'total': total}
        return Response(content)
