from django.urls import path, include

from . import views


urlpatterns = [
    path('user-search/', views.UserSearchView.as_view()),
    path('user/<id>', views.UserDetailView.as_view()),
]
