# -*- coding: utf-8 -*-
from typing import Union, Dict, Any, List

SUCCESS_CODE = "0"

SUCCESS_MSG = "success"


def build_response_dict(result: bool, code: str, message: str, data=Union[Dict[str, Any], List[Any]]) -> Dict[str, Any]:
    return {"result": result, "code": code, "data": data, "message": message}
