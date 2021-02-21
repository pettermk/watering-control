from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import User

from .models import InputDevice, OutputDevice, OnOffController, Host

class InputDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputDevice
        fields = '__all__'

class OutputDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputDevice
        fields = '__all__'

class ControllerSerializer(serializers.ModelSerializer):
    input_device = InputDeviceSerializer()
    output_device = OutputDeviceSerializer()
    class Meta:
        model = OnOffController
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    controllers = ControllerSerializer(many=True, read_only=True)
    class Meta:
        model = Host
        fields = '__all__'


### User serialization
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')
