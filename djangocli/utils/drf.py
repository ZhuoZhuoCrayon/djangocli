# -*- coding: utf-8 -*-
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class DjangoCliGenericViewSet(GenericViewSet):
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)


class DjangoCliModelViewSet(DjangoCliGenericViewSet, ModelViewSet):
    model = None
