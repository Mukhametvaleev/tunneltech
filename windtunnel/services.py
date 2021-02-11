import grpc
from django.conf import settings

import proto.windtunnel_pb2_grpc as pb2_grpc
import proto.windtunneltypes_pb2 as pb2
from windtunnel.serializers import ReadResultsProtoSerializer


class WindTunnelServicer:
    def __init__(self):
        self.channel = grpc.insecure_channel(settings.WINDTUNNEL_GRPC_HOST)
        self.stub = pb2_grpc.WindTunnelStub(self.channel)

    def read_multi(self, read_request_dicts):
        parameters = [
            pb2.ReadRequest(**read_request_dict)
            for read_request_dict in read_request_dicts
        ]
        read_results = self.stub.ReadMulti(pb2.ReadRequests(parameters=parameters))
        return ReadResultsProtoSerializer(read_results).data
