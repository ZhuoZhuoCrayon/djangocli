# run in project root
FROM python:3.7-alpine

ENV DC_ENV=prod

ADD . /code
WORKDIR /code

# The -e causes the command to stop on any errors. \
# A more typical syntax is to separate commands with && to stop on any error.
# The -x causes the shell to output each command being run. This is useful for debugging scripts.
# refer: https://stackoverflow.com/questions/47143319/what-does-set-x-do-in-dockerfile

# 安装 mariadb 相关依赖
RUN set -ex \
    && apk update && apk add musl-dev mariadb-dev gcc \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r support-files/deploy/$DC_ENV/requirements.txt

# 收集静态资源（包括 drf_yasg 等）
RUN python manage.py collectstatic --noinput

# docker run 启动时钩子
ENTRYPOINT ["scripts/services/k8s/images/app/django-migrate-docker-entrypoint.sh"]
