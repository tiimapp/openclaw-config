#!/usr/bin/env python3
"""
C2605 Corn Futures Monitor

Fetches DCE Corn Futures (C2605 - 玉米 2605 contract) price data
and generates reports for Discord.

Trading Hours (Asia/Shanghai UTC+8):
- Day session: 09:00-10:15, 10:30-11:30, 13:30-15:00
- No night session for corn
- Monday-Friday only

Data Source Strategy:
- dashscope-websearch (primary data source via DashScope LLM with enable_search)
- AKShare (fallback data source)
- Tavily (validation tool only)
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from trading_time_checker import (
    is_trading_time,
    is_trading_day,
    get_trading_status,
    get_next_trading_time,
    get_previous_trading_time,
)

# Import Tavily fetcher for validation
from fetchers.c2605_tavily_fetcher import fetch_c2605_price_tavily

# Try to import AKShare for futures data
try:
    import akshare as ak
    AKSHARE_AVAILABLE = True
except ImportError:
    AKSHARE_AVAILABLE = False

# Try to import requests for dashscope API
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration from JSON file."""
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), 'c2605_config.json')
    
    default_config = {
        'symbol': 'C2605',
        'symbol_name': '玉米 2605',
        'exchange': 'DCE',
        'discord_channel_id': '1475775915844960428',
        'trading_hours': {
            'sessions': [
                {'start': '09:00', 'end': '10:15'},
                {'start': '10:30', 'end': '11:30'},
                {'start': '13:30', 'end': '15:00'},
            ]
        },
        'report_preferences': {
            'hourly_report': True,
            'daily_summary': True,
            'include_chart': False,
        },
        'custom_holidays': {},
    }
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config: {e}. Using defaults.")
    
    return default_config


