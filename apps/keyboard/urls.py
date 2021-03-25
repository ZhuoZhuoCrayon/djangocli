# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=True)


urlpatterns = [url(r"", include(router.urls))]
