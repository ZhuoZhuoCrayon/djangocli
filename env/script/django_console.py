# -*- coding: utf-8 -*-
import sys
import django
import dotenv

# 打印系统信息
print('Python %s on %s' % (sys.version, sys.platform))
print('Django %s' % django.get_version())

# 载入项目路径
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
# 导入环境变量
dotenv.load_dotenv(dotenv_path=PROJECT_ROOT + "/env/dc_dev.env")

# 启动Django
if 'setup' in dir(django):
    django.setup()

import django_manage_shell
django_manage_shell.run(PROJECT_ROOT)
