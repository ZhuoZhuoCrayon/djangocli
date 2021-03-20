# -*- coding: utf-8 -*-

from djangocli.conf.default_settings import *  # noqa
from djangocli.utils import string

INSTALLED_APPS.extend(
    [
        "rest_framework",
        "drf_yasg",  # swagger's support
    ]
)

REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    # "DEFAULT_AUTHENTICATION_CLASSES": (
    #     "rest_framework.authentication.BasicAuthentication",
    #     "rest_framework.authentication.SessionAuthentication",
    #     'rest_framework.authentication.TokenAuthentication',
    # ),
    # "DEFAULT_RENDERER_CLASSES": (
    #     # 自定义渲染器
    #     # "apps.utils.drf.CustomJsonRender",
    #     "rest_framework.renderers.JSONRenderer",
    # ),
    "EXCEPTION_HANDLER": "djangocli.utils.drf.view.django_cli_exception_handler",
    # djangocli.utils.drf.view.DjangoCliGenericViewSet 中亦可指定分页器
    "DEFAULT_PAGINATION_CLASS": "djangocli.utils.drf.filter.DjangoCliPageNumberPagination",
}


ALLOWED_HOSTS = ["*"]

# REDIS
DEFAULT_REDIS_PORT = 6379

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": string.get_redis_url(
            host=os.getenv("DC_REDIS_HOST", "localhost"), port=os.getenv("DC_REDIS_PORT", 6379), db_index=0
        ),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.getenv("DC_REDIS_PASSWORD", ""),
            # 最大连接数量
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        },
        "KEY_FUNCTION": "djangocli.utils.redis.django_cache_key_maker",
    }
}


# Celery's config

CELERY_BROKER_URL = string.get_redis_url(
    password=os.getenv("DC_REDIS_PASSWORD", ""),
    host=os.getenv("DC_REDIS_HOST", "localhost"),
    port=os.getenv("DC_REDIS_PORT", 6379),
    db_index=1,
)

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_TASK_SERIALIZER = "json"
