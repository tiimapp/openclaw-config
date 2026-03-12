#!/usr/bin/env python3
"""
C2605 Price Fetcher - Tavily Optimized

Uses Tavily AI search API to find real-time C2605 corn futures prices
from multiple Chinese financial websites.

Fallback chain:
1. Tavily Search → Extract from search results
2. AKShare Historical (reliable, but may be stale)

Usage:
    python3 c2605_tavily_fetcher.py [--test]
"""

import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Try to import requests for Tavily API
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Warning: requests library not available")

# Try to import AKShare as fallback
try:
    import akshare as ak
    AKSHARE_AVAILABLE = True
except ImportError:
    AKSHARE_AVAILABLE = False
    print("Warning: AKShare not available")


# Configuration
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY', '')
TAVILY_API_URL = 'https://api.tavily.com/search'

# Target websites for price data
TARGET_SITES = [
    'finance.sina.com.cn',
    'futures.eastmoney.com',
    'finance.qq.com',
    'www.dce.com.cn',
    'www.cfi.cn',
    'futures.hexun.com',
]

# Price pattern regex
PRICE_PATTERN = re.compile(r'(?:玉米|C2605|玉米 2605).*?(?:价格|现价|最新|收盘)[:：]?\s*¥?\s*([\d.]+)', re.IGNORECASE)


