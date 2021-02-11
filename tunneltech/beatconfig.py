from django.conf import settings


BEAT_SCHEDULE = {
    "grpc-windtunnel": [
        {
            "type": "windtunnel.read.multi",
            "message": [
                {"name": "fan.drive.input.voltage", "tags": "fan=1"},
                {"name": "fan.drive.input.voltage", "tags": "fan=2"},
                {"name": "current.session.time.elapsed"},
                {"name": "current.session.time.left"},
            ],
            "schedule": settings.WINDTUNNEL_READ_MULTI_SCHEDULE,
        },
    ]
}
