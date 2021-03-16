# -*- coding: utf-8 -*-


def get_redis_url(host: str, port: int, password: str = None, db_index: int = 0) -> str:
    if not password:
        return "redis://{host}:{port}/{db_index}".format(host=host, port=port, db_index=db_index)
    else:
        return "redis://:{password}@{host}:{port}/{db_index}".format(
            password=password, host=host, port=port, db_index=db_index
        )
