# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.db.models.query import QuerySet
from rest_framework.authentication import BasicAuthentication
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from djangocli import exceptions
from djangocli.utils.drf import filter, mixins
from djangocli.utils.drf.auth import CsrfExemptSessionAuthentication


class DjangoCliGenericViewSetHandler(mixins.ViewSetExceptionHandlerMixin, mixins.ViewSetResponseMixin, GenericViewSet):
    # 设置默认分页器
    pagination_class = filter.DjangoCliPageNumberPagination

    # 认证
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)


class DjangoCliModelViewSet(DjangoCliGenericViewSetHandler, ModelViewSet):
    model = None

    def get_filter_queryset(self) -> QuerySet:
        """获取筛选后的queryset"""
        return self.filter_queryset(self.get_queryset())


def django_cli_exception_handler(exc: exceptions.DjangoCliBaseException, context):
    """统一异常返回"""

    def build_response(code=0, message="", data=None, errors=None) -> JsonResponse:
        data = data or {}
        return JsonResponse(
            {
                "result": False,
                "code": code,
                "data": data,
                "message": message,
            }
        )

    return build_response(code=exc.code, message=exc.message, data=exc.data, errors=exc.errors)
