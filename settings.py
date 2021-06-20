# -*- coding: utf-8 -*-

import os
from pathlib import Path

from djangocli.constants import EnvType
from djangocli.core.envfile_manage import inject_env
from scripts.check_and_create_log_file import check_and_create_log_file

# 部署环境
ENV = os.getenv("DC_ENV", EnvType.LOCAL)

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent

# 对于本地开发环境，通过建立.env文件，可以在启动时便导入环境变量，解决envfile不支持在Pycharm Terminal / Python Console
# 中导入环境变量的问题，当然也可以将env/script的脚本分别加入到PyCharm的启用脚本（Terminal仍不支持前置命令；）
# -- 脚手架仅维护 environ.sh 👇👇👇
# .sh在生产环境仍为主流，为了避免一套环境维护两种类型的文件，在该脚手架中仅维护environ.sh文件，通过动态生成.env文件注入Django运行环境
inject_env(environ_sh_path=f"{BASE_DIR}/scripts/deploy/{ENV}/environ.sh")

# 默认配置文件模块，当相应环境的配置文件模块不存在时需要导入该默认配置
DEFAULT_CONF_MODULE = os.getenv("DC_DEFAULT_CONF_MODULE") or "conf.default_settings"
DJANGO_CONF_MODULE = (DEFAULT_CONF_MODULE, f"conf.{ENV}")[os.path.exists(f"{BASE_DIR}/conf/{ENV}.py")]

try:
    _module = __import__(DJANGO_CONF_MODULE, globals(), locals(), ["*"])
except ImportError as error:
    raise ImportError(f"Could not import config {DJANGO_CONF_MODULE} (Is it on sys.path?): {error}")

for _setting in dir(_module):
    if _setting == _setting.upper():
        locals()[_setting] = getattr(_module, _setting)

# 需要覆盖全局的变量
BASE_DIR = BASE_DIR

# check and create log file
check_and_create_log_file(log_file_paths=list(_module.LOGGING_FILE.values()))
