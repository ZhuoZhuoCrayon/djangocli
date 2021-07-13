# -*- coding: utf-8 -*-
import sys
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import cpu_count, get_context
from typing import Any, Callable, Dict, List

from django.conf import settings


def batch_call(
    func: Callable,
    params_list: List[Dict[str, Any]],
    handle_func_result: Callable = lambda x: x,
    expand_result: bool = False,
) -> List:
    """
    多线程处理函数
    :param func: 逻辑函数
    :param params_list: 参数列表
    :param handle_func_result: 处理逻辑函数返回结果
    :param expand_result: 是否通过expand整合返回结果
    :return:
    """

    func_result_list = []
    with ThreadPoolExecutor(max_workers=settings.CONCURRENT_NUMBER) as ex:
        tasks = [ex.submit(func, **params) for params in params_list]
    for future in as_completed(tasks):
        if expand_result:
            func_result_list.extend(handle_func_result(future.result()))
        else:
            func_result_list.append(handle_func_result(future.result()))
    return func_result_list


def batch_call_multi_proc(
    func: Callable,
    params_list: List[Dict[str, Any]],
    handle_func_result: Callable = lambda x: x,
    expand_result: bool = False,
) -> List:
    """
    多进程处理函数
    TODO 暂无法处理MySQL多进程链接
    :param func: 逻辑函数
    :param params_list: 参数列表
    :param handle_func_result: 处理逻辑函数返回结果
    :param expand_result: 是否通过expand整合返回结果
    :return:
    """
    if sys.platform in ["win32", "cygwim", "msys"]:
        return batch_call(func, params_list, handle_func_result, expand_result)
    else:
        ctx = get_context("fork")

    func_result_list = []

    pool = ctx.Pool(processes=cpu_count())
    futures = [pool.apply_async(func=func, kwds=params) for params in params_list]

    pool.close()
    pool.join()

    # 取值
    for future in futures:
        if expand_result:
            func_result_list.extend(handle_func_result(future.get()))
        else:
            func_result_list.append(handle_func_result(future.get()))
    return func_result_list
