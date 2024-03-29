from django.contrib import admin

from .models import Calendar, Schedule


# Register your models here.

class CalednarAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'calendar_name', 'created_at')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'calendar', 'schedule_name', 'start_date', 'status')

admin.site.register(Calendar, CalednarAdmin)
admin.site.register(Schedule, ScheduleAdmin)