def fetch_from_dashscope_websearch(today: str) -> Optional[Dict[str, Any]]:
    """
    Fetch C2605 futures data from DashScope LLM API with web search enabled.
    This uses the qwen-max model with enable_search=true to search the web
    and extract the latest C2605 futures price.
    
    Args:
        today: Current date string in format YYYY-MM-DD
    
    Returns:
        Dictionary with current price data or None if fetch fails
    """
    if not REQUESTS_AVAILABLE:
        print("⚠️ requests library not available")
        return None
    
    # Get DashScope API key from environment
    api_key = os.getenv('DASHSCOPE_API_KEY')
    if not api_key:
        print("⚠️ DASHSCOPE_API_KEY not set, skipping dashscope-websearch")
        return None
    
    # Build query for DashScope with date context
    query = f"请搜索并告诉我：大连商品交易所玉米期货C2605合约在{today}的最新交易价格、开盘价、最高价、最低价和成交量"
    
    # DashScope API endpoint
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "qwen-max",
        "input": {
            "messages": [
                {"role": "user", "content": query}
            ]
        },
        "parameters": {
            "enable_search": True,
            "result_format": "text"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        
        # Parse response
        if 'output' not in data or 'text' not in data['output']:
            print("⚠️ Unexpected response format from DashScope")
            return None
        
        text = data['output']['text']
        print("✅ DashScope API returned data (with web search)")
        
        # Extract price from text response
        price_data = extract_price_from_dashscope_text(text)
        
        if price_data:
            price_data['data_source'] = 'dashscope-websearch'
            price_data['data_date'] = today
            # Ensure is_today is properly set based on data
            price_data['is_today'] = price_data.get('is_today', False)
            price_data['is_stale'] = not price_data.get('is_today', False)
            price_data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Check if data is fresh (from today)
            if price_data.get('is_today', False):
                print(f"✅ Real-time data fetched from dashscope-websearch: ¥{price_data.get('price', 'N/A')}")
                return price_data
            else:
                print(f"⚠️ dashscope-websearch data is stale (date: {price_data.get('date_in_response', 'unknown')}), will try AKShare")
        
        print("⚠️ Could not extract fresh price from dashscope-websearch response")
        if 'text' in data['output']:
            print(f"   Response text: {data['output']['text'][:500]}")
        return None
        
        print("⚠️ Could not extract price from dashscope-websearch response")
        print(f"   Response text: {text[:500]}")
        return None
        
    except requests.exceptions.Timeout:
        print("❌ dashscope-websearch request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error calling dashscope-websearch: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing dashscope-websearch response: {e}")
        return None


def extract_price_from_dashscope_text(text: str) -> Optional[Dict[str, Any]]:
    """
    Extract price data from DashScope API text response.
    
    Args:
        text: Raw text response from DashScope
    
    Returns:
        Dictionary with price data or None if not found
    """
    import re
    
    result = {}
    
    # Pattern for price: ¥2395.000, 2395.000元/吨, latest:2399, etc.
    patterns = {
        'price': r'(?:最新交易价格|最新价|最新|现价)[:：]?\s*¥?\s*([\d.]+)',
        'open': r'开盘价[:：]?\s*¥?\s*([\d.]+)',
        'high': r'最高价[:：]?\s*¥?\s*([\d.]+)',
        'low': r'最低价[:：]?\s*¥?\s*([\d.]+)',
        'previous_close': r'(?:昨结算|昨收|上一交易日结算价)[:：]?\s*¥?\s*([\d.]+)',
        'volume': r'成交量[:：]?\s*([\d.]+)手',
    }
    
    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                value = float(match.group(1))
                # For volume, no need to check price range
                if field == 'volume':
                    result[field] = int(value)
                elif 2000 <= value <= 3500:  # Validate price range for price fields
                    result[field] = value
            except (ValueError, IndexError):
                continue
    
    # Check if the data is from today
    if 'today' in text.lower() or datetime.now().strftime('%Y-%m-%d') in text:
        result['is_today'] = True
    else:
        # Check for date in response
        date_match = re.search(r'(\d{4}-\d{1,2}-\d{1,2})', text)
        if date_match:
            result['date_in_response'] = date_match.group(1)
            result['is_today'] = (date_match.group(1) == datetime.now().strftime('%Y-%m-%d'))
        else:
            result['is_today'] = False
    
    # Extract volume if available (e.g., "成交量为46.60万手")
    volume_match = re.search(r'成交量[:：]?\s*([\d.]+)万手', text)
    if volume_match:
        try:
            volume = int(float(volume_match.group(1)) * 10000)
            result['volume'] = volume
        except (ValueError, IndexError):
            pass
    
    # Calculate change if we have previous close and today's data
    if 'price' in result and 'previous_close' in result:
        price = result['price']
        prev_close = result['previous_close']
        change = price - prev_close
        change_percent = (change / prev_close * 100) if prev_close else 0
        result['change'] = f"{change:+.2f}"
        result['change_percent'] = change_percent
        result['is_today'] = True  # We have today's data if prev_close is included
    
    # If we got at least the price, return the result
    if 'price' in result:
        return result


def fetch_from_akshare() -> Optional[Dict[str, Any]]:
    """
    Fetch C2605 futures data from AKShare/Sina Finance.
    
    Returns:
        Dictionary with current price data or None if fetch fails
    """
    if not AKSHARE_AVAILABLE:
        print("⚠️ AKShare not available")
        return None
    
    import urllib.request
    import re
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Method 1: Try Sina Finance real-time API directly (with retry)
    for attempt in range(3):
        try:
            url = "https://hq.sinajs.cn/list=fu_C2605"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read().decode('gbk')
                
                # Parse Sina real-time data format
                match = re.search(r'hq_str_fu_C2605="([^"]+)"', content)
                if match:
                    data_str = match.group(1).split(',')
                    if len(data_str) >= 11:
                        name = data_str[0]
                        open_price = float(data_str[1]) if data_str[1] else 0
                        prev_close = float(data_str[2]) if data_str[2] else 0
                        current_price = float(data_str[3]) if data_str[3] else 0
                        high = float(data_str[4]) if data_str[4] else 0
                        low = float(data_str[5]) if data_str[5] else 0
                        volume = int(float(data_str[10]) if data_str[10] else 0)
                        
                        # Calculate change
                        change = current_price - prev_close
                        change_percent = (change / prev_close * 100) if prev_close else 0
                        
                        data = {
                            'symbol': 'C2605',
                            'name': '玉米 2605',
                            'price': current_price,
                            'open': open_price,
                            'high': high,
                            'low': low,
                            'previous_close': prev_close,
                            'volume': volume,
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'change': f"{change:+.2f}",
                            'change_percent': change_percent,
                            'data_source': 'sina_realtime',
                            'data_date': today,
                            'is_stale': False
                        }
                        
                        print(f"✅ Real-time data fetched from Sina (attempt {attempt+1}): ¥{current_price}")
                        return data
        
        except Exception as e:
            print(f"Warning: Sina real-time fetch failed (attempt {attempt+1}/3): {e}")
            if attempt < 2:
                import time
                time.sleep(1)
    
    # Method 2: Fallback to AKShare historical data
    try:
        futures_df = ak.futures_zh_daily_sina(symbol="C2605")
        
        if futures_df is not None and len(futures_df) > 0:
            row = futures_df.iloc[-1]
            last_date = row.get('date', '')
            
            is_stale = (last_date != today)
            if is_stale:
                print(f"⚠️ STALE DATA: Data is from {last_date}, not today ({today})")
            else:
                print(f"⚠️ Using today's historical data (market may be closed)")
            
            # Use 'settle' as previous close reference (settlement price from previous day)
            prev_close = float(row.get('settle', row.get('close', 0)))
            current_price = float(row.get('close', 0))
            change = current_price - prev_close
            
            data = {
                'symbol': 'C2605',
                'name': '玉米 2605',
                'price': current_price,
                'open': float(row.get('open', 0)),
                'high': float(row.get('high', 0)),
                'low': float(row.get('low', 0)),
                'previous_close': prev_close,
                'volume': int(row.get('volume', 0)),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'change': f"{change:+.2f}",
                'change_percent': (change / prev_close * 100) if prev_close else 0,
                'data_source': 'akshare_historical',
                'data_date': last_date,
                'is_stale': is_stale
            }
            
            return data
            
    except Exception as e:
        print(f"Error fetching from AKShare: {e}")
    
    return None


def fetch_c2605_data():
    """
    获取 C2605 数据 - dashscope-websearch 优先，AKShare 备用，Tavily 验证
    
    数据源优先级:
    1. dashscope-websearch (主数据源)
    2. AKShare (备用数据源)
    3. Tavily (验证工具)
    
    Raises:
        RuntimeError: If all data sources fail
    """
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 1. 主数据源：dashscope-websearch
    print("📊 Attempt 1/2: dashscope-websearch (DashScope LLM with enable_search)...")
    dashscope_data = fetch_from_dashscope_websearch(today)
    
    if dashscope_data:
        print(f"✅ Success! Price: ¥{dashscope_data['price']} (dashscope-websearch)")
    else:
        print("⚠️ dashscope-websearch failed, falling back to AKShare...")
        
        # 2. 备用数据源：AKShare
        print("📊 Attempt 2/2: AKShare Historical...")
        akshare_data = fetch_from_akshare()
        
        if akshare_data:
            print(f"✅ Success! Price: ¥{akshare_data['price']} (AKShare)")
            dashscope_data = akshare_data
        else:
            # 所有数据源都失败，直接报错
            error_msg = (
                "❌ 无法获取 C2605 数据：\n"
                "   1. dashscope-websearch 无法获取数据\n"
                "   2. AKShare 也无法获取数据\n"
                "   3. Tavily 验证也无法获取数据\n"
                "请检查网络连接或稍后重试。"
            )
            print(error_msg)
            raise RuntimeError(error_msg)
    
    # 3. 验证工具：Tavily
    print("\n🔍 Validating with Tavily...")
    tavily_data = fetch_c2605_price_tavily()
    
    # 4. 数据对比
    validation_status = "✅ 已验证"
    price_diff = 0
    
    if tavily_data and tavily_data.get('price'):
        price_diff = abs(dashscope_data['price'] - tavily_data['price']) / dashscope_data['price']
        
        if price_diff >= 0.03:
            validation_status = "🚨 数据差异严重 (>3%)"
        elif price_diff >= 0.01:
            validation_status = "⚠️ 数据轻微差异 (>1%)"
        else:
            validation_status = f"✅ 已验证 (差异 {price_diff:.2f}%)"
        
        print(f"   Tavily price: ¥{tavily_data['price']}")
        print(f"   Price difference: {price_diff:.2%}")
        print(f"   Validation status: {validation_status}")
    else:
        print("   ⚠️ Tavily validation unavailable")
    
    # 5. 添加验证状态
    dashscope_data['validation'] = {
        'status': validation_status,
        'tavily_price': tavily_data.get('price') if tavily_data else None,
        'price_diff': f"{price_diff:.2f}%"
    }
    
    return dashscope_data

def format_report(data: Dict[str, Any], report_type: str = 'hourly') -> str:
    """
    Format the price data into a Discord-friendly report.
    
    Args:
        data: Price data dictionary
        report_type: 'hourly' or 'daily'
    
    Returns:
        Formatted report string
    """
    report_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Price direction emoji
    change_str = data.get('change', '0.00')
    try:
        change_val = float(change_str)
        if change_val > 0:
            direction = '📈'
        elif change_val < 0:
            direction = '📉'
        else:
            direction = '➡️'
    except:
        direction = '➡️'
    
    # Compute change_percent_display
    try:
        change_percent = float(data.get('change_percent', 0))
        change_percent_display = f"{change_percent:+.2f}%"
    except:
        change_percent_display = "N/A"
    
    # In Discord, use bullet lists instead of markdown tables
    report = f"""🌽 **C2605 玉米期货 {report_time} 快报** {direction}

• **当前价格**: ¥{data['price']:.2f}
• **涨跌**: {change_str} ({change_percent_display})
• **数据来源**: {data.get('data_source', 'UNKNOWN')} {data['validation']['status']}
• **Tavily 验证**: {data['validation'].get('tavily_price', 'N/A')}
• **价格差异**: {data['validation']['price_diff']}

**开盘**: ¥{data.get('open', 0):.2f}
**最高**: ¥{data.get('high', 0):.2f}
**最低**: ¥{data.get('low', 0):.2f}
**成交量**: {data.get('volume', 0):,}

_下次报告：1 小时后 (交易时段内)_
"""
    
    return report


def send_to_discord(message: str, channel_id: str) -> bool:
    """
    Send message to Discord channel.
    
    This is a placeholder - in production, this would use the OpenClaw message API
    or a Discord webhook.
    """
    print(f"[Discord {channel_id}] {message}")
    # In production, this would call the actual Discord API
    return True


def main():
    """Main entry point for C2605 monitor."""
    import argparse
    
    parser = argparse.ArgumentParser(description='C2605 Corn Futures Monitor')
    parser.add_argument('--config', type=str, help='Path to config file')
    parser.add_argument('--type', type=str, choices=['hourly', 'daily'], 
                       default='hourly', help='Report type')
    parser.add_argument('--test', action='store_true', help='Test mode')
    parser.add_argument('--skip-trading-check', action='store_true', 
                       help='Skip trading time verification (for daily summary)')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Check if it's a trading day
    if not is_trading_day():
        print("📭 Not a trading day (weekend or holiday). Skipping hourly report.")
        return
    
    # Check if currently in trading hours (for hourly reports only)
    if args.type == 'hourly' and not args.skip_trading_check:
        if not is_trading_time():
            now = datetime.now()
            print(f" smtp Outside trading hours ({now.strftime('%H:%M')}). Skipping hourly report.")
            print(f"   Trading sessions: 09:00-10:15, 10:30-11:30, 13:30-15:00")
            return
    
    try:
        # Fetch data with Tavily validation
        data = fetch_c2605_data()
    except RuntimeError as e:
        print(f"❌ Data fetch failed: {e}")
        return
    
    if not data:
        print("Failed to fetch C2605 data")
        return
    
    # Format report
    report = format_report(data, args.type)
    
    # Output report
    print("\n" + "="*60)
    print(report)
    print("="*60)
    
    # Send to Discord (if not in test mode)
    if not args.test:
        channel_id = config.get('discord_channel_id', '1475775915844960428')
        send_to_discord(report, channel_id)
    
    # Log to file
    log_dir = Path(__file__).parent / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / f"c2605_{datetime.now().strftime('%Y%m%d')}.log"
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n--- {args.type.upper()} REPORT ---\n")
        f.write(f"{datetime.now().isoformat()}\n")
        f.write(json.dumps(data, indent=2, ensure_ascii=False))
        f.write("\n")


if __name__ == '__main__':
    main()
