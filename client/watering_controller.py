import service_pb2
import service_pb2_grpc
import grpc
from concurrent import futures
import threading
import logging

class RPIController:
    def __init__(self):
        self._config = {}
        threading.Timer(5, self.control).start()
    
    def SetConfig(self, config: dict) -> None:
        self._config = config

    def control(self):
        print(f'Controlling using config {self._config}')
        threading.Timer(5, self.control).start()


class WaterControllerServer(service_pb2_grpc.WaterController):
    def __init__(self):
        self._rpi_controller = RPIController()
    
    def SetConfig(self, request, context):
        print(f'Set config as {request.config}')
        logging.info(f'Set config as {request.config}')
        self._rpi_controller.SetConfig(request.config)
        return service_pb2.Status(ok=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    service_pb2_grpc.add_WaterControllerServicer_to_server(WaterControllerServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
