# k8s 部署
> 假设项目根目录为变量 `PROJECT_DIR`


## 依赖服务安装


### 安装 Docker

Centos：https://yeasy.gitbook.io/docker_practice/install/centos

你可以在上述教程中找到更多相关系统的安装教程

### 安装 minikube

按照教程安装并启动 minikube：https://minikube.sigs.k8s.io/docs/start/


### 安装 Helm

按照教程安装并启动 Helm： https://helm.sh/zh/docs/intro/install/



## 拉取代码


### Git

```shell
git clone https://github.com/ZhuoZhuoCrayon/djangocli.git
```

查看版本，本项目通过 `tag` 标记版本号
```shell
git tag
```

切换到具体版本
```shell
git checkout tags/<version> -b <new_branch_name>
```

### 拉取指定版本

拉取指定版本包
```shell
curl -LO https://github.com/ZhuoZhuoCrayon/djangocli/archive/refs/tags/<version>.tar.gz
```

解压
```shell
tar -xvzf <version>.tar.gz

# 进入项目根目录
cd djangocli-<version>
ls -al
```

## 最小化部署
> 起始路径为项目根目录

### helm 依赖构建

进入 helm 目录
```shell
cd .helm/djangocli
```

安装依赖 
```shell
helm dependency update
```

### charts 说明

```shell
tree .
```

```text
.
├── Chart.lock  # 依赖版本
├── Chart.yaml  # charts包信息、依赖声明
├── charts  # 依赖charts包
│   ├── common-1.7.1.tgz
│   ├── mariadb-9.4.0.tgz
│   └── redis-14.8.7.tgz
├── templates   # charts模板
│   ├── NOTES.txt   # 启动后提示信息
│   ├── _helpers.tpl    # 公共模板
│   ├── backend
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   ├── celery
│   │   └── worker-deployment.yaml
│   ├── nginx
│   │   ├── deployment.yaml
│   │   ├── nginx-conf-configmap.yaml
│   │   └── service.yaml
│   ├── secret  # 敏感信息管理
│   │   ├── app.yaml
│   │   ├── mariadb.yaml
│   │   └── redis.yaml
│   └── serviceaccount.yaml
├── values-private.yaml # 下一个步骤会介绍
└── values.yaml # helm 全局变量管理

```


### 完善 values-private.yaml

拷贝 `values.yaml`
```shell
cp values.yaml values-private.yaml
```

为了避免敏感信息泄漏，不直接使用 `values.yaml`，请不要将 `values-private.yaml`提交到版本仓库

填写 `appCredentials.superuser`：`superuser` 的信息将用于初始化 django admin
```yaml
appCredentials:
  secretKey:
  appName: "django-cli"
  appVersion: "latest"
  superuser:
     username:
     password:
     email:
```

将 `backend.image` `celeryworker.image` 中 `caicrayon/djangocli` 的版本信息替换为自己需要的版本

检查yaml配置
```shell
helm install --debug --dry-run djangocli -f values-private.yaml .
```

### 部署到 minikube

```shell
cd ${PROJECT_DIR}/.helm/djangocli

helm install djangocli -f values-private.yaml .
```

### 访问（以 minikube 为例）

#### 本地访问

```shell
minikube service djangocli-nginx

# 仅显示链接
minikube service djangocli-nginx --url
```


#### 允许服务器访问

```shell
nohup kubectl port-forward --address 0.0.0.0 svc/djangocli-nginx <accessPort>:<nodePort> >> djangocli.log 2>&1 &
```
* accessPort: 访问端口
* nodePort: 暴露服务的`NodePort`
