# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from apps.exceptions import AppModuleErrorCode
from djangocli.exceptions import DjangoCliBaseException


class ExampleAppBaseException(DjangoCliBaseException):
    MODULE_CODE = AppModuleErrorCode.EXAMPLE


class ExampleCommonExceptionException(ExampleAppBaseException):
    FUNCTION_ERROR_CODE = "00"
    MESSAGE_TEMPLATE = _("用户[{user}]主动抛出了一个异常")
