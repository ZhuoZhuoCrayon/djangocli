# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r"v1/example/", include("apps.example.urls")),
]
