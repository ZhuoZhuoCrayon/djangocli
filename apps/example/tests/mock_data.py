# -*- coding: utf-8 -*-
from rest_framework import status

from apps.example import exceptions as apps_example_exceptions
from djangocli import exceptions as dc_exceptions
from djangocli.utils.unittest.base import ApiMockData

API_EXAMPLE_BOOK_SEARCH = ApiMockData(
    request_data={"page": 1, "page_size": 10},
    response_data={
        "count": 1,
        "list": [
            {
                "id": 1,
                "name": "Redis设计与实现",
                "ISBN": "9787111464747",
                "publication_date": "2021-03-13",
                "package_type": 1,
                "publisher_id": 0,
                "author_ids": "[1, 2, 3, 4]",
                "created_at": "2021-03-13 20:36:09",
                "updated_at": "2021-03-13 20:41:20",
            }
        ],
    },
)

API_EXAMPLE_COMMON_EXCEPTION = ApiMockData(
    request_data={},
    response_data={
        "result": False,
        "code": f"{apps_example_exceptions.ExampleAppBaseException.MODULE_CODE}-"
        f"{apps_example_exceptions.ExampleCommonExceptionException.FUNCTION_ERROR_CODE}",
        "data": {},
        "message": apps_example_exceptions.ExampleCommonExceptionException.MESSAGE_TEMPLATE,
    },
)

API_EXAMPLE_COMMON_UN_EXCEPTION = ApiMockData(
    request_data={},
    response_data={
        "result": False,
        "code": f"{dc_exceptions.ModuleErrorCode.SYSTEM}-"
        f"{dc_exceptions.DjangoCliSystemBaseException.FUNCTION_ERROR_CODE}",
        "data": {},
        "message": "别慌，系统暂时出了点小问题，请联系管理员排查（<class 'TypeError'>('User' object is not subscriptable)）",
    },
)


API_EXAMPLE_COMMON_VALIDATE_EXCEPTION = ApiMockData(
    request_data={},
    response_data={
        "result": False,
        "code": f"{dc_exceptions.ModuleErrorCode.REST}-{status.HTTP_400_BAD_REQUEST}",
        "data": {"page": ["该字段是必填项。"], "page_size": ["该字段是必填项。"]},
        "message": "invalid (Details: Invalid input.)",
    },
)
