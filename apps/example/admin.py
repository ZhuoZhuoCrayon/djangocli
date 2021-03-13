from django.contrib import admin

from apps.example import models

# Register your models here.


@admin.register(models.Book)
class ExampleBookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Book._meta.get_fields()]
    search_fields = ["name", "ISBN", "package_type"]
    list_filter = ["name", "ISBN", "package_type"]


@admin.register(models.Author)
class ExampleAuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Author._meta.get_fields()]
    search_fields = ["first_name", "last_name"]
    list_filter = ["first_name", "last_name"]


@admin.register(models.Publisher)
class ExamplePublisherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Publisher._meta.get_fields()]
    search_fields = ["name", "city", "country"]
    list_filter = ["name", "city", "country"]
