import datetime
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.filters import OrderingFilter

from .models import TaskGroup, TaskItem
from .serializers import TaskGroupSerializer, TaskItemNestedSerializer, TaskItemSerializer
from users.paginations import TablePagination
from users.services import fillZeroDates


# Create your views here.

class TaskGroupView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['task_group', 'created_at']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        task_group = TaskGroup.objects.filter(user=user)
        results = self.paginate_queryset(task_group, request, view=self)
        serializer = TaskGroupSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TaskGroupDetailView(APIView):
    def get(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        serializer = TaskGroupSerializer(task_group)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        serializer = TaskGroupSerializer(task_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        task_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------
# task item

class AllTaskItemView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['task_group', 'task_item', 'priority', 'start_date', 'end_date', 'status']
    ordering = ['-pkid']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        task_item = TaskItem.objects.filter(task_group__user=user)
        results = self.paginate_queryset(task_item, request, view=self)
        serializer = TaskItemNestedSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class TaskItemView(APIView):
    def get(self, request, format=None):
        task_group = self.request.query_params.get('task_group', None)
        task_item = TaskItem.objects.filter(task_group=task_group)
        serializer = TaskItemSerializer(task_item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TaskItemDetailView(APIView):
    def get(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        serializer = TaskItemSerializer(task_item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        serializer = TaskItemSerializer(task_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        task_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

class TaskGroupCountView(APIView):
    def get(self, request, format=None):
        count = TaskGroup.objects\
            .filter(user__id=self.request.query_params.get('user', None))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .count()           
        content = {'count': count}
        return Response(content)

class TaskItemCountView(APIView):
    def get(self, request, format=None):
        count = TaskItem.objects\
            .filter(task_group__user__id=self.request.query_params.get('user', None))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .count()           
        content = {'count': count}
        return Response(content)

class AllToDoCountView(APIView):
    def get(self, request, format=None):
        count = TaskItem.objects\
            .filter(task_group__user__id=self.request.query_params.get('user', None), status="To Do")\
            .count()           
        content = {'count': count}
        return Response(content)

class TaskGroupAnnotateView(APIView):
    def get(self, request, format=None):
        items = TaskGroup.objects\
            .filter(user__id=self.request.query_params.get('user', None))\
            .annotate(date=TruncDate('created_at'))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .values('date').annotate(count=Count('id')).order_by('-date')
        filled_items = fillZeroDates(items)
        return Response(filled_items)

class TaskItemAnnotateView(APIView):
    def get(self, request, format=None):
        items = TaskItem.objects\
            .filter(task_group__user__id=self.request.query_params.get('user', None))\
            .annotate(date=TruncDate('created_at'))\
            .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
            .values('date').annotate(count=Count('id')).order_by('-date')
        filled_items = fillZeroDates(items)
        return Response(filled_items)
