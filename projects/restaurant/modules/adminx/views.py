import uuid

from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import AccountUser, Access, Invitation
from .serializers import AccountUserSerializer, AccessSerializer, InvitationSerializer
from accounts.models import Account


# Create your views here.

# users

class AccountUserView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        user = AccountUser.objects.filter(account=account)
        serializer = AccountUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccountUserDetailView(APIView):
    def get(self, request, id, format=None):
        user = AccountUser.objects.get(id=id)
        serializer = AccountUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = AccountUser.objects.get(id=id)
        serializer = AccountUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        user = AccountUser.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# all accounts of an account belonging to a user
class AccountUserAccountView(APIView):
    def get(self, request, format=None):
        personal_id = self.request.query_params.get('personal_id', None)
        user = AccountUser.objects.filter(personal_id=personal_id)
        serializer = AccountUserSerializer(user, many=True)
        return Response(serializer.data)


# access
# ---------------------------------------------------------------------------

class AccessView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        access = Access.objects.filter(account=account)
        serializer = AccessSerializer(access, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccessDetailView(APIView):
    def get(self, request, id, format=None):
        access = Access.objects.get(id=id)
        serializer = AccessSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Access.objects.get(id=id)
        serializer = AccessSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Access.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------------------------

class InvitationView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        invitation = Invitation.objects.filter(account=account)
        serializer = InvitationSerializer(invitation, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class InvitationDetailView(APIView):
    def get(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------
# signals

@receiver(post_save, sender=Account)
def save_account_user(sender, instance, created, **kwargs):
    if created:
        AccountUser.objects.create(
            account=Account.objects.get(id=instance.id),
            is_creator=True,
            personal_id=instance.creator_id,
            personal_name=instance.creator_name,
            access_level="Admin",
        )

@receiver(post_save, sender=AccountUser)
def save_access(sender, instance, created, **kwargs):
    if created:
        if instance.access_level == "Admin":
            Access.objects.create(
                id=instance.id,
                account=Account.objects.get(id=uuid.UUID(str(instance.account))),
                admin_access=True,
                portal_access=True,
                settings_access=True,
                menu_access=True,
                staff_access=True,
                tables_access=True,
                customers_access=True,
                deliveries_access=True,
                payments_access=True,
                roster_access=True,
                reservations_access=True,
                orders_access=True,
                kitchen_stock_access=True,
            )
        else:
            Access.objects.create(
                id=instance.id,
                account=Account.objects.get(id=uuid.UUID(str(id=instance.account))),
                admin_access=False,
                portal_access=False,
                settings_access=False,
                menu_access=False,
                staff_access=False,
                tables_access=False,
                customers_access=False,
                deliveries_access=False,
                payments_access=False,
                roster_access=False,
                reservations_access=False,
                orders_access=False,
                kitchen_stock_access=False,
            )
