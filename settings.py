# -*- coding: utf-8 -*-

import os
from pathlib import Path


class EnvType:
    DEV = "dev"
    PROD = "prod"
    STAG = "stag"


ENV = os.getenv("DJANGO_CLI_ENV", EnvType.DEV)

DJANGO_CONF_MODULE = "conf.{env}".format(env=ENV)

try:
    _module = __import__(DJANGO_CONF_MODULE, globals(), locals(), ["*"])
except ImportError as error:
    raise ImportError(f"Could not import config {DJANGO_CONF_MODULE} (Is it on sys.path?): {error}")

for _setting in dir(_module):
    if _setting == _setting.upper():
        locals()[_setting] = getattr(_module, _setting)

# 需要覆盖全局的变量
BASE_DIR = Path(__file__).resolve().parent
