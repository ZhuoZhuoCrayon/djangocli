# -*- coding: utf-8 -*-
import json
from typing import Any, Dict

from rest_framework import status
from rest_framework.test import APIClient

from djangocli.utils.drf import base

# DEFAULT_CONTENT_TYPE & DEFAULT_FORMAT 不能同时设置
DEFAULT_CONTENT_TYPE = None  # or "application/json"

DEFAULT_FORMAT = "json"


class ApiMockData:
    def __init__(self, request_data, response_data, **kwargs):
        self.request_data = request_data
        self.response_data = response_data

        # 约定错误的请求写全返回体，成功请求需要进行补全
        if "result" not in response_data:
            self.response_data = base.build_response_dict(
                result=True, code=base.SUCCESS_CODE, data=response_data, message=base.SUCCESS_MSG
            )


class DjangoCliAPIClient(APIClient):
    @staticmethod
    def assert_response(response) -> Dict[str, Any]:
        assert response.status_code == status.HTTP_200_OK
        return json.loads(response.content)

    def get(self, path, data=None, follow=False, **extra):
        response = super().get(path=path, data=data, follow=float, **extra)
        return self.assert_response(response)

    def post(self, path, data=None, format=DEFAULT_FORMAT, content_type=DEFAULT_CONTENT_TYPE, follow=False, **extra):
        response = super().post(
            path=path, data=data, format=format, content_type=DEFAULT_CONTENT_TYPE, follow=follow, **extra
        )
        return self.assert_response(response)

    def put(self, path, data=None, format=DEFAULT_FORMAT, content_type=DEFAULT_CONTENT_TYPE, follow=False, **extra):
        response = super().put(
            path=path, data=data, format=format, content_type=DEFAULT_CONTENT_TYPE, follow=follow, **extra
        )
        return self.assert_response(response)

    def delete(self, path, data=None, format=DEFAULT_FORMAT, content_type=DEFAULT_CONTENT_TYPE, follow=False, **extra):
        response = super().delete(
            path=path, data=data, format=format, content_type=content_type, follow=follow, **extra
        )
        return self.assert_response(response)
