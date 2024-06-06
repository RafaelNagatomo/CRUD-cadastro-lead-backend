from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json


# def databaseEmDjango():

#     data = User.objects.get()         retorna obj

#     data = User.objects.filter()      retorna queryset

#     data = User.objects.exclude()     retorna queryset

#     data.save()

#     data.delete()


@api_view(['GET'])
def getUsers(request):

    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    return Response(status=status.HTTP_404_BAD_REQUEST)
