#!/bin/bash
# 每小时体育赛事跟踪任务

set -e

WORKSPACE="$HOME/.openclaw/workspace/sports-tracker"

echo "[$(date)] 开始执行体育赛事搜索任务..."

# 执行搜索和摘要生成
python3 "$WORKSPACE/sports_tracker.py"

echo "[$(date)] 摘要生成完成，开始推送到 Discord..."

# 推送到 Discord
python3 "$WORKSPACE/discord_push.py"

echo "[$(date)] 任务完成！"
