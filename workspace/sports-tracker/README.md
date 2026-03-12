# 体育赛事跟踪任务

这是一个每小时自动搜索国内体育网站热门比赛并生成总结的任务。

## 功能

- 使用 dashscope-websearch MCP 工具搜索腾讯体育、网易体育、懂球帝、直播吧等主流中文体育网站
- 获取最新热门赛事信息
- 生成包含赛事名称、对阵双方、关键信息（比分/时间/热度）的简洁中文摘要
- 在 Discord #gameday 频道推送结果

## 文件结构

- `sports_tracker.py` - 主要的搜索和摘要生成脚本
- `discord_push.py` - Discord 推送脚本
- `run_sports_tracker.sh` - 完整的运行脚本
- `discord_config.json` - Discord webhook 配置文件
- `latest_summary.md` - 最新生成的摘要文件（自动生成）

## 配置 Discord Webhook

1. 在 Discord 服务器中创建一个 webhook
2. 复制 webhook URL
3. 编辑 `discord_config.json` 文件，替换 `YOUR_DISCORD_WEBHOOK_URL_HERE` 为实际的 webhook URL

```json
{
  "webhook_url": "https://discord.com/api/webhooks/your-webhook-url"
}
```

或者设置环境变量：
```bash
export DISCORD_GAMEDAY_WEBHOOK="https://discord.com/api/webhooks/your-webhook-url"
```

## 手动运行

```bash
cd ~/.openclaw/workspace/sorts-tracker
./run_sports_tracker.sh
```

## 自动运行

任务已配置为每小时自动运行（通过 cron 作业）：
```
0 * * * * cd /home/admin/.openclaw/workspace/sports-tracker && ./run_sports_tracker.sh >> /tmp/sports_tracker.log 2>&1
```

## 日志

运行日志保存在 `/tmp/sports_tracker.log`

## 依赖

- mcporter (已配置 dashscope-websearch MCP 服务器)
- curl
- Python 3
