"""djangocli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from rest_framework import permissions
from django.contrib import admin
from django.conf.urls import include, url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="DjangoCli API",
        default_version="v1",
        description="基于DRF的Django轻量级Web开发脚手架",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(url="https://github.com/ZhuoZhuoCrayon", email="873217631@qq.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_format_view = schema_view.without_ui(cache_timeout=0)
# 登录豁免
setattr(swagger_format_view, "login_exempt", True)

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    # apps' api
    url(r"^api/", include("apps.urls")),
    # swagger
    url(r"^swagger(?P<format>\.json|\.yaml)$", swagger_format_view, name="schema-json"),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
