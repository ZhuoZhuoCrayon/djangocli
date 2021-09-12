# -*- coding: utf-8 -*-

from djangocli.conf.djangocli_settings import *  # noqa

DC_MYSQL_NAME = get_env("DC_MYSQL_NAME", APP_NAME)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": DC_MYSQL_NAME,
        "USER": get_env("DC_MYSQL_USER", "root"),
        "PASSWORD": get_env("DC_MYSQL_PASSWORD", ""),
        "HOST": get_env("DC_MYSQL_HOST", "localhost"),
        "PORT": get_env("DC_MYSQL_PORT", 3306),
        "TEST": {
            "NAME": f"{DC_MYSQL_NAME}_test",
            "CHARSET": "utf8mb4",
            "COLLATION": "utf8mb4_unicode_ci",
        },
    }
}

INSTALLED_APPS.extend(["apps.example"])
