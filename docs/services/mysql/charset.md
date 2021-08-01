

## MySQL设置默认字符集

### 查看系统当前默认字符集设置
```mysql
SHOW VARIABLES LIKE 'char%'; 
SHOW VARIABLES LIKE 'collation%';
```

### 查看数据库/表编码
```mysql
show create [database_or_table_name] score;
```

### 查看表每一列的编码
```mysql
show full columns from [table_name];
```

### 修改配置 - my.cnf
```
[client]
default-character-set=utf8mb4

[mysql]
default-character-set=utf8mb4

[mysqld]
collation-server = utf8mb4_unicode_ci
init-connect='SET NAMES utf8mb4'
character-set-server = utf8mb4
```

### 修改存量数据库字符集

```mysql
ALTER DATABASE [databasename] CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE [tablename] CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

