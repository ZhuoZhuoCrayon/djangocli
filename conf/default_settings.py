# -*- coding: utf-8 -*-
from djangocli.conf.djangocli_settings import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": environ.DC_MYSQL_NAME,
        "USER": environ.DC_MYSQL_USER,
        "PASSWORD": environ.DC_MYSQL_PASSWORD,
        "HOST": environ.DC_MYSQL_HOST,
        "PORT": environ.DC_MYSQL_PORT,
        "TEST": {
            "NAME": f"{environ.DC_MYSQL_NAME}_test",
            "CHARSET": "utf8mb4",
            "COLLATION": "utf8mb4_unicode_ci",
        },
    }
}

INSTALLED_APPS.extend(["apps.example"])
