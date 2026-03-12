#!/usr/bin/env python3
"""
将体育赛事摘要推送到 Discord #gameday 频道
"""

import json
import os
import sys
import subprocess

def get_discord_webhook_url():
    """获取 Discord webhook URL"""
    # 从环境变量或配置文件中获取 webhook URL
    webhook_url = os.environ.get('DISCORD_GAMEDAY_WEBHOOK')
    if not webhook_url:
        config_path = os.path.expanduser('~/.openclaw/workspace/sports-tracker/discord_config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                webhook_url = config.get('webhook_url')
    return webhook_url

def send_to_discord(content):
    """发送内容到 Discord"""
    webhook_url = get_discord_webhook_url()
    if not webhook_url or webhook_url == "YOUR_DISCORD_WEBHOOK_URL_HERE":
        print("警告: Discord webhook URL 未配置，跳过推送")
        print("请在 ~/.openclaw/workspace/sports-tracker/discord_config.json 中设置 webhook_url")
        return False
    
    try:
        # 使用 curl 发送消息
        cmd = [
            "curl", "-X", "POST",
            "-H", "Content-Type: application/json",
            "-d", json.dumps({"content": content[:1990] if len(content) > 1990 else content}),
            webhook_url
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("成功发送到 Discord")
            return True
        else:
            print(f"发送失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"发送过程中出错: {e}")
        return False

def main():
    """主函数"""
    # 读取最新的摘要文件
    summary_file = os.path.expanduser("~/.openclaw/workspace/sports-tracker/latest_summary.md")
    
    if not os.path.exists(summary_file):
        print("错误: 摘要文件不存在")
        return 1
    
    with open(summary_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip():
        print("错误: 摘要内容为空")
        return 1
    
    if send_to_discord(content):
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
