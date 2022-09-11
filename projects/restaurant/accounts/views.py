from functools import partial
from django.shortcuts import render
from django.contrib.sessions.backends.db import SessionStore

from rest_framework.response import Response
from rest_framework import generics, request, status
from rest_framework import filters
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer
# from modules.module_admin.serializers import UserAccountsSerializer
# from modules.module_admin.models import User


# Create your views here.

class AccountView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        account = Account.objects.filter(account=account)
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccountDetailView(APIView):
    def get(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        account = Account.objects.get(id=id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------

# restaurant search

class AccountSearchView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # TODO:
    # account = request.query_params.get('account', None)
    # exclude_field = [id=account]

# ----------------------------------------------------------------------------------------------

# # checks if user has a restaurant acount
# class AccountExistView(APIView):
#     def post(self, request, *args, **kwargs):
#         user = User.objects.filter(personal_id=request.data.get('personal_id'))
#         if user.exists():
#             return Response({'has_account': True})
#         else:
#             return Response({'has_account': False})

# # get all restaurant suites of a personal id
# class UserAccountsView(generics.ListAPIView):
#     serializer_class = UserAccountsSerializer

#     def get_queryset(self):
#         queryset = User.objects.all()
#         personal_id = self.request.query_params.get('personal_id', None)
#         if personal_id is not None:
#             queryset = queryset.filter(personal_id=personal_id)
#         return queryset
