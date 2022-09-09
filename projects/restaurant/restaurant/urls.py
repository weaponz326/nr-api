"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls')),

    path('accounts/', include('accounts.urls')),
    path('module-admin/', include('modules.adminx.urls')),
    path('module-portal/', include('modules.portal.urls')),
    path('module-settings/', include('modules.settings.urls')),
    path('module-menu/', include('modules.menu.urls')),
    path('module-staff/', include('modules.staff.urls')),
    path('module-payments/', include('modules.payments.urls')),
    path('module-orders/', include('modules.orders.urls')),
    path('module-kitchen-stock/', include('modules.kitchen_stock.urls')),
    path('module-roster/', include('modules.roster.urls')),
    path('module-tables/', include('modules.tables.urls')),
    path('module-deliveries/', include('modules.deliveries.urls')),
    path('module-reservations/', include('modules.reservations.urls')),
    path('module-customers/', include('modules.customers.urls')),
]