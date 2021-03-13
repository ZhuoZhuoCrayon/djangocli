# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.example import models


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
