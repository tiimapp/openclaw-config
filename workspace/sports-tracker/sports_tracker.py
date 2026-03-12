#!/usr/bin/env python3
"""
每小时自动搜索国内体育网站热门比赛并生成总结的脚本
使用 dashscope-websearch MCP 工具搜索腾讯体育、网易体育、懂球帝、直播吧等主流中文体育网站
"""

import json
import subprocess
import sys
import os
from datetime import datetime

def call_dashscope_websearch(query):
    """调用 dashscope-websearch MCP 工具进行搜索"""
    try:
        # 构建 MCP 调用命令
        cmd = [
            "mcporter", "call", "dashscope-websearch", "web_search",
            "--input-json", json.dumps({"query": query, "count": 5})
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                print(f"JSON解析错误: {result.stdout}")
                return None
        else:
            print(f"命令执行失败: {result.stderr}")
            return None
    except Exception as e:
        print(f"调用 dashscope-websearch 时出错: {e}")
        return None

def generate_sports_summary():
    """生成体育赛事摘要"""
    # 搜索查询
    sites = ["腾讯体育", "网易体育", "懂球帝", "直播吧"]
    queries = [
        f"site:{" OR site:".join([s.lower().replace('体育', '') for s in sites])} 最新热门比赛",
        "中超 CBA 热门比赛 最新赛况",
        "NBA 足球 热门赛事 今日比赛"
    ]
    
    all_results = []
    
    # 执行多次搜索以获取全面信息
    for query in queries:
        print(f"正在搜索: {query}")
        result = call_dashscope_websearch(query)
        if result:
            all_results.append(result)
    
    if not all_results:
        return "未能获取到体育赛事信息。"
    
    # 提取关键信息并生成摘要
    summary = "# 🏆 今日热门体育赛事\n\n"
    
    # 这里需要根据实际返回的数据结构进行解析
    # 由于我们不知道确切的返回格式，先创建一个通用的处理方式
    matches_info = []
    
    for result in all_results:
        if isinstance(result, dict) and 'results' in result:
            for item in result['results']:
                if 'title' in item and 'url' in item:
                    # 提取比赛信息
                    title = item['title']
                    # 简单提取对阵双方和比分/时间
                    matches_info.append({
                        'title': title,
                        'url': item['url'],
                        'snippet': item.get('snippet', '')
                    })
        elif isinstance(result, list):
            for item in result:
                if isinstance(item, dict) and 'title' in item:
                    matches_info.append({
                        'title': item['title'],
                        'url': item.get('url', ''),
                        'snippet': item.get('snippet', '')
                    })
    
    # 去重并限制数量
    unique_matches = []
    seen_titles = set()
    
    for match in matches_info:
        if match['title'] not in seen_titles and len(unique_matches) < 10:
            seen_titles.add(match['title'])
            unique_matches.append(match)
    
    if not unique_matches:
        return "未能解析到具体的比赛信息。"
    
    # 生成简洁摘要
    for i, match in enumerate(unique_matches[:8], 1):
        summary += f"{i}. **{match['title']}**\n"
        if match['snippet']:
            # 提取关键信息如比分、时间等
            snippet = match['snippet'][:100] + "..." if len(match['snippet']) > 100 else match['snippet']
            summary += f"   {snippet}\n"
        summary += "\n"
    
    summary += f"\n*数据更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}*"
    
    return summary

def main():
    """主函数"""
    try:
        summary = generate_sports_summary()
        print(summary)
        
        # 将结果保存到文件，以便后续推送
        output_file = os.path.expanduser("~/.openclaw/workspace/sports-tracker/latest_summary.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print(f"\n摘要已保存到: {output_file}")
        return 0
    except Exception as e:
        print(f"执行过程中出错: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
