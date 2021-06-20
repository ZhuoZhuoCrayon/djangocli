# -*- coding: utf-8 -*-
import sys

import dotenv

# 打印系统信息
print("Python %s on %s" % (sys.version, sys.platform))

sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])

# 导入环境变量
dotenv.load_dotenv(dotenv_path=PROJECT_ROOT + "scripts/deploy/local/environ.sh")
