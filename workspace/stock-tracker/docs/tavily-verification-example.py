#!/usr/bin/env python3
"""
Tavily Search Verification Example for C2605 Night Trading

This script demonstrates how to use Tavily Search API to verify
DCE Corn Futures (C2605) night trading session status.

Setup:
1. pip install tavily-python
2. export TAVILY_API_KEY='tvly-xxxxxxxxxxxxxxxxxxxx'
   (or add to ~/.openclaw/.env)

Usage:
    python3 tavily-verification-example.py
    python3 tavily-verification-example.py --json
"""

import os
import sys
import json
from datetime import datetime

try:
    from tavily import TavilyClient
except ImportError:
    print("❌ Tavily SDK not installed. Run: pip install tavily-python")
    sys.exit(1)


def verify_night_trading(query=None, days=7, max_results=5):
    """
    Verify night trading status using Tavily Search.
    
    Args:
        query: Search query (default: C2605 night trading)
        days: Limit results to last N days (default: 7)
        max_results: Number of results to return (default: 5)
    
    Returns:
        dict: Verification result with answer and sources
    """
    if query is None:
        query = "大连商品交易所 玉米期货 夜盘交易时间 2026"
    
    api_key = os.environ.get('TAVILY_API_KEY')
    if not api_key:
        print("❌ TAVILY_API_KEY not set. Please set environment variable.")
        print("   export TAVILY_API_KEY='tvly-xxxxxxxxxxxxxxxxxxxx'")
        sys.exit(1)
    
    client = TavilyClient(api_key=api_key)
    
    print(f"🔍 Searching Tavily for: {query}")
    print(f"   Topic: finance | Days: {days} | Max results: {max_results}")
    print()
    
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=max_results,
        include_answer=True,
        topic="finance",
        days=days
    )
    
    return response


def parse_night_session_status(answer):
    """
    Parse AI answer to determine night session status.
    
    Returns:
        str: "enabled", "disabled", or "uncertain"
    """
    if not answer:
        return "uncertain"
    
    answer_lower = answer.lower()
    
    # Positive indicators
    if any(kw in answer_lower for kw in ['有夜盘', '夜盘交易', '21:00', '21:00-23:00', 'enabled']):
        if any(kw in answer_lower for kw in ['玉米', 'C2605', '大商所', 'DCE']):
            return "enabled"
    
    # Negative indicators
    if any(kw in answer_lower for kw in ['无夜盘', '没有夜盘', 'not enabled', 'disabled', '暂未纳入']):
        if any(kw in answer_lower for kw in ['玉米', 'C2605', '大商所', 'DCE']):
            return "disabled"
    
    return "uncertain"


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Tavily verification for C2605 night trading')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    parser.add_argument('--days', type=int, default=7, help='Search last N days (default: 7)')
    parser.add_argument('--query', type=str, default=None, help='Custom search query')
    args = parser.parse_args()
    
    response = verify_night_trading(query=args.query, days=args.days)
    
    status = parse_night_session_status(response.get('answer', ''))
    
    result = {
        "timestamp": datetime.now().isoformat(),
        "query": response.get('query', ''),
        "status": status,
        "answer": response.get('answer', ''),
        "sources": [
            {
                "title": r.get('title', ''),
                "url": r.get('url', ''),
                "score": r.get('score', 0),
                "published_date": r.get('published_date', '')
            }
            for r in response.get('results', [])
        ],
        "follow_up_questions": response.get('follow_up_questions', [])
    }
    
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=" * 60)
        print("🔍 TAVILY VERIFICATION RESULT")
        print("=" * 60)
        print(f"\n⏰ Timestamp: {result['timestamp']}")
        print(f"📝 Query: {result['query']}")
        print(f"\n🎯 Status: {result['status'].upper()}")
        print(f"\n💡 AI Answer:\n{result['answer']}")
        print(f"\n📚 Sources ({len(result['sources'])}):")
        for i, source in enumerate(result['sources'], 1):
            print(f"  {i}. {source['title']}")
            print(f"     URL: {source['url']}")
            print(f"     Score: {source['score']} | Date: {source['published_date']}")
            print()
        if result['follow_up_questions']:
            print(f"\n❓ Follow-up Questions:")
            for q in result['follow_up_questions']:
                print(f"   - {q}")
        print("=" * 60)
    
    return result


if __name__ == '__main__':
    main()
