from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=50)
    rp_channel = models.IntegerField()

    class Meta:
        abstract = True


class InputDevice(Device):
    def get_input_value(self):
        #rpio get value
        pass

    def __str__(self):
        return self.name + ', input device on GPIO pin ' + str(self.rp_channel)


class OutputDevice(Device):
    def set_output(self, value):
        # Set gpio port
        pass

    def __str__(self):
        return self.name + ', output device on GPIO pin ' + str(self.rp_channel)


class Controller(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    input_device = models.ForeignKey(to=InputDevice, null=True, on_delete=models.SET_NULL)
    output_device = models.ForeignKey(to=OutputDevice, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField()
    set_point = models.FloatField()

    class Meta:
        abstract = True


class OnOffController(Controller):
    hysteresis = models.FloatField()

    def control(self):
        pass
        #GPIO stuff
