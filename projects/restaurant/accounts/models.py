from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from .managers import CustomBaseManager, CustomUserManager


def accounts_upload_path(instance, filename):
    return instance.account.id + '/account/logo'

# Create your models here.

# base model for all models
# implements uuid for keys and softdelete features
class CustomBaseModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = CustomBaseManager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def remove(self):
        super(CustomBaseModel, self).delete()

class User(AbstractUser, CustomBaseModel):
    username = None
    email = models.EmailField(max_length=256, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)
         
class Account(CustomBaseModel):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    about = models.TextField()
    logo = models.FileField(null=True, blank=True, upload_to=accounts_upload_path)
    creator_id = models.CharField(max_length=256)
    creator_name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id)
