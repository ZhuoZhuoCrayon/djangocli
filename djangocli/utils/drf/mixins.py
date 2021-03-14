# -*- coding: utf-8 -*-
import traceback

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from djangocli import exceptions


class ViewSetExceptionHandlerMixin:
    """统一异常处理"""

    def dispatch(self, request, *args, **kwargs):
        """
        `.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        """
        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?

        try:
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)

        except (exceptions.DjangoCliBaseException, APIException, Http404) as exc:
            response = self.handle_exception(exc)
        except Exception as exc:
            # TODO 打印预期外异常堆栈，并且应该记录日志
            # logging自带记录堆栈的功能，具体 -> https://stackoverflow.com/questions/1508467/log-exception-with-traceback
            # logging.exception("xxxx")
            traceback.print_exc()
            response = self.handle_exception(exc)

        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response

    def handle_exception(self, exc):
        """将异常格式化为统一格式"""
        if isinstance(exc, exceptions.DjangoCliBaseException):
            return super().handle_exception(exc)

        if isinstance(exc, APIException):
            exc = exceptions.DjangoCliRestApiException(exc)
        elif isinstance(exc, Http404):
            exc = exceptions.DjangoCliHttp404Exception(exc)
        else:
            exc = exceptions.DjangoCliSystemBaseException(exc)

        return super().handle_exception(exc)


class ViewSetResponseMixin:
    """统一返回格式"""

    def finalize_response(self, request, response, *args, **kwargs):
        """统一接口返回格式"""
        if isinstance(response, Response):
            response.data = {
                "result": not response.exception,
                "data": response.data or {},
                "code": getattr(response, "code", exceptions.SUCCESS_CODE),
                "message": getattr(response, "message", "") if response.exception else "success",
            }
            response.status_code = status.HTTP_200_OK

        return super().finalize_response(request, response, *args, **kwargs)
