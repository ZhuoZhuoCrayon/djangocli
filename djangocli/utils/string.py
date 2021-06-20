# -*- coding: utf-8 -*-

from typing import Optional


def get_redis_url(host: str, port: int, password: Optional[str] = None, db_index: int = 0) -> str:
    if not password:
        return "redis://{host}:{port}/{db_index}".format(host=host, port=port, db_index=db_index)
    else:
        return "redis://:{password}@{host}:{port}/{db_index}".format(
            password=password, host=host, port=port, db_index=db_index
        )


def str2bool(string: Optional[str], strict: bool = True) -> bool:
    """
    字符串转布尔值
    对于bool(str) 仅在len(str) == 0 or str is None 的情况下为False，为了适配bool("False") 等环境变量取值情况，定义该函数
    参考：https://stackoverflow.com/questions/21732123/convert-true-false-value-read-from-file-to-boolean
    :param string:
    :param strict: 严格校验，非False / True 时抛出异常，用于环境变量的转换
    :return:
    """
    if string == "False":
        return False
    if string == "True":
        return True

    if strict:
        raise ValueError(f"{string} can not convert to bool")
    return bool(None)
