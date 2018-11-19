from django.db import models


class Device(models.Model):
    rp_channel = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=50)

    class Meta:
        abstract = True


class InputDevice(Device):
    def __str__(self):
        return self.name + ', input device on GPIO pin ' + str(self.rp_channel)


class OutputDevice(Device):
    def __str__(self):
        return self.name + ', output device on GPIO pin ' + str(self.rp_channel)

