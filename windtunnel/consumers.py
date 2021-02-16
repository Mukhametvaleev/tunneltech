from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from windtunnel import services


class GRPCWindTunnelConsumer(AsyncConsumer):
    def __init__(self):
        self.windtunnel_servicer = services.WindTunnelServicer()

    async def windtunnel_read_multi(self, message):
        read_request_dicts = message["message"]
        read_results_dict = self.windtunnel_servicer.read_multi(read_request_dicts)
        parameters = read_results_dict["parameters"]

        await self.channel_layer.group_send(
            "windtunnel_parameters",
            {"type": "windtunnel.parameters", "message": parameters},
        )


class WindTunnelConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"windtunnel_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def windtunnel_parameters(self, event):
        parameter_dicts = event["message"]

        await self.send_json(parameter_dicts)
