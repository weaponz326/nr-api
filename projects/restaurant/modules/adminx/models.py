from django.db import models

from accounts.models import CustomBaseModel, Account


# Create your models here.

class AccountUser(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)
    personal_id = models.CharField(null=True, max_length=200)
    personal_name = models.CharField(null=True, max_length=100)
    access_level = models.CharField(null=True, max_length=20)

    def __str__(self):
        return str(self.id)

class Access(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    admin_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    menu_access = models.BooleanField(default=False)
    staff_access = models.BooleanField(default=False)
    tables_access = models.BooleanField(default=False)
    customers_access = models.BooleanField(default=False)
    deliveries_access = models.BooleanField(default=False)
    payments_access = models.BooleanField(default=False)
    roster_access = models.BooleanField(default=False)
    reservations_access = models.BooleanField(default=False)
    orders_access = models.BooleanField(default=False)
    kitchen_stock_access = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Invitation(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    invitee_id = models.CharField(null=True, max_length=200)
    invitee_name = models.CharField(null=True, max_length=200)
    invitation_status = models.CharField(null=True, max_length=30)
    date_sent = models.DateTimeField(null=True, auto_now=True)
    date_confirmed = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.id)
