from django.db import models
from users.models import CustomBaseModel, User


# Create your models here.

class Calendar(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    calendar_name = models.CharField(null=True, blank=True, max_length=256)

    def __str__(self):
        return str(self.id)

class Schedule(CustomBaseModel):
    calendar = models.ForeignKey(Calendar, to_field='id', on_delete=models.DO_NOTHING)
    schedule_name = models.CharField(null=True, blank=True, max_length=256)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=256)
    status = models.CharField(null=True, blank=True, max_length=32)

    def __str__(self):
        return str(self.id)
