# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageSerializer(serializers.Serializer):
    page = serializers.IntegerField(help_text=_("页数"))
    page_size = serializers.IntegerField(help_text=_("每页数量"))


class OrderingSerializer(serializers.Serializer):
    ordering = serializers.CharField(help_text=_("排序字段，`-`表示逆序，多个排序字段以`,`分隔"), required=False)


class SearchSerializer(serializers.Serializer):
    search = serializers.CharField(help_text=_("模糊查找，多个查找关键字以`,`分隔"), required=False)


class PostFilterSerializer(serializers.Serializer):
    class ConditionSerializer(serializers.Serializer):
        fields = serializers.ListField(help_text=_("查询目标字段列表"), child=serializers.CharField(), min_length=1)
        operator = serializers.CharField(help_text=_("查询类型，可选：`in` `contains` `range` `gt(lt)` `gte(lte)..."))
        values = serializers.ListField(help_text=_("查询目标值列表"), min_length=1)

    conditions = serializers.ListField(help_text=_("查询条件"), child=ConditionSerializer(), required=False, default=[])


class DjangoCliPageNumberPagination(PageNumberPagination):
    # 用于最大页数据量
    max_page_size = 500

    page_size_query_param = "page_size"
    page_query_param = "page"

    # 设置分页默认参数
    page_size = 10

    def get_page_size(self, request):
        """分页支持POST方法"""
        if request.method in ["DELETE", "GET"]:
            return super().get_page_size(request)

        # 设置 _mutable = True使得query_param可注入data中的page_size & page
        request.query_params._mutable = True
        if request.query_params.get(self.page_size_query_param) is None:
            request.query_params[self.page_query_param] = request.data.get(self.page_query_param)
            request.query_params[self.page_size_query_param] = request.data.get(self.page_size_query_param)
        request.query_params._mutable = False

        # self.paginate_queryset() 会从query_param读出分页参数
        return super().get_page_size(request)

    def get_paginated_response(self, data):
        return Response({"count": self.page.paginator.count, "list": data})
