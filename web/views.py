from django.shortcuts import render

from rest_framework.views import APIView
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import InputDevice, OutputDevice, OnOffController
from .serializers import (InputDeviceSerializer,
    OutputDeviceSerializer,
    ControllerSerializer,
    UserSerializer,
    UserSerializerWithToken,
)


def index(request):
    devices = InputDevice.objects.all()
    context = {'input_device_list' : devices}

    return render(request, 'web/index.html', context)


class InputDeviceList(APIView):
    """
    List all input devices, or create a new snippet.
    """
    def get(self, request, format=None):
        input_devices = InputDevice.objects.all()
        serializer = InputDeviceSerializer(input_devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InputDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OutputDeviceList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = OutputDevice.objects.all()
        serializer = OutputDeviceSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OutputDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ControllerList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        controllers = OnOffController.objects.all()
        serializer = ControllerSerializer(controllers, many=True)
        return Response(serializer.data)


### User authentication

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)