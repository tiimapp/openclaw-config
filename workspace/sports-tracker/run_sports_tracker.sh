#!/bin/bash
# 每小时运行的体育赛事跟踪脚本

set -e

# 获取脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "[$(date)] 开始执行体育赛事跟踪任务..."

# 运行体育赛事搜索和摘要生成
cd "$SCRIPT_DIR"
python3 sports_tracker.py

# 推送到 Discord
python3 discord_push.py

echo "[$(date)] 体育赛事跟踪任务完成"
