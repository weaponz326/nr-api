from django.urls import path, include

from . import views


urlpatterns = [
    path('account/', views.AccountView.as_view()),
    path('account/<id>', views.AccountDetailView.as_view()),
    path('transaction/', views.TransactionView.as_view()),
    path('transaction/<id>', views.TransactionDetailView.as_view()),
    path('all-transaction/', views.AllTransactionsView.as_view()),

    path('all-account-count/', views.AllAccountCountView.as_view()),
    path('transaction-share/', views.TransactionShareView.as_view()),
    path('transaction-annotate/', views.TransactionAnnotateView.as_view()),
]
