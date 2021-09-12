#!/bin/bash

# 单元测试

# coverage 忽略文件
COVERAGE_OMIT_PATH="*/virtualenv/*,*/*venv*/*,*/migrations/*,*/tests/*"

echo "current python version -> ${PYTHON_VERSION}, mainline python version -> ${MAINLINE_PYTHON_VERSION}"
echo "current django version -> ${DJANGO_VERSION}, mainline django version -> ${MAINLINE_DJANGO_VERSION}"

if [[ "${PYTHON_VERSION}" == "${MAINLINE_PYTHON_VERSION}" && "${DJANGO_VERSION}" == "${MAINLINE_DJANGO_VERSION}" ]]
then
  # 删除coverage历史归档文件
  coverage erase
  coverage run --omit="$COVERAGE_OMIT_PATH" ./manage.py test
  coverage report --omit="$COVERAGE_OMIT_PATH"
else
  python manage.py test
fi
