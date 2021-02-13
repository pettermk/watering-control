protos:
	python -m grpc_tools.protoc -Iclient --python_out=client --grpc_python_out=client client/service.proto
