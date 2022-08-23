from rest_framework import serializers

from .models import Calendar, Schedule


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = [
            'id',
            'created_at',
            'updated_at',
            'user',
            'calendar_name',
        ]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'updated_at',
            'calendar',
            'schedule_name',
            'description',
            'start_date',
            'end_date',
            'location',
            'status',
        ]

class ScheduleNestedSerializer(serializers.ModelSerializer):
    calendar = CalendarSerializer()

    class Meta:
        model = Schedule
        fields = [
            'id',
            'updated_at',
            'calendar',
            'schedule_name',
            'description',
            'start_date',
            'end_date',
            'location',
            'status',
        ]
