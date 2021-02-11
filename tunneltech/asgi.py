import os

import django
from channels.routing import (
    ChannelNameRouter,
    ProtocolTypeRouter,
    URLRouter,
)
from django.core.asgi import get_asgi_application

import windtunnel.consumers
import windtunnel.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tunneltech.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(windtunnel.routing.websocket_urlpatterns),
        "channel": ChannelNameRouter(
            {
                "grpc-windtunnel": windtunnel.consumers.GRPCWindTunnelConsumer.as_asgi(),
            }
        ),
    }
)
