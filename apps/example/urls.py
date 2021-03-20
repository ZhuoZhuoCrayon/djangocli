# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apps.example import views

router = routers.DefaultRouter(trailing_slash=True)

router.register(prefix=r"book", viewset=views.ExampleBookViews, basename="book")
router.register(prefix=r"author", viewset=views.ExampleAuthorViews, basename="author")
router.register(prefix=r"publisher", viewset=views.ExamplePublisherView, basename="publisher")
router.register(prefix=r"common", viewset=views.ExampleCommonViews, basename="common")


urlpatterns = [url(r"", include(router.urls))]
