## 初始化项目数据库


### 创建用户
在 `root` 权限下创建当前项目所属用户

`'your_app_name'@'ip_expr'` 组成
* `your_app_name`: 取环境变量中的 `APP_NAME` 或者 `DC_MYSQL_USER`
* `ip_expr`: `%`允许任意IP访问，若内网部署，可以修改为IP表达式，例如 `127.0.0.*` 或明确的IP

```mysql
create user 'your_app_name'@'ip_expr' identified by 'your_password';
/* 刷新权限 */
flush privileges
```


### 授予权限

将正式 & 测试数据库 `APP_NAME` 的全部权限授予用户 `'your_app_name'@'ip_expr'`

测试数据库名称：本项目采用 `${APP_NAME}_test"`

```mysql
grant all privileges on 'your_app_name'.'*' to 'your_app_name'@'ip_expr';
grant all privileges on 'your_app_name_test'.'*' to 'your_app_name'@'ip_expr';
flush privileges
```

### 检查授予情况
```mysql
show grants for 'your_app_name'@'ip_expr'
```

如果上述步骤成功，可以看到下列类似的数据
```text
+-----------------------------------------------------------------------------------------------------------+
| Grants for django-cli@%                                                                                   |
+-----------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `django-cli`@`%` IDENTIFIED BY PASSWORD 'xxx' |
| GRANT ALL PRIVILEGES ON `django-cli`.* TO `django-cli`@`%`                                                |
| GRANT ALL PRIVILEGES ON `django-cli_test`.* TO `django-cli`@`%`                                           |
+-----------------------------------------------------------------------------------------------------------+
3 rows in set (0.000 sec)
```

### 创建数据库

```sql
create database `your_app_name` default character set utf8mb4 collate utf8mb4_general_ci;
```
    