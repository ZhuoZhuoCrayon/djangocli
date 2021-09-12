#!/bin/bash

cat << EOF
SCRIPT_DIR -> "$SCRIPT_DIR"
PROJECT_ROOT -> "$PROJECT_ROOT"
PYTHON_VERSION -> "$PYTHON_VERSION"
DJANGO_VERSION -> "$DJANGO_VERSION"
EOF

pip install --upgrade pip
pip install -r support-files/deploy/"$DC_ENV"/requirements.txt
pip install django=="${DJANGO_VERSION}"

# 删除遗留数据库，并新建一个空的本地数据库
CREATE_DB_SQL="
drop database if exists \`${DC_MYSQL_NAME}\`;
drop database if exists \`${DC_MYSQL_NAME}_test\`;
create database \`${DC_MYSQL_NAME}\` default character set utf8mb4 collate utf8mb4_general_ci;
"

if [ "$DC_MYSQL_PASSWORD" ]; then
  mysql -h"$DC_MYSQL_HOST" -P"$DC_MYSQL_PORT" -u"$DC_MYSQL_USER" -p"$DC_MYSQL_PASSWORD" -sNe "$CREATE_DB_SQL"
else
  # 没有密码时无需-p，防止回车阻塞
  mysql -h"$DC_MYSQL_HOST" -P"$DC_MYSQL_PORT" -u"$DC_MYSQL_USER" -sNe "$CREATE_DB_SQL"
fi

# 执行 migrate
python manage.py migrate
