from django.shortcuts import render
from django.shortcuts import render
from products.serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
# Create your views here.


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(username)
        print(password)
        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "access",
                "user_id": user.id,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

        )
