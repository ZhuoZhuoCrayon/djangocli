BASHRC_PATH="$HOME/.bashrc"

# 先执行卸载
cat "$PWD/pyenv_uninstall.sh" | bash

# 依赖安装
yum install -y git
yum install -y curl
yum install -y gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel

# 加载执行安装脚本
curl https://pyenv.run | bash

{
  echo 'export PYENV_ROOT="$HOME/.pyenv"';
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"';
  echo 'eval "$(pyenv init --path)"'
} >> "$BASHRC_PATH"


# 重启shell
exec "$SHELL"
