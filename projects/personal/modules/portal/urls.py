from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink/<id>', views.RinkDetailView.as_view()),
    path('rink-list/', views.AllRinkView.as_view()),

    path('rink-share-count/', views.RinkShareCountView.as_view()),
    path('rink-share-annotate/', views.RinkShareAnnotateView.as_view()),
]
