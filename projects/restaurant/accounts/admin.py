from django.contrib import admin

from .models import Account, User


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'name', 'location')

class UserAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'email')

admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)
