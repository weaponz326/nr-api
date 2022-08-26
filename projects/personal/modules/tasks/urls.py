from django.urls import path, include
from . import views


urlpatterns = [
    path('task-group/', views.TaskGroupView.as_view()),
    path('task-group/<id>', views.TaskGroupDetailView.as_view()),
    path('all-task-item/', views.AllTaskItemView.as_view()),
    path('task-item/', views.TaskItemView.as_view()),
    path('task-item/<id>', views.TaskItemDetailView.as_view()),

    path('task-group-count/', views.TaskGroupCountView.as_view()),
    path('task-item-count/', views.TaskItemCountView.as_view()),
    path('all-todo-count/', views.AllToDoCountView.as_view()),
    path('task-group-annotate/', views.TaskGroupAnnotateView.as_view()),
    path('task-item-annotate/', views.TaskItemAnnotateView.as_view()),
]
