import service_pb2
import service_pb2_grpc
import grpc
from concurrent import futures
from typing import List
import threading
import logging

class RPIController:
    def __init__(self):
        self._configurations = []
        threading.Timer(5, self.control).start()
    
    def set_configurations(self, configurations: service_pb2.Configurations) -> None:
        self._configurations = []
        for config in configurations:
            self._configurations.append(config)

    def get_values(self):
        retval = service_pb2.Values()
        for a in range(3):
            ret = service_pb2.Value()
            ret.device = 'test'
            ret.value = 3.
            retval.values.append(ret)
        return retval #[service_pb2.Value(device='bla', value=2)]

    def control(self):
        print(f'Controlling using config {self._configurations}')
        threading.Timer(5, self.control).start()


class WaterControllerServer(service_pb2_grpc.WaterController):
    def __init__(self):
        self._rpi_controller = RPIController()
    
    def SetConfig(self, request, context):
        print(f'Set config as {request.configurations}')
        logging.info(f'Set config as {request.configurations}')
        self._rpi_controller.set_configurations(request.configurations)
        return service_pb2.Status(ok=True)

    def GetValues(self, request, context):
        print(f'getting values')
        values = self._rpi_controller.get_values()
        logging.info(f'getting values')
        return values

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    service_pb2_grpc.add_WaterControllerServicer_to_server(WaterControllerServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
