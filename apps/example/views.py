from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.utils.translation import ugettext_lazy as _

from apps.example import models, serializers, exceptions
from djangocli.utils.drf.view import DjangoCliModelViewSet, DjangoCliGenericViewSetHandler

# Create your views here.


class ExampleBookViews(DjangoCliModelViewSet):
    model = models.Book
    serializer_class = serializers.ExampleBookModelSerializer

    def get_queryset(self):
        return self.model.objects.all()

    @swagger_auto_schema(
        operation_summary=_("查询书籍"),
        tags=["book"],
        request_body=serializers.ExampleBookSearchRequestSerializer(),
        responses={status.HTTP_200_OK: serializers.ExampleBookSearchResponseSerializer()},
    )
    @action(methods=["POST"], detail=False, serializer_class=serializers.ExampleBookSearchRequestSerializer)
    def search(self, request, *args, **kwargs):
        return Response({})


class ExampleAuthorViews(DjangoCliModelViewSet):
    model = models.Author
    serializer_class = serializers.ExampleAuthorModelSerializer

    def get_queryset(self):
        return self.model.objects.all()


class ExamplePublisherView(DjangoCliModelViewSet):
    model = models.Publisher
    serializer_class = serializers.ExamplePublisherModelSerializer

    def get_queryset(self):
        return self.model.objects.all()


class ExampleCommonViews(DjangoCliGenericViewSetHandler):
    @swagger_auto_schema(
        operation_summary=_("主动抛出预期异常"),
        tags=["common"],
        request_body=serializers.ExampleCommonExceptionRequestSerializer(),
        responses={status.HTTP_200_OK: serializers.ExampleCommonExceptionResponseSerializer()},
    )
    @action(methods=["POST"], detail=False, serializer_class=serializers.ExampleCommonExceptionRequestSerializer)
    def expected_exception(self, request, *args, **kwargs):
        raise exceptions.ExampleCommonExceptionException(context={"user": request.user})

    @swagger_auto_schema(
        operation_summary=_("系统错误（非预期）异常"),
        tags=["common"],
        request_body=serializers.ExampleCommonUnExceptionRequestSerializer(),
        responses={status.HTTP_200_OK: serializers.ExampleCommonUnExceptionResponseSerializer()},
    )
    @action(methods=["POST"], detail=False, serializer_class=serializers.ExampleCommonUnExceptionRequestSerializer)
    def unexpected_exception(self, request, *args, **kwargs):
        return Response({"name": request.user["no_name"]})