def tavily_search(query: str, max_results: int = 5) -> Optional[List[Dict[str, Any]]]:
    """
    Search using Tavily AI search API.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return
    
    Returns:
        List of search results or None if failed
    """
    if not REQUESTS_AVAILABLE:
        print("❌ requests library not available for Tavily API")
        return None
    
    if not TAVILY_API_KEY:
        print("⚠️ TAVILY_API_KEY not set, skipping Tavily search")
        return None
    
    try:
        payload = {
            "query": query,
            "search_depth": "basic",
            "include_answer": False,
            "include_raw_content": False,
            "max_results": max_results,
            "include_domains": TARGET_SITES,
            "time_range": "day"
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TAVILY_API_KEY}"
        }
        
        response = requests.post(TAVILY_API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        results = data.get('results', [])
        
        print(f"✅ Tavily search successful: {len(results)} results")
        return results
        
    except Exception as e:
        print(f"❌ Tavily search failed: {e}")
        return None


def extract_price_from_content(content: str, symbol: str = 'C2605') -> Optional[Dict[str, Any]]:
    """
    Extract price data from text content.
    
    Args:
        content: Text content to parse
        symbol: Futures symbol
    
    Returns:
        Dictionary with price data or None
    """
    # Look for price patterns
    patterns = [
        r'玉米\s*(?:2605|期货)?\s*(?:最新价 | 当前价 | 收盘价 | 价格)[:：]?\s*([0-9]{3,4}(?:\.[0-9]{1,2})?)',
        r'C2605\s*(?:最新价 | 当前价 | 收盘价 | 价格)[:：]?\s*([0-9]{3,4}(?:\.[0-9]{1,2})?)',
        r'(?:现手 | 最新)\s*[:：]?\s*([0-9]{3,4}(?:\.[0-9]{1,2})?)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            try:
                price = float(match.group(1))
                # Validate price range (corn futures typically 2000-3000)
                if 2000 <= price <= 3500:
                    return {
                        'price': price,
                        'source': 'tavily_search',
                        'confidence': 'high' if '收盘' in content else 'medium'
                    }
            except (ValueError, IndexError):
                continue
    
    return None


def fetch_from_tavily(symbol: str = 'C2605') -> Optional[Dict[str, Any]]:
    """
    Fetch C2605 price data using Tavily search.
    
    Args:
        symbol: Futures symbol
    
    Returns:
        Dictionary with price data or None
    """
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Search queries (in Chinese for better results)
    queries = [
        f'玉米期货 C2605 {today} 最新价格 行情',
        f'大连商品交易所 玉米 2605 实时价格 {today}',
        f'C2605 玉米期货 收盘价 {today}',
    ]
    
    all_results = []
    
    for query in queries:
        results = tavily_search(query, max_results=3)
        if results:
            all_results.extend(results)
    
    if not all_results:
        print("⚠️ No Tavily results found")
        return None
    
    # Try to extract price from each result
    for result in all_results:
        # Check title
        title = result.get('title', '')
        content = result.get('content', '')
        url = result.get('url', '')
        
        # Extract price from content
        price_data = extract_price_from_content(content, symbol)
        if price_data:
            print(f"✅ Price found from {url}: ¥{price_data['price']}")
            return {
                'symbol': symbol,
                'name': '玉米 2605',
                'current_price': price_data['price'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'data_source': 'tavily',
                'source_url': url,
                'confidence': price_data.get('confidence', 'medium'),
                'is_stale': False
            }
    
    print("⚠️ Could not extract price from Tavily results")
    return None


def fetch_from_akshare(symbol: str = 'C2605') -> Optional[Dict[str, Any]]:
    """
    Fallback: Fetch from AKShare historical data.
    
    Args:
        symbol: Futures symbol
    
    Returns:
        Dictionary with price data or None
    """
    if not AKSHARE_AVAILABLE:
        print("⚠️ AKShare not available")
        return None
    
    try:
        futures_df = ak.futures_zh_daily_sina(symbol=symbol)
        
        if futures_df is not None and len(futures_df) > 0:
            row = futures_df.iloc[-1]
            last_date = row.get('date', '')
            today = datetime.now().strftime('%Y-%m-%d')
            
            is_stale = (last_date != today)
            
            if is_stale:
                print(f"⚠️ STALE DATA: Data is from {last_date}, not today ({today})")
            else:
                print(f"✅ Using today's historical data")
            
            data = {
                'symbol': symbol,
                'name': '玉米 2605',
                'current_price': float(row.get('close', 0)),
                'open': float(row.get('open', 0)),
                'high': float(row.get('high', 0)),
                'low': float(row.get('low', 0)),
                'previous_close': float(row.get('pre_close', row.get('close', 0))),
                'volume': int(row.get('volume', 0)),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'change': 0,
                'change_percent': 0,
                'data_source': 'akshare_historical',
                'data_date': last_date,
                'is_stale': is_stale
            }
            
            # Calculate change
            if 'pre_close' in row:
                prev_close = float(row.get('pre_close', data['current_price']))
                data['previous_close'] = prev_close
                data['change'] = data['current_price'] - prev_close
                data['change_percent'] = (data['change'] / prev_close * 100) if prev_close else 0
            
            return data
            
    except Exception as e:
        print(f"❌ AKShare fetch failed: {e}")
    
    return None


def fetch_c2605_price(symbol: str = 'C2605') -> Optional[Dict[str, Any]]:
    """
    Main entry point - Fetch C2605 price with optimized fallback chain.
    
    Priority:
    1. Tavily Search (AI-powered, real-time)
    2. AKShare Historical (reliable, but may be stale)
    
    Args:
        symbol: Futures symbol
    
    Returns:
        Dictionary with price data
    
    Raises:
        RuntimeError: If all sources fail
    """
    print(f"🔍 Fetching {symbol} price data...")
    print(f"   Tavily API: {'✅ Configured' if TAVILY_API_KEY else '❌ Not configured'}")
    print(f"   AKShare: {'✅ Available' if AKSHARE_AVAILABLE else '❌ Not available'}")
    print()
    
    # Try Tavily first
    if TAVILY_API_KEY:
        print("📊 Attempt 1/2: Tavily Search...")
        data = fetch_from_tavily(symbol)
        if data:
            print(f"✅ Success! Price: ¥{data['current_price']} (Tavily)")
            return data
        print()
    
    # Fallback to AKShare
    print("📊 Attempt 2/2: AKShare Historical...")
    data = fetch_from_akshare(symbol)
    if data:
        print(f"✅ Success! Price: ¥{data['current_price']} (AKShare)")
        return data
    
    # All sources failed - raise exception
    error_msg = (
        f"❌ 无法获取 {symbol} 数据：\n"
        "   1. Tavily Search 无法获取数据\n"
        "   2. AKShare 也无法获取数据\n"
        "请检查网络连接或稍后重试。"
    )
    print(error_msg)
    raise RuntimeError(error_msg)


def main():
    """Test the fetcher."""
    import argparse
    
    parser = argparse.ArgumentParser(description='C2605 Tavily Price Fetcher')
    parser.add_argument('--test', action='store_true', help='Run test mode')
    parser.add_argument('--symbol', type=str, default='C2605', help='Futures symbol')
    
    args = parser.parse_args()
    
    # Fetch price data
    data = fetch_c2605_price(args.symbol)
    
    # Print results
    print("\n" + "=" * 60)
    print(f"📊 {data['name']} ({data['symbol']}) Price Data")
    print("=" * 60)
    print(f"Current Price: ¥{data['current_price']:.2f}")
    print(f"Change: {data.get('change', 0):+.2f} ({data.get('change_percent', 0):+.2f}%)")
    print(f"Open: ¥{data.get('open', 0):.2f}")
    print(f"High: ¥{data.get('high', 0):.2f}")
    print(f"Low: ¥{data.get('low', 0):.2f}")
    print(f"Volume: {data.get('volume', 0):,}")
    print(f"Data Source: {data['data_source']}")
    print(f"Timestamp: {data['timestamp']}")
    print(f"Is Stale: {data.get('is_stale', False)}")
    if data.get('source_url'):
        print(f"Source URL: {data['source_url']}")
    print("=" * 60)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())


def fetch_c2605_price_tavily(symbol: str = 'C2605') -> Optional[Dict[str, Any]]:
    """
    Wrapper function for C2605 price fetch - returns normalized data structure.
    
    This function is designed to be used as a validation source alongside AKShare.
    
    Returns:
        Dictionary with 'price' key for compatibility
    """
    data = fetch_c2605_price(symbol)
    
    if data:
        # Normalize to use 'price' instead of 'current_price' for compatibility
        if 'current_price' in data and 'price' not in data:
            data['price'] = data['current_price']
        return data
    
    return None
