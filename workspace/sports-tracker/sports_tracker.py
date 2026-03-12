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

def call_dashscope_websearch(query, count=5):
    """调用 dashscope-websearch MCP 工具进行搜索"""
    try:
        # 设置工作目录为 OpenClaw 工作目录，确保 mcporter 能找到配置文件
        openclaw_workspace = os.path.expanduser("~/.openclaw/workspace")
        
        # 使用正确的参数格式: query=value count=value
        cmd = [
            "mcporter", "call", "dashscope-websearch.bailian_web_search",
            "query=" + query,
            "count=" + str(count)
        ]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=30,
            cwd=openclaw_workspace  # 设置工作目录
        )
        
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

def extract_matches_from_results(search_results):
    """从搜索结果中提取比赛信息"""
    matches = []
    
    if not isinstance(search_results, dict):
        return matches
    
    # dashscope-websearch 返回的格式包含 pages 数组
    pages = search_results.get('pages', [])
    
    for page in pages:
        if isinstance(page, dict):
            title = page.get('title', '')
            snippet = page.get('snippet', '')
            url = page.get('url', '')
            
            # 检查是否包含比赛相关信息
            if any(keyword in title.lower() or keyword in snippet.lower() 
                   for keyword in ['比赛', '赛事', 'vs', '对阵', '比分', '赛程', 'nba', 'cba', '中超', '足球', '篮球', '常规赛', '直播']):
                matches.append({
                    'title': title,
                    'snippet': snippet,
                    'url': url
                })
    
    return matches

def generate_sports_summary():
    """生成体育赛事摘要"""
    # 搜索查询 - 针对中文体育网站和热门赛事
    queries = [
        "今日热门体育比赛 NBA CBA 中超",
        "最新体育赛事 比分 时间 直播",
        "腾讯体育 网易体育 懂球帝 直播吧 热门比赛"
    ]
    
    all_matches = []
    
    # 执行多次搜索以获取全面信息
    for query in queries:
        print(f"正在搜索: {query}")
        result = call_dashscope_websearch(query, count=3)
        if result:
            matches = extract_matches_from_results(result)
            all_matches.extend(matches)
    
    if not all_matches:
        return "未能获取到体育赛事信息。"
    
    # 去重并限制数量
    unique_matches = []
    seen_titles = set()
    
    for match in all_matches:
        # 使用标题和片段的组合作为去重键
        title_key = (match['title'] + " " + match['snippet'])[:100]
        if title_key not in seen_titles and len(unique_matches) < 8:
            seen_titles.add(title_key)
            unique_matches.append(match)
    
    if not unique_matches:
        return "未能解析到具体的比赛信息。"
    
    # 生成简洁摘要
    summary = "# 🏆 今日热门体育赛事\n\n"
    
    for i, match in enumerate(unique_matches, 1):
        summary += f"{i}. **{match['title']}**\n"
        if match['snippet']:
            # 清理和格式化片段
            snippet = match['snippet'].replace('\n', ' ').strip()
            if len(snippet) > 120:
                snippet = snippet[:120] + "..."
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
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print(f"\n摘要已保存到: {output_file}")
        return 0
    except Exception as e:
        print(f"执行过程中出错: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
