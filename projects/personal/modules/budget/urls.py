from django.urls import path, include

from . import views


urlpatterns = [
    path('budget/', views.BudgetView.as_view()),
    path('budget/<id>', views.BudgetDetailView.as_view()),
    path('income/', views.IncomeView.as_view()),
    path('income/<id>', views.IncomeDetailView.as_view()),
    path('expenditure/', views.ExpenditureView.as_view()),
    path('expenditure/<id>', views.ExpenditureDetailView.as_view()),
    
    path('budget-count', views.budget_count),
    path('income-total', views.income_total),
    path('expenditure-total', views.expenditure_total),
]
