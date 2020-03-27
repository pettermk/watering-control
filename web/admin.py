from django.contrib import admin

from .models import InputDevice, OutputDevice, OnOffController

admin.site.register(InputDevice)
admin.site.register(OutputDevice)
admin.site.register(OnOffController)
