# -*- coding: utf-8 -*-
from rest_framework import serializers

from djangocli.utils.drf import filter
from apps.example import models
from apps.example.tests import mock_data


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
