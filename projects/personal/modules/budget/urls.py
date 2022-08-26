from django.urls import path, include

from . import views


urlpatterns = [
    path('budget/', views.BudgetView.as_view()),
    path('budget/<id>', views.BudgetDetailView.as_view()),
    path('income/', views.IncomeView.as_view()),
    path('income/<id>', views.IncomeDetailView.as_view()),
    path('expenditure/', views.ExpenditureView.as_view()),
    path('expenditure/<id>', views.ExpenditureDetailView.as_view()),
    
    path('budget-count', views.BudgetCountView.as_view()),
    path('income-total', views.IncomeTotalView.as_view()),
    path('expenditure-total', views.ExpenditureTotalView.as_view()),
]
