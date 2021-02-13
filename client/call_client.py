import time

import grpc
from service_pb2 import Configuration, Configurations
import service_pb2
import service_pb2_grpc

if __name__=='__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        for a in range(3):
            stub = service_pb2_grpc.WaterControllerStub(channel)
            conf = Configurations()
            conf.configurations.append(Configuration(config={
                'test': 'config',
                'second': 'test'
            }))
            conf.configurations.append(Configuration(config={
                'test': 'config2',
                'second': 'test'
            }))
            stub.SetConfig(conf)
            time.sleep(3)
            a = stub.GetValues(service_pb2.Configuration())
            print(a)

