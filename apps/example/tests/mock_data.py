# -*- coding: utf-8 -*-
from rest_framework import status

from apps.example import constants, exceptions
from djangocli import exceptions as dc_exceptions
from djangocli.utils.unittest.base import ApiMockData
from djangocli.utils.unittest.testcase import MockSuperUserMixin

API_BOOK_SEARCH = ApiMockData(
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

API_COMMON_EXCEPTION = ApiMockData(
    request_data={},
    response_data={
        "result": False,
        "code": f"{exceptions.ExampleAppBaseException.MODULE_CODE}-"
        f"{exceptions.CommonExceptionException.FUNCTION_ERROR_CODE}",
        "data": {},
        "message": exceptions.CommonExceptionException.MESSAGE_TEMPLATE.format(user=MockSuperUserMixin.SUPERUSER_NAME),
    },
)

API_COMMON_UN_EXCEPTION = ApiMockData(
    request_data={},
    response_data={
        "result": False,
        "code": f"{dc_exceptions.ModuleErrorCode.SYSTEM}-"
        f"{dc_exceptions.DjangoCliSystemBaseException.FUNCTION_ERROR_CODE}",
        "data": {},
        "message": "别慌，系统暂时出了点小问题，请联系管理员排查（<class 'TypeError'>('User' object is not subscriptable)）",
    },
)


API_COMMON_VALIDATE_EXCEPTION = ApiMockData(
    request_data={},
    response_data={
        "result": False,
        "code": f"{dc_exceptions.ModuleErrorCode.REST}-{status.HTTP_400_BAD_REQUEST}",
        "data": {"page": ["该字段是必填项。"], "page_size": ["该字段是必填项。"]},
        "message": "invalid (Details: Invalid input.)",
    },
)


API_COMMON_CELERY_DELAY = ApiMockData(
    request_data={"left_val": 1, "right_val": 2, "operate": constants.MathOp.ADD},
    response_data={"task_id": "377ef8e1-395b-4a94-9ee5-d084e4b20567"},
)

API_BATCH_CELERY_RESULTS_DELAY = ApiMockData(
    request_data={"task_ids": ["bafa6f6a-2fba-4fad-9d34-7dc167e8768c", "470a9e20-2abe-413a-89e7-3f18e9351f28"]},
    response_data=[
        {
            "date_done": "2021-03-20T15:51:35.011043",
            "task_id": "470a9e20-2abe-413a-89e7-3f18e9351f28",
            "result": 10000000,
            "status": "SUCCESS",
            "state": "SUCCESS",
        },
        {
            "date_done": "2021-03-20T15:46:03.580606",
            "task_id": "bafa6f6a-2fba-4fad-9d34-7dc167e8768c",
            "result": 3,
            "status": "SUCCESS",
            "state": "SUCCESS",
        },
    ],
)
