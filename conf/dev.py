# -*- coding: utf-8 -*-

from djangocli.conf.default_settings import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": APP_NAME,
        "USER": os.getenv("DC_MYSQL_NAME", "root"),
        "PASSWORD": os.getenv("DC_MYSQL_PASSWORD", ""),
        "HOST": os.getenv("DC_MYSQL_HOST", "localhost"),
        "PORT": os.getenv("DC_MYSQL_PORT", 3306),
        "TEST": {
            "NAME": f"{APP_NAME}_test",
            "CHARSET": "utf8mb4",
            "COLLATION": "utf8mb4_unicode_ci",
        },
    }
}
