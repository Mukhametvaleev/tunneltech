from django.urls import path

from windtunnel import consumers

websocket_urlpatterns = [
    path(
        "windtunnels/default/<room_name>",
        consumers.WindTunnelConsumer.as_asgi(),
    ),
]
