# -*- coding: utf-8 -*-

from djangocli.utils.drf import base


class ApiMockData:
    def __init__(self, request_data, response_data, **kwargs):
        self.request_data = request_data
        self.response_data = response_data

        # 约定错误的请求写全返回体，成功请求需要进行补全
        if "result" not in response_data:
            self.response_data = base.build_response_dict(
                result=True, code=base.SUCCESS_CODE, data=response_data, message=base.SUCCESS_MSG
            )
