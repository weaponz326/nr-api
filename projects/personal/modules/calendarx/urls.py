from django.urls import path, include

from . import views


urlpatterns = [
    path('calendar/', views.CalendarView.as_view()),
    path('calendar/<id>', views.CalendarDetailView.as_view()),
    path('schedule/', views.ScheduleView.as_view()),
    path('schedule/<id>', views.ScheduleDetailView.as_view()),
    path('all-schedule/', views.AllScheduleView.as_view()),

    path('calendar-count/', views.calendar_count),
    path('schedule-count/', views.schedule_count),
    path('calendar-annotate/', views.calendar_annotate),
    path('schedule-annotate/', views.schedule_annotate),
]
