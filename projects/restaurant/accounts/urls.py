from django.urls import path, include

from . import views


urlpatterns = [
    path('account/', views.AccountView.as_view()),
    path('account/<id>', views.AccountDetailView.as_view()),

    path('search-list/', views.AccountSearchView.as_view()),
    path('search-detail/<id>', views.AccountDetailView.as_view()),

    # path('account-exist/', views.AccountExistView.as_view()),
    # path('user-accounts/', views.UserAccountsView.as_view()),
]
