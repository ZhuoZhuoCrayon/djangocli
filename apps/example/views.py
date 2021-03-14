from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from apps.example import models, serializers
from djangocli.utils.drf.view import DjangoCliModelViewSet

# Create your views here.


class ExampleBookViews(DjangoCliModelViewSet):
    model = models.Book
    serializer_class = serializers.ExampleBookModelSerializer

    def get_queryset(self):
        return self.model.objects.all()

    @swagger_auto_schema(
        operation_summary="查询书籍",
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
