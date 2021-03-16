# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from djangocli.utils.drf import filter
from apps.example.tests import mock_data
from apps.example import models, constants


class ExampleBookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class ExampleAuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class ExamplePublisherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = "__all__"


class ExampleBookSearchRequestSerializer(filter.PageSerializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_BOOK_SEARCH.request_data}


class ExampleBookSearchResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_BOOK_SEARCH.response_data}


class ExampleCommonExceptionRequestSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_COMMON_EXCEPTION.request_data}


class ExampleCommonExceptionResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_COMMON_EXCEPTION.response_data}


class ExampleCommonUnExceptionRequestSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_COMMON_UN_EXCEPTION.request_data}


class ExampleCommonUnExceptionResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_COMMON_UN_EXCEPTION.response_data}


class ExampleCommonValidateExceptionRequestSerializer(filter.PageSerializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_COMMON_VALIDATE_EXCEPTION.request_data}


class ExampleCommonValidateExceptionResponseSerializer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_EXAMPLE_COMMON_VALIDATE_EXCEPTION.response_data}


class CommonCeleryDelayRequestSer(serializers.Serializer):

    left_val = serializers.FloatField(required=True, help_text=_("左操作数"))
    right_val = serializers.FloatField(required=True, help_text=_("右操作数"))
    operate = serializers.ChoiceField(
        required=False, default=constants.MathOp.ADD, choices=constants.OP_CHOICES, help_text=_("数值操作")
    )

    class Meta:
        swagger_schema_fields = {"example": mock_data.API_COMMON_CELERY_DELAY.request_data}


class CommonCeleryDelayResponseSer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_COMMON_CELERY_DELAY.response_data}


class CommonBatchCeleryResultsRequestSer(serializers.Serializer):

    task_ids = serializers.ListField(
        required=True, child=serializers.CharField(help_text=_("celery task id")), min_length=1
    )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs["task_ids"] = list(set(attrs["task_ids"]))
        return attrs

    class Meta:
        swagger_schema_fields = {"example": mock_data.API_COMMON_CELERY_DELAY.request_data}


class CommonBatchCeleryResultsResponseSer(serializers.Serializer):
    class Meta:
        swagger_schema_fields = {"example": mock_data.API_COMMON_CELERY_DELAY.response_data}
