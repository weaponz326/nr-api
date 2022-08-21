from rest_framework import serializers

from .models import TaskGroup, TaskItem


class TaskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGroup
        fields = [
            'id',
            'created_at',
            'updated_at',
            'user',
            'task_group',
        ]

class TaskItemSerializer(serializers.ModelSerializer):
    task_group = TaskGroupSerializer()
    
    class Meta:
        model = TaskItem
        fields = [
            'id',
            'updated_at',
            'task_group',
            'task_item',
            'description',
            'start_date',
            'end_date',
            'status',
        ]
