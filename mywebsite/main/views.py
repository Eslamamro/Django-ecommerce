from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.

class CreateUser(APIView):

    def post(self, request):
        pass
