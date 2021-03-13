from djangocli.utils.drf import DjangoCliModelViewSet
from apps.example import models, serializers

# Create your views here.


class ExampleBookViews(DjangoCliModelViewSet):
    model = models.Book
    serializer_class = serializers.ExampleBookModelSerializer

    def get_queryset(self):
        return self.model.objects.all()


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
