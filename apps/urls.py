# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    # 屏蔽不使用的app
    # url(r"v1/example/", include("apps.example.urls")),
    url(r"v1/keyboard/", include("apps.keyboard.urls")),
]
