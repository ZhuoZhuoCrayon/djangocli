# -*- coding: utf-8 -*-
from typing import Dict, Any, List

from celery.result import AsyncResult

from apps.example import task as apps_example_task


class CommonHandler:
    @staticmethod
    def celery_delay(left_val: float, right_val: float, operate: str) -> str:
        return getattr(apps_example_task, operate).delay(left_val, right_val).task_id

    @staticmethod
    def batch_celery_results(task_ids: str) -> List[Dict[str, Any]]:
        celery_results = []
        for task_id in task_ids:
            task = AsyncResult(task_id)
            celery_results.append(
                {
                    "date_done": task.date_done,
                    "task_id": task.task_id,
                    "result": task.result,
                    "status": task.status,
                    "state": task.state,
                }
            )
        return celery_results
