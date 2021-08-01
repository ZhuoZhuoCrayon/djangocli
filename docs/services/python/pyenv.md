# 使用 pyenv
> CentOS 8.0 CentOS 8.2
> 
> 2021 / 07 / 08


## 安装

### 安装依赖
```shell
yum install git
yum install curl
yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel
```

### 拉取脚本并安装
```shell
curl https://pyenv.run | bash
```

如果出现
```shell
fatal: unable to access 'https://github.com/pyenv/pyenv-doctor.git/': Empty reply from server
Failed to git clone https://github.com/pyenv/pyenv-doctor.git
```

可以尝试 `rm -rf ~/.pyenv` & `export USE_GIT_URI = true(任意非空字符串)` & `curl https://pyenv.run | bash` 重新执行安装

`export USE_GIT_URI = true(任意非空字符串)` 将使用 `git://` 替代 `https://`

### 添加下列语句到`.bashrc`
```shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
```

### 重启shell
```shell
exec $SHELL
```

### 检查是否成功安装
```shell
pyenv --version
```

## 卸载

### 移除安装目录

```shell
rm -rf ~/.pyenv
```


### 移除添加到 `.bashrc` 的语句
```shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
```

### 重启shell
```shell
exec $SHELL
```



## 常见问题


### pyenv install 报错: `curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to domain.com:443`

尝试安装/更新 nss(Network Security Service, 网络安全服务)
```shell
yum install nss
# 或者
yum update nss
```
