# -*- coding: utf-8 -*-
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
