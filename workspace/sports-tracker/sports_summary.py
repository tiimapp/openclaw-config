#!/usr/bin/env python3
"""
每小时自动搜索国内体育网站热门比赛并生成总结的脚本
使用 dashscope-websearch MCP 工具搜索腾讯体育、网易体育、懂球帝、直播吧等主流中文体育网站
"""

import json
import subprocess
import sys
import datetime
from typing import List, Dict, Any

def search_sports_news() -> List[Dict[str, Any]]:
    """使用 dashscope-websearch MCP 工具搜索体育新闻"""
    # 构建搜索查询 - 包含多个主流中文体育网站
    query = "site: sports.qq.com OR site: sports.163.com OR site: dongqiudi.com OR site: zhibo8.cc 热门比赛 最新赛事"
    
    # 调用 mcporter 执行 dashscope-websearch
    try:
        result = subprocess.run([
            'mcporter', 'call', 'dashscope-websearch', 'web_search',
            '--arguments', json.dumps({"query": query, "max_results": 10})
        ], capture_output=True, text=True, check=True)
        
        response = json.loads(result.stdout)
        return response.get('results', [])
    except Exception as e:
        print(f"搜索失败: {e}", file=sys.stderr)
        return []

def extract_match_info(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """从搜索结果中提取比赛信息"""
    matches = []
    
    for result in results:
        title = result.get('title', '')
        url = result.get('url', '')
        content = result.get('content', '')
        
        # 简单提取比赛信息（实际应用中可能需要更复杂的解析）
        match_info = {
            'title': title,
            'url': url,
            'summary': content[:200] + '...' if len(content) > 200 else content,
            'source': extract_source(url)
        }
        matches.append(match_info)
    
    return matches[:5]  # 只保留前5个结果

def extract_source(url: str) -> str:
    """从URL提取来源网站"""
    if 'qq.com' in url:
        return '腾讯体育'
    elif '163.com' in url:
        return '网易体育'
    elif 'dongqiudi.com' in url:
        return '懂球帝'
    elif 'zhibo8.cc' in url:
        return '直播吧'
    else:
        return '其他'

def generate_summary(matches: List[Dict[str, Any]]) -> str:
    """生成简洁的中文摘要"""
    if not matches:
        return "暂无热门比赛信息。"
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    summary = f"🔥 **国内体育热门赛事摘要** ({current_time})\n\n"
    
    for i, match in enumerate(matches, 1):
        summary += f"{i}. **{match['title']}**\n"
        summary += f"   来源: {match['source']}\n"
        summary += f"   摘要: {match['summary']}\n"
        summary += f"   链接: <{match['url']}>\n\n"
    
    summary += "📊 数据来源于腾讯体育、网易体育、懂球帝、直播吧等主流体育网站"
    return summary

def main():
    """主函数"""
    print("开始搜索体育赛事信息...")
    results = search_sports_news()
    matches = extract_match_info(results)
    summary = generate_summary(matches)
    
    # 输出到stdout，供后续处理
    print(summary)
    
    # 同时保存到文件
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    with open(f"~/.openclaw/workspace/sports-tracker/summary_{timestamp}.txt", "w") as f:
        f.write(summary)

if __name__ == "__main__":
    main()
