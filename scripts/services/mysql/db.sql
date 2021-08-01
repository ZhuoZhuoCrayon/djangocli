/* 注意修改成自己的APP_NAME */
CREATE DATABASE `django-cli` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

CREATE DATABASE IF NOT EXISTS `$APP_NAME` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

# 远程链接支持

# 前置操作
# /etc/mysql/my.conf
# bind-address = 0.0.0.0

# *.* -> 所有资源所有权限 1: 数据库 2: 表
# 'username'@'%': username -> 账户名，% -> 所有的访问原ip地址（支持ip的sql语法匹配，例如 %.0.0.123 ）
# IDENTIFIED BY 'password' -> 密码
# with grant option -> 允许级联授权。
grant all privileges on *.* to 'username'@'%' identified by 'password' with grant option;
# 刷新权限
flush privileges;


grant all privileges on *.* to 'root'@'%' identified by 'password' with grant option;
flush privileges;
