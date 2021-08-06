# TODO 当前版本不支持
# 相比与slim系，alpine占用空间 < 10M
# 选择合适镜像 -> https://aws.amazon.com/cn/blogs/china/choose-the-best-docker-image-for-your-python-application/
FROM python:3.7-alpine
# FROM python:3.7-slim

ENV DC_ENV=local

COPY scripts /setup/scripts
COPY requirements.txt /setup/requirements.txt

# The -e causes the command to stop on any errors. \
# A more typical syntax is to separate commands with && to stop on any error.
# The -x causes the shell to output each command being run. This is useful for debugging scripts.
# refer: https://stackoverflow.com/questions/47143319/what-does-set-x-do-in-dockerfile

# slim
# RUN_DEPS 用于安装 mysql-client 的依赖
# 参考：https://stackoverflow.com/questions/59554493/unable-to-fire-a-docker-build-for-django-and-mysql
#RUN set -ex \
#    && RUN_DEPS=" \
#    python3-dev \
#    default-libmysqlclient-dev \
#    gcc \
#    " \
#    && apt-get update && apt-get install -y $RUN_DEPS \
#    && pip install --upgrade pip \
#    && pip install --no-cache-dir -r /setup/requirements.txt

# alpine
RUN set -ex \
    && apk update && apk add musl-dev mariadb-dev gcc \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /setup/requirements.txt


ADD . /code
WORKDIR /code

COPY scripts/services/docker/django-migrate-docker-entrypoint.sh /django-migrate-docker-entrypoint.sh

# 收集静态资源（包括 drf_yasg 等）
RUN echo "yes" | python manage.py collectstatic

# EXPOSE 2170

ENTRYPOINT ["/django-migrate-docker-entrypoint.sh"]

# CMD ["gunicorn", "--bind", "0.0.0.0:2170", "--workers", "3", "wsgi:application"]
# CMD ["python", "manage.py", "runserver", "$PORT"]
