import datetime
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter

from .models import Calendar, Schedule
from .serializers import CalendarSerializer, ScheduleNestedSerializer, ScheduleSerializer
from users.paginations import TablePagination
from users.services import fillZeroDates


# Create your views here.

class CalendarView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['calendar_name', 'created_at']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        calendar = Calendar.objects.filter(user=user)
        results = self.paginate_queryset(calendar, request, view=self)
        serializer = CalendarSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CalendarDetailView(APIView):
    def get(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        serializer = CalendarSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        serializer = CalendarSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------
# schedule

class AllScheduleView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['schedule_name', 'calendar', 'start_date', 'end_date', 'status']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        schedule = Schedule.objects.filter(calendar__user=user)
        results = self.paginate_queryset(schedule, request, view=self)
        serializer = ScheduleNestedSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class ScheduleView(APIView, TablePagination):
    def get(self, request, format=None):
        calendar = self.request.query_params.get('calendar', None)
        schedule = Schedule.objects.filter(calendar=calendar)
        serializer = ScheduleSerializer(schedule, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ScheduleDetailView(APIView):
    def get(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        serializer = ScheduleSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        serializer = ScheduleSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------
# dashboard

class CalendarCountView(APIView):
    def get(self, request, format=None):
        count = Calendar.objects\
            .filter(user__id=self.request.query_params.get('user', None))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .count()            
        content = {'count': count}
        return Response(content)

class ScheduleCountView(APIView):
    def get(self, request, format=None):
        count = Schedule.objects\
            .filter(calendar__user__id=self.request.query_params.get('user', None))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .count()            
        content = {'count': count}
        return Response(content)

class CalendarAnnotateView(APIView):
    def get(self, request, format=None):
        items = Calendar.objects\
            .filter(user__id=self.request.query_params.get('user', None))\
            .annotate(date=TruncDate('created_at'))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .values('date').annotate(count=Count('id')).order_by('-date')
        filled_items = fillZeroDates(items)
        return Response(filled_items)

class ScheduleAnnotateView(APIView):
    def get(self, request, format=None):
        items = Schedule.objects\
            .filter(calendar__user__id=self.request.query_params.get('user', None))\
            .annotate(date=TruncDate('created_at'))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .values('date').annotate(count=Count('id')).order_by('-date')
        filled_items = fillZeroDates(items)
        return Response(filled_items)

