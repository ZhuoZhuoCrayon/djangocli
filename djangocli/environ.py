# -*- coding: utf-8 -*-

from multiprocessing import cpu_count

from djangocli.constants import EnvType
from djangocli.core.env import get_env

# APP INFO
APP_NAME = get_env(key="APP_NAME", default="django-cli", _type=str)
APP_VERSION = get_env(key="APP_VERSION", default="0.0.0", _type=str)
SECRET_KEY = get_env(key="SECRET_KEY", default="", _type=str)

# 环境配置
ENV = get_env(key="DC_ENV", default=EnvType.LOCAL, _type=str)
# 是否通过 environ.sh 的方式注入环境变量
IS_INJECT_ENV = get_env(key="IS_INJECT_ENV", default=True, _type=bool)
DC_KEEP_ENVFILE = get_env(key="DC_KEEP_ENVFILE", default=False, _type=bool)
DJANGO_SETTINGS_MODULE = get_env(key="DJANGO_SETTINGS_MODULE", default="settings", _type=str)
DC_DEFAULT_CONF_MODULE = get_env(key="DC_DEFAULT_CONF_MODULE", default="conf.default_settings", _type=str)

# MYSQL
DC_MYSQL_HOST = get_env(key="DC_MYSQL_HOST", default="localhost", _type=str)
DC_MYSQL_PORT = get_env(key="DC_MYSQL_PORT", default=3306, _type=int)
DC_MYSQL_USER = get_env(key="DC_MYSQL_USER", default="root", _type=str)
DC_MYSQL_NAME = get_env(key="DC_MYSQL_NAME", default=APP_NAME, _type=str)
DC_MYSQL_PASSWORD = get_env(key="DC_MYSQL_PASSWORD", default="", _type=str)

# REDIS
DC_REDIS_HOST = get_env(key="DC_REDIS_HOST", default="localhost", _type=str)
DC_REDIS_PORT = get_env(key="DC_REDIS_PORT", default=6379, _type=int)
DC_REDIS_PASSWORD = get_env(key="DC_REDIS_PASSWORD", default="", _type=str)


DC_SUPER_USER_NAME = get_env(key="DC_SUPER_USER_NAME", default="admin", _type=str)
DC_SUPER_PASSWORD = get_env(key="DC_SUPER_PASSWORD", default="", _type=str)

# 最大并发数
MAXIMUM_CONCURRENT_NUMBER = get_env(key="MAXIMUM_CONCURRENT_NUMBER", default=cpu_count(), _type=int)

try:
    from environ import *  # noqa
except ImportError:
    pass
