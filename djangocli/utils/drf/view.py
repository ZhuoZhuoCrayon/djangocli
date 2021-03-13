# -*- coding: utf-8 -*-
from rest_framework.authentication import BasicAuthentication
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from djangocli.utils.drf import filter
from djangocli.utils.drf.auth import CsrfExemptSessionAuthentication


class DjangoCliGenericViewSet(GenericViewSet):
    # 设置默认分页器
    pagination_class = filter.DjangoCliPageNumberPagination

    # 认证
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)


class DjangoCliModelViewSet(DjangoCliGenericViewSet, ModelViewSet):
    model = None
