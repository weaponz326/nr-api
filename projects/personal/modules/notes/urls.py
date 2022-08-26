from django.urls import path, include

from . import views


urlpatterns = [
    path('note/', views.NoteView.as_view()),
    path('note/<id>', views.NoteDetailView.as_view()),
    path('note-search/', views.NoteSearchView.as_view()),

    path('note-count/', views.NoteCountView.as_view()),
    path('note-annotate/', views.NoteAnnotateView.as_view()),
]
