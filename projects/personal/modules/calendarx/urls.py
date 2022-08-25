from django.urls import path, include

from . import views


urlpatterns = [
    path('calendar/', views.CalendarView.as_view()),
    path('calendar/<id>', views.CalendarDetailView.as_view()),
    path('schedule/', views.ScheduleView.as_view()),
    path('schedule/<id>', views.ScheduleDetailView.as_view()),
    path('all-schedule/', views.AllScheduleView.as_view()),

    path('calendar-count/', views.CalendarCountView.as_view()),
    path('schedule-count/', views.ScheduleCountView.as_view()),
    path('calendar-annotate/', views.CalendarAnnotateView.as_view()),
    path('schedule-annotate/', views.ScheduleAnnotateView.as_view()),
]
