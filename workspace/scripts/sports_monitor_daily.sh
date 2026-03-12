#!/bin/bash
# Sports Monitor 每日早间报告 - 每天 9:00 自动推送

SCRIPT_DIR="$HOME/.agents/skills/sports-monitor"
OUTPUT_FILE="/tmp/sports_monitor_output.txt"
CHANNEL_ID="1479649544458338405"

# 获取当日赛事
python3 "$SCRIPT_DIR/sports_monitor.py" --today > "$OUTPUT_FILE" 2>&1

if [ $? -eq 0 ]; then
    # 读取输出内容并发送到 Discord 频道
    CONTENT=$(cat "$OUTPUT_FILE")
    openclaw message send --channel discord --target "$CHANNEL_ID" --message "$CONTENT" 2>&1
    echo "$(date): Sports Monitor 报告已发送" >> /tmp/sports_monitor_cron.log
else
    echo "$(date): Sports Monitor 执行失败" >> /tmp/sports_monitor_cron.log
fi
