export DJANGO_SETTINGS_MODULE="settings"

export SECRET_KEY=
export APP_NAME="django-cli"
export APP_VERSION="v1"

# 是否保留生成的env文件
export DC_KEEP_ENVFILE="False"

# 默认配置文件模块，当相应环境的配置文件模块不存在时需要导入该默认配置
export DC_DEFAULT_CONF_MODULE="conf.default_settings"

# MYSQL
export DC_MYSQL_USER="root"
export DC_MYSQL_PASSWORD=
export DC_MYSQL_HOST="localhost"
export DC_MYSQL_PORT="3306"

# REDIS
export DC_REDIS_HOST="localhost"
export DC_REDIS_PASSWORD=
export DC_REDIS_PORT="6379"


# USER
export DC_SUPER_USER_NAME="crayon"
export DC_SUPER_PASSWORD="123"
