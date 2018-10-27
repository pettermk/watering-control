from django.shortcuts import render

from .models import Device


def index(request):
    devices = Device.objects.all()
    context = {'device_list' : devices}

    return render(request, 'web/index.html', context)
