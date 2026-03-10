#!/usr/bin/env python3
"""
C2605 Corn Futures Monitor

Fetches DCE Corn Futures (C2605 - 玉米 2605 contract) price data
and generates reports for Discord.

Trading Hours (Asia/Shanghai UTC+8):
- Day session: 09:00-10:15, 10:30-11:30, 13:30-15:00
- No night session for corn
- Monday-Friday only
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

# Try to import AKShare for futures data
try:
    import akshare as ak
    AKSHARE_AVAILABLE = True
except ImportError:
    AKSHARE_AVAILABLE = False
    print("Warning: AKShare not available. Using mock data for testing.")


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


def fetch_c2605_data() -> Optional[Dict[str, Any]]:
    """
    Fetch C2605 futures REAL-TIME data from Sina Finance.
    
    Returns:
        Dictionary with current price data or None if fetch fails
    """
    import urllib.request
    import re
    
    today = datetime.now().strftime('%Y-%m-%d')
    data_source = 'unknown'
    data_date = None
    is_stale = False
    
    # Method 1: Try Sina Finance real-time API directly (with retry)
    # Sina real-time URL for DCE futures: https://hq.sinajs.cn/list=fu_C2605
    for attempt in range(3):
        try:
            url = "https://hq.sinajs.cn/list=fu_C2605"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read().decode('gbk')
                
                # Parse Sina real-time data format:
                # var hq_str_fu_C2605="C2605,open,prev_close,current_price,high,low,buy_price,sell_price,..."
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
                            'current_price': current_price,
                            'open': open_price,
                            'high': high,
                            'low': low,
                            'previous_close': prev_close,
                            'volume': volume,
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'change': change,
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
                time.sleep(1)  # Wait 1 second before retry
    
    # Method 2: Fallback to AKShare historical data (with date validation)
    if AKSHARE_AVAILABLE:
        try:
            futures_df = ak.futures_zh_daily_sina(symbol="C2605")
            
            if futures_df is not None and len(futures_df) > 0:
                row = futures_df.iloc[-1]
                last_date = row.get('date', '')
                
                # Check if data is from today
                if last_date == today:
                    print(f"⚠️ Using today's historical data (market may be closed)")
                    is_stale = False
                else:
                    print(f"⚠️ STALE DATA: Data is from {last_date}, not today ({today})")
                    is_stale = True
                
                data = {
                    'symbol': 'C2605',
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
                
                # Calculate change if we have previous close
                if 'pre_close' in row:
                    prev_close = float(row.get('pre_close', data['current_price']))
                    data['previous_close'] = prev_close
                    data['change'] = data['current_price'] - prev_close
                    data['change_percent'] = (data['change'] / prev_close * 100) if prev_close else 0
                
                return data
                
        except Exception as e:
            print(f"Error fetching from AKShare: {e}")
    
    # Method 3: Fallback to mock data
    print("⚠️ Using mock data (all data sources failed)")
    data = generate_mock_data()
    data['data_source'] = 'mock'
    data['data_date'] = today
    data['is_stale'] = False
    return data


def generate_mock_data() -> Dict[str, Any]:
    """Generate mock data for testing when AKShare is unavailable."""
    import random
    base_price = 2450.0
    return {
        'symbol': 'C2605',
        'name': '玉米 2605',
        'current_price': base_price + random.uniform(-20, 20),
        'open': base_price + random.uniform(-10, 10),
        'high': base_price + random.uniform(10, 30),
        'low': base_price + random.uniform(-30, -10),
        'previous_close': base_price,
        'volume': random.randint(10000, 100000),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'change': random.uniform(-15, 15),
        'change_percent': random.uniform(-0.6, 0.6),
    }


def format_report(data: Dict[str, Any], report_type: str = 'hourly') -> str:
    """
    Format the price data into a Discord-friendly report.
    
    Args:
        data: Price data dictionary
        report_type: 'hourly' or 'daily'
    
    Returns:
        Formatted report string
    """
    symbol = data.get('symbol', 'C2605')
    name = data.get('name', '玉米 2605')
    price = data.get('current_price', 0)
    change = data.get('change', 0)
    change_pct = data.get('change_percent', 0)
    is_stale = data.get('is_stale', False)
    data_date = data.get('data_date', '')
    data_source = data.get('data_source', 'unknown')
    
    # Price direction emoji
    if change > 0:
        direction = '📈'
        color = 'green'
    elif change < 0:
        direction = '📉'
        color = 'red'
    else:
        direction = '➡️'
        color = 'gray'
    
    timestamp = data.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # Stale data warning
    stale_warning = ""
    if is_stale and data_date:
        today = datetime.now().strftime('%Y-%m-%d')
        stale_warning = f"\n⚠️ **数据延迟:** 最新可用数据为 {data_date} (非实时)\n"
    
    if report_type == 'hourly':
        report = f"""🌽 **C2605 玉米期货 实时快报** {direction}
{stale_warning}
**合约:** {name} ({symbol})
**当前价格:** ¥{price:.2f}
**涨跌:** {change:+.2f} ({change_pct:+.2f}%)
**开盘:** ¥{data.get('open', 0):.2f}
**最高:** ¥{data.get('high', 0):.2f}
**最低:** ¥{data.get('low', 0):.2f}
**成交量:** {data.get('volume', 0):,}

**更新时间:** {timestamp}
**数据来源:** {data_source}

_下次报告：1 小时后 (交易时段内)_
"""
    else:  # daily summary
        report = f"""🌽 **C2605 玉米期货 每日总结** {direction}
{stale_warning}
**合约:** {name} ({symbol})
**收盘价:** ¥{price:.2f}
**日涨跌:** {change:+.2f} ({change_pct:+.2f}%)
**今日区间:** ¥{data.get('low', 0):.2f} - ¥{data.get('high', 0):.2f}
**成交量:** {data.get('volume', 0):,}

**交易日期:** {timestamp.split()[0]}
**数据来源:** {data_source}

_明日报告：09:00 (开盘后)_
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
            print(f"📭 Outside trading hours ({now.strftime('%H:%M')}). Skipping hourly report.")
            print(f"   Trading sessions: 09:00-10:15, 10:30-11:30, 13:30-15:00")
            return
    
    # Fetch data
    data = fetch_c2605_data()
    if not data:
        print("Failed to fetch C2605 data")
        return
    
    # Format report
    report = format_report(data, args.type)
    
    # Output report
    print(report)
    
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
        f.write(json.dumps(data, indent=2))
        f.write("\n")


if __name__ == '__main__':
    main()
