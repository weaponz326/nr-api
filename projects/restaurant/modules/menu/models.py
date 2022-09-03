from django.db import models

from accounts.models import CustomBaseModel, Account


# Create your models here.

class MenuGroup(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    menu_group = models.CharField(max_length=256, null=True)
    category = models.CharField(max_length=64, null=True)

    def __str__(self):
        return str(self.id)

class MenuItem(CustomBaseModel):
    menu_group = models.ForeignKey(MenuGroup, to_field='id', on_delete=models.DO_NOTHING)
    item_code = models.CharField(max_length=32, blank=True)
    item_name = models.CharField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
