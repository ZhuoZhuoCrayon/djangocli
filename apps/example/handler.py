# -*- coding: utf-8 -*-
from typing import Any, Dict, List

from celery.result import AsyncResult

from apps.example import task


class CommonHandler:
    @staticmethod
    def celery_delay(left_val: float, right_val: float, operate: str) -> str:
        return getattr(task, operate).delay(left_val, right_val).task_id

    @staticmethod
    def batch_celery_results(task_ids: str) -> List[Dict[str, Any]]:
        celery_results = []
        for task_id in task_ids:
            task_info_obj = AsyncResult(task_id)
            celery_results.append(
                {
                    "date_done": task_info_obj.date_done,
                    "task_id": task_info_obj.task_id,
                    "result": task_info_obj.result,
                    "status": task_info_obj.status,
                    "state": task_info_obj.state,
                }
            )
        return celery_results
