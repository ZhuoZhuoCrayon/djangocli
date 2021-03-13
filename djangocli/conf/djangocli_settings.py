# -*- coding: utf-8 -*-

from djangocli.conf.default_settings import *  # noqa

INSTALLED_APPS.extend(["rest_framework"])

REST_FRAMEWORK = {
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    "DEFAULT_RENDERER_CLASSES": (
        # 自定义渲染器
        # "apps.utils.drf.CustomJsonRender",
        "rest_framework.renderers.JSONRenderer",
    ),
    # "EXCEPTION_HANDLER": "apps.utils.drf.custom_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "apps.utils.drf.PageNumberPagination",
}
