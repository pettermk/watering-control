from django.shortcuts import render

from .models import InputDevice


def index(request):
    devices = InputDevice.objects.all()
    context = {'input_device_list' : devices}

    return render(request, 'web/index.html', context)
