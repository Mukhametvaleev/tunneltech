from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "fnf)88h=&gvm%qut34%ue!gki-wnon8c=b@8o#qic98hgls6lq"
DEBUG = True

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_grpc_framework",
    "manifest_loader",
    "beatserver",
    "channels",
    "frontend",
    "windtunnel.apps.WindtunnelConfig",
]

ROOT_URLCONF = "tunneltech.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    }
}

ASGI_APPLICATION = "tunneltech.asgi.application"
STATICFILES_DIRS = [BASE_DIR.joinpath(Path("./frontend/static/frontend"))]
STATIC_URL = "/static/"

WINDTUNNEL_GRPC_HOST = "gnitry.com:7735"
WINDTUNNEL_READ_MULTI_SCHEDULE = timedelta(seconds=1)
