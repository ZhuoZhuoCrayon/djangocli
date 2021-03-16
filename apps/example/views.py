from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.utils.translation import ugettext_lazy as _

from apps.example import models, serializers, exceptions, handler as apps_example_handler
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

        return Response({"query_data": self.query_data, "list": self.get_queryset().values()})


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

    @swagger_auto_schema(
        operation_summary=_("序列化器校验异常"),
        tags=["common"],
        request_body=serializers.ExampleCommonValidateExceptionRequestSerializer(),
        responses={status.HTTP_200_OK: serializers.ExampleCommonValidateExceptionResponseSerializer()},
    )
    @action(
        methods=["POST"], detail=False, serializer_class=serializers.ExampleCommonValidateExceptionRequestSerializer
    )
    def validate_exception(self, request, *args, **kwargs):
        return Response({"query_data": self.query_data})

    @swagger_auto_schema(
        operation_summary=_("Celery异步任务"),
        tags=["common"],
        request_body=serializers.CommonCeleryDelayRequestSer(),
        responses={status.HTTP_200_OK: serializers.CommonCeleryDelayResponseSer()},
    )
    @action(methods=["POST"], detail=False, serializer_class=serializers.CommonCeleryDelayRequestSer)
    def celery_delay(self, request, *args, **kwargs):
        return Response(
            {
                "task_id": apps_example_handler.CommonHandler.celery_delay(
                    left_val=self.query_data["left_val"],
                    right_val=self.query_data["right_val"],
                    operate=self.query_data["operate"],
                )
            }
        )

    @swagger_auto_schema(
        operation_summary=_("获取Celery执行结果"),
        tags=["common"],
        request_body=serializers.CommonBatchCeleryResultsRequestSer(),
        responses={status.HTTP_200_OK: serializers.CommonBatchCeleryResultsResponseSer()},
    )
    @action(methods=["POST"], detail=False, serializer_class=serializers.CommonBatchCeleryResultsRequestSer)
    def batch_celery_results(self, request, *args, **kwargs):
        return Response(apps_example_handler.CommonHandler.batch_celery_results(task_ids=self.query_data["task_ids"]))
