from django.contrib import admin

from .models import Host, InputDevice, OutputDevice, OnOffController

admin.site.register(Host)
admin.site.register(InputDevice)
admin.site.register(OutputDevice)
admin.site.register(OnOffController)
