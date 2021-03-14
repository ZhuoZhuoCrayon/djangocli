# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet
from rest_framework.authentication import BasicAuthentication
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from djangocli.utils.drf import filter
from djangocli.utils.drf.auth import CsrfExemptSessionAuthentication


class DjangoCliGenericViewSet(GenericViewSet):
    # 设置默认分页器
    pagination_class = filter.DjangoCliPageNumberPagination

    # 认证
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)

    def get_filter_queryset(self) -> QuerySet:
        """获取筛选后的queryset"""
        return self.filter_queryset(self.get_queryset())


class DjangoCliModelViewSet(DjangoCliGenericViewSet, ModelViewSet):
    model = None
