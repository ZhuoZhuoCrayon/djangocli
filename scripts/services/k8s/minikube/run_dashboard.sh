# 在后台运行 Dashboard
# 脚本授权 -> chmod 777 run_dashboard.sh

# 启用 dashboard 并挂后台
nohup minikube dashboard --url >> run_dashboard.log 2>&1 &

# 预估启动时间并等待
sleep 1

# 获取主机IP
if [[ $1 ]]; then
  HOST=$1
else
  HOST=$(curl icanhazip.com)
fi

# 获取dashboard url，取最后一则匹配的url
DASHBOARD_URL=$(grep -E "http://127.0.0.1:[[:digit:]]+" run_dashboard.log | tail -n 1)
# 提取 dashboard 监听端口
DASHBOARD_PORT=$(echo "$DASHBOARD_URL" | sed -nr "s/^http:\/\/[0-9.]+:([0-9]+).*$/\1/p")

cat << EOF
HOST -> "$HOST"
DASHBOARD_URL -> "$DASHBOARD_URL"
DASHBOARD_PORT -> "$DASHBOARD_PORT"
EOF

# 开启代理，允许远程访问
nohup kubectl proxy --port="$DASHBOARD_PORT" --address="$HOST" --disable-filter=true >> run_dashboard.log 2>&1 &

# 替换localhost
echo "👉 ${DASHBOARD_URL/127.0.0.1/${HOST}}"
