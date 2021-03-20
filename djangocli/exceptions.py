# -*- coding: utf-8 -*-
from typing import Any, Dict

from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, status


class ModuleErrorCode:
    SYSTEM = "DC:-1"
    DJANGO_CLI = "DC:00"
    REST = "DC:01"
    DJANGO_HTTP = "DC:02"


class DjangoCliBaseException(Exception):
    MODULE_CODE = ModuleErrorCode.DJANGO_CLI
    FUNCTION_ERROR_CODE = str(status.HTTP_500_INTERNAL_SERVER_ERROR)

    MESSAGE_TEMPLATE = None
    MESSAGE = _("系统异常")

    def __init__(self, context: Dict[str, Any] = None, **kwargs):

        context = context or {}

        # 优先取传入错误码 & 报错信息
        self.code = kwargs.get("code") or f"{self.MODULE_CODE}-{self.FUNCTION_ERROR_CODE}"

        if "message" in kwargs:
            self.message = kwargs["message"]
        else:
            self.message = self.MESSAGE_TEMPLATE.format(**context) if self.MESSAGE_TEMPLATE else self.MESSAGE

        self.errors = kwargs.get("errors")
        self.data = kwargs.get("data")

    def __str__(self):
        return f"{self.code}: {self.message}"


class DjangoCliRestApiException(DjangoCliBaseException):
    MODULE_CODE = ModuleErrorCode.REST

    def __init__(self, rest_exc: exceptions.APIException):

        code = f"{self.MODULE_CODE}-{rest_exc.status_code}"
        message = f"{rest_exc.default_code} (Details: {rest_exc.default_detail})"
        data = rest_exc.detail

        super().__init__(code=code, message=message, data=data)


class DjangoCliSystemBaseException(DjangoCliBaseException):
    MODULE_CODE = ModuleErrorCode.SYSTEM
    MESSAGE_TEMPLATE = _("别慌，系统暂时出了点小问题，请联系管理员排查（{msg}）")

    def __init__(self, exc: Exception, **kwargs):
        code = f"{self.MODULE_CODE}-{kwargs.get('status_code') or status.HTTP_500_INTERNAL_SERVER_ERROR}"
        # TODO 展示__class__信息可能会引起恶意攻击
        super().__init__(context={"msg": f"{str(exc.__class__)}({exc})"}, code=code)


class DjangoCliHttp404Exception(DjangoCliSystemBaseException):
    MODULE_CODE = ModuleErrorCode.DJANGO_HTTP
    MESSAGE_TEMPLATE = _("未找到资源 ({msg})")

    def __init__(self, http404: Http404):
        super().__init__(exc=http404, status_code=status.HTTP_404_NOT_FOUND)
