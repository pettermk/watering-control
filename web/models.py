from django.db import models

class Device(models.Model):
    INPUT = 'input'
    OUTPUT = 'output'
    DEVICE_TYPE_CHOICES = (
        (INPUT, 'GPIO Input'),
        (OUTPUT, 'GPIO Output'),
    )

    device_type = models.CharField(
        max_length = 6,
        choices = DEVICE_TYPE_CHOICES,
        default = INPUT
    )

    rp_channel = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ', ' + self.device_type + ' at GPIO pin ' + str(self.rp_channel)
