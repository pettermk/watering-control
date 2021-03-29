from django.db.models.signals import post_save
from django.dispatch import receiver
import grpc
from google.protobuf.struct_pb2 import Struct

from web.models import OnOffController, Host
from web.serializers import ControllerSerializer, HostSerializer
from web.grpc.service_pb2 import Configuration, Configurations, Input, Output, Controller
from web.grpc import service_pb2_grpc

def config_from_controller(controller: dict):
    input_pb = Struct()
    input_pb.update(dict(controller.pop('input_device')))
    output_pb = Struct()
    output_pb.update(dict(controller.pop('output_device')))
    controller_pb = Struct()
    controller_pb.update(dict(controller))
    config = Configuration(
        input=Input(properties=input_pb),
        output=Output(properties=output_pb),
        controller=Controller(properties=controller_pb),
    )
    return config

def get_configurations(host: Host) -> Configurations:
    serializer = HostSerializer(host)
    controllers = serializer.data['controllers']
    conf = Configurations()
    for controller in controllers:
        c = config_from_controller(controller)
        conf.configurations.append(c)
    return conf


@receiver(post_save, sender=OnOffController)
def update_controller(sender, instance: OnOffController, **kwargs):
    host: Host = instance.host
    ip_address: str = host.ip_address
    configurations: Configurations = get_configurations(host)
    # with grpc.insecure_channel(f'{ip_address}:50051') as channel:
    #     stub = service_pb2_grpc.WaterControllerStub(channel)
    #     stub.AddControllers(configurations)

