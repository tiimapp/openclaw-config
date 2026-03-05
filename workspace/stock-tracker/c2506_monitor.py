#!/usr/bin/env python3
"""
C2506 Corn Futures Monitor

Fetches DCE Corn Futures (C2506 - 玉米 2605 contract) price data
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
        config_path = os.path.join(os.path.dirname(__file__), 'c2506_config.json')
    
    default_config = {
        'symbol': 'C2506',
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
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config: {e}. Using defaults.")
    
    return default_config


def fetch_c2506_data() -> Optional[Dict[str, Any]]:
    """
    Fetch C2506 futures data from AKShare.
    
    Returns:
        Dictionary with current price data or None if fetch fails
    """
    if not AKSHARE_AVAILABLE:
        return generate_mock_data()
    
    try:
        # Fetch real-time futures data from DCE
        # Method 1: Try futures_zh_realtime for specific contract
        try:
            # Get real-time data for DCE corn futures
            realtime_df = ak.futures_zh_realtime(symbol="C2506")
            
            if realtime_df is not None and len(realtime_df) > 0:
                row = realtime_df.iloc[0]
                data = {
                    'symbol': 'C2506',
                    'current_price': float(row.get('price', row.get('current_price', 0))),
                    'change': float(row.get('change', 0)),
                    'change_percent': float(row.get('pct_chg', row.get('change_percent', 0))),
                    'volume': int(row.get('volume', row.get('vol', 0))),
                    'open': float(row.get('open', 0)),
                    'high': float(row.get('high', 0)),
                    'low': float(row.get('low', 0)),
                    'prev_close': float(row.get('pre_close', row.get('prev_close', 0))),
                    'open_interest': int(row.get('open_interest', row.get('oi', 0))),
                    'timestamp': datetime.now(),
                    'source': 'akshare',
                }
                return data
        except Exception as e1:
            print(f"Method 1 (futures_zh_realtime) failed: {e1}")
        
        # Method 2: Try futures_spot_price for commodity prices
        try:
            futures_spot_df = ak.futures_spot_price()
            
            if futures_spot_df is not None and len(futures_spot_df) > 0:
                # Filter for corn-related contracts
                corn_row = None
                for idx, row in futures_spot_df.iterrows():
                    row_str = str(row.to_dict())
                    if '玉米' in row_str or 'C2506' in row_str or 'corn' in row_str.lower():
                        corn_row = row
                        break
                
                if corn_row is None:
                    corn_row = futures_spot_df.iloc[0]
                
                data = {
                    'symbol': 'C2506',
                    'current_price': float(corn_row.get('price', corn_row.get('close', 2450))),
                    'change': float(corn_row.get('change', 0)),
                    'change_percent': float(corn_row.get('pct_chg', corn_row.get('change_percent', 0))),
                    'volume': int(corn_row.get('volume', corn_row.get('vol', 0))),
                    'open': float(corn_row.get('open', 0)),
                    'high': float(corn_row.get('high', 0)),
                    'low': float(corn_row.get('low', 0)),
                    'prev_close': float(corn_row.get('pre_close', corn_row.get('prev_close', 2450))),
                    'open_interest': int(corn_row.get('open_interest', corn_row.get('oi', 0))),
                    'timestamp': datetime.now(),
                    'source': 'akshare',
                }
                return data
        except Exception as e2:
            print(f"Method 2 (futures_spot_price) failed: {e2}")
        
        # Method 3: Try futures_zh_daily_sina for latest data
        try:
            daily_df = ak.futures_zh_daily_sina(symbol="C2506")
            
            if daily_df is not None and len(daily_df) > 0:
                row = daily_df.iloc[-1]  # Get latest record
                data = {
                    'symbol': 'C2506',
                    'current_price': float(row.get('close', 0)),
                    'change': float(row.get('change', 0)),
                    'change_percent': float(row.get('pct_chg', row.get('change_percent', 0))),
                    'volume': int(row.get('volume', 0)),
                    'open': float(row.get('open', 0)),
                    'high': float(row.get('high', 0)),
                    'low': float(row.get('low', 0)),
                    'prev_close': float(row.get('pre_close', row.get('prev_close', 0))),
                    'open_interest': int(row.get('open_interest', 0)),
                    'timestamp': datetime.now(),
                    'source': 'akshare',
                }
                return data
        except Exception as e3:
            print(f"Method 3 (futures_zh_daily_sina) failed: {e3}")
            
    except Exception as e:
        print(f"Error fetching data from AKShare: {e}")
    
    # Fallback to mock data
    return generate_mock_data()


def generate_mock_data() -> Dict[str, Any]:
    """Generate mock data for testing when AKShare is unavailable."""
    import random
    
    base_price = 2450.0  # Approximate corn futures price
    price_change = random.uniform(-30, 30)
    current_price = base_price + price_change
    
    return {
        'symbol': 'C2506',
        'current_price': round(current_price, 0),
        'change': round(price_change, 2),
        'change_percent': round((price_change / base_price) * 100, 2),
        'volume': random.randint(50000, 200000),
        'open': round(base_price + random.uniform(-20, 20), 0),
        'high': round(current_price + abs(price_change) + random.uniform(0, 10), 0),
        'low': round(current_price - abs(price_change) - random.uniform(0, 10), 0),
        'prev_close': base_price,
        'open_interest': random.randint(100000, 500000),
        'timestamp': datetime.now(),
        'source': 'mock',
    }


def fetch_daily_history(days: int = 30) -> Optional[list]:
    """
    Fetch historical daily data for C2506.
    
    Args:
        days: Number of days of history to fetch
    
    Returns:
        List of daily records or None
    """
    if not AKSHARE_AVAILABLE:
        return generate_mock_history(days)
    
    try:
        # Method 1: Try futures_zh_daily_sina
        try:
            futures_df = ak.futures_zh_daily_sina(symbol="C2506")
            
            if futures_df is not None and len(futures_df) > 0:
                recent_df = futures_df.tail(days)
                
                history = []
                for idx, row in recent_df.iterrows():
                    history.append({
                        'date': str(row.get('date', row.get('day', ''))),
                        'open': float(row.get('open', 0)),
                        'high': float(row.get('high', 0)),
                        'low': float(row.get('low', 0)),
                        'close': float(row.get('close', 0)),
                        'volume': int(row.get('volume', 0)),
                        'open_interest': int(row.get('open_interest', 0)),
                    })
                return history
        except Exception as e1:
            print(f"Historical method 1 failed: {e1}")
        
        # Method 2: Try futures_zh_hist for historical data
        try:
            hist_df = ak.futures_zh_hist(symbol="C2506", period="daily", adjust="qfq")
            
            if hist_df is not None and len(hist_df) > 0:
                recent_df = hist_df.tail(days)
                
                history = []
                for idx, row in recent_df.iterrows():
                    history.append({
                        'date': str(row.get('date', row.get('datetime', ''))),
                        'open': float(row.get('open', 0)),
                        'high': float(row.get('high', 0)),
                        'low': float(row.get('low', 0)),
                        'close': float(row.get('close', 0)),
                        'volume': int(row.get('volume', 0)),
                        'open_interest': int(row.get('open_interest', 0)),
                    })
                return history
        except Exception as e2:
            print(f"Historical method 2 failed: {e2}")
            
    except Exception as e:
        print(f"Error fetching historical data: {e}")
    
    return generate_mock_history(days)


def generate_mock_history(days: int = 30) -> list:
    """Generate mock historical data for testing."""
    import random
    
    history = []
    base_price = 2450.0
    current_date = datetime.now()
    
    for i in range(days):
        date = current_date - timedelta(days=i)
        if date.weekday() < 5:  # Only weekdays
            daily_change = random.uniform(-40, 40)
            open_price = base_price + random.uniform(-20, 20)
            close_price = open_price + daily_change
            high_price = max(open_price, close_price) + random.uniform(0, 15)
            low_price = min(open_price, close_price) - random.uniform(0, 15)
            
            history.append({
                'date': date.strftime('%Y-%m-%d'),
                'open': round(open_price, 0),
                'high': round(high_price, 0),
                'low': round(low_price, 0),
                'close': round(close_price, 0),
                'volume': random.randint(100000, 300000),
                'open_interest': random.randint(100000, 500000),
            })
    
    return history


def format_hourly_report(data: Dict[str, Any], config: Dict[str, Any]) -> str:
    """
    Format hourly trading report.
    
    Args:
        data: Current price data
        config: Configuration dictionary
    
    Returns:
        Formatted report string for Discord
    """
    symbol = config.get('symbol', 'C2506')
    symbol_name = config.get('symbol_name', '玉米 2605')
    
    # Price change indicator
    if data['change'] > 0:
        change_indicator = "📈"
        change_sign = "+"
    elif data['change'] < 0:
        change_indicator = "📉"
        change_sign = ""
    else:
        change_indicator = "➡️"
        change_sign = ""
    
    report = f"""
**🌽 {symbol_name} ({symbol}) - 盘中快报**

**当前价格**: ¥{data['current_price']:,.0f} {change_indicator}
**涨跌**: {change_sign}{data['change']:.2f} ({change_sign}{data['change_percent']:.2f}%)

**今日行情**:
• 开盘：¥{data['open']:,.0f}
• 最高：¥{data['high']:,.0f}
• 最低：¥{data['low']:,.0f}
• 昨结：¥{data['prev_close']:,.0f}

**成交数据**:
• 成交量：{data['volume']:,} 手
• 持仓量：{data['open_interest']:,} 手

**更新时间**: {data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
**数据来源**: {data['source'].upper()}
""".strip()
    
    return report


def format_daily_summary(data: Dict[str, Any], history: list, config: Dict[str, Any]) -> str:
    """
    Format daily summary report.
    
    Args:
        data: Current price data (day's close)
        history: Historical daily data
        config: Configuration dictionary
    
    Returns:
        Formatted daily summary string
    """
    symbol = config.get('symbol', 'C2506')
    symbol_name = config.get('symbol_name', '玉米 2605')
    
    # Price change indicator
    if data['change'] > 0:
        change_indicator = "📈"
        change_sign = "+"
    elif data['change'] < 0:
        change_indicator = "📉"
        change_sign = ""
    else:
        change_indicator = "➡️"
        change_sign = ""
    
    # Calculate some stats from history
    if len(history) >= 5:
        recent_prices = [h['close'] for h in history[:5]]
        avg_5day = sum(recent_prices) / len(recent_prices)
        high_5day = max(recent_prices)
        low_5day = min(recent_prices)
    else:
        avg_5day = data['current_price']
        high_5day = data['high']
        low_5day = data['low']
    
    # Daily K-line summary
    close_price = data.get('close', data.get('current_price', data['open']))
    if close_price > data['open']:
        kline_type = "阳线 (Bullish)"
        kline_emoji = "🟢"
    elif close_price < data['open']:
        kline_type = "阴线 (Bearish)"
        kline_emoji = "🔴"
    else:
        kline_type = "十字星 (Doji)"
        kline_emoji = "⚪"
    
    report = f"""
**🌽 {symbol_name} ({symbol}) - 每日总结**
**日期**: {data['timestamp'].strftime('%Y年%m月%d日 %A')}

**今日收盘**: ¥{data['current_price']:,.0f} {change_indicator}
**日涨跌**: {change_sign}{data['change']:.2f} ({change_sign}{data['change_percent']:.2f}%)

**K 线形态**: {kline_emoji} {kline_type}
**价格区间**: ¥{data['low']:,.0f} - ¥{data['high']:,.0f}

**今日行情**:
• 开盘：¥{data['open']:,.0f}
• 最高：¥{data['high']:,.0f}
• 最低：¥{data['low']:,.0f}
• 收盘：¥{data['current_price']:,.0f}
• 昨结：¥{data['prev_close']:,.0f}

**成交数据**:
• 成交量：{data['volume']:,} 手
• 持仓量：{data['open_interest']:,} 手
• 持仓变化：{data.get('oi_change', 'N/A')}

**近期走势** (5 日):
• 平均价格：¥{avg_5day:,.0f}
• 最高：¥{high_5day:,.0f}
• 最低：¥{low_5day:,.0f}

**更新时间**: {data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}
**数据来源**: {data['source'].upper()}
""".strip()
    
    return report


def format_non_trading_message(config: Dict[str, Any], status: dict) -> str:
    """
    Format message for non-trading hours.
    
    Args:
        config: Configuration dictionary
        status: Trading status dictionary
    
    Returns:
        Formatted message string
    """
    symbol = config.get('symbol', 'C2506')
    symbol_name = config.get('symbol_name', '玉米 2605')
    
    now = datetime.now()
    
    message = f"""
**🌽 {symbol_name} ({symbol}) - 市场状态**

**当前状态**: {'休市中' if not status['is_trading_time'] else '交易中'}
**今日是否交易日**: {'是' if status['is_trading_day'] else '否'}
""".strip()
    
    if status['next_trading_time']:
        next_time = status['next_trading_time']
        message += f"\n\n**下次开盘**: {next_time.strftime('%Y-%m-%d %H:%M')} ({next_time.strftime('%A')})"
        
        if status['time_to_next']:
            hours, remainder = divmod(int(status['time_to_next'].total_seconds()), 3600)
            minutes, _ = divmod(remainder, 60)
            if hours > 0:
                message += f" (还有 {hours}小时{minutes}分钟)"
            else:
                message += f" (还有 {minutes}分钟)"
    
    message += f"""

**交易时间** (Asia/Shanghai UTC+8):
• 上午：09:00 - 10:15, 10:30 - 11:30
• 下午：13:30 - 15:00
• 无夜盘

**更新时间**: {now.strftime('%Y-%m-%d %H:%M:%S')}
""".strip()
    
    return message


def send_to_discord(message: str, channel_id: str) -> bool:
    """
    Send message to Discord channel.
    
    This is a placeholder - in production, integrate with Discord bot API
    or use the OpenClaw message tool.
    
    Args:
        message: Message to send
        channel_id: Discord channel ID
    
    Returns:
        True if sent successfully
    """
    # For now, just print the message
    # In production, this would call Discord API
    print(f"\n{'='*60}")
    print(f"DISCORD MESSAGE (Channel: {channel_id})")
    print('='*60)
    print(message)
    print('='*60)
    
    # TODO: Implement actual Discord integration
    # Options:
    # 1. Use Discord webhook
    # 2. Use Discord bot token
    # 3. Use OpenClaw message tool
    
    return True


def run_monitor(mode: Optional[str] = None, config_path: Optional[str] = None):
    """
    Main monitoring function.
    
    Args:
        mode: 'hourly', 'daily', or 'auto' (default: auto)
        config_path: Path to config file
    """
    # Load configuration
    config = load_config(config_path)
    
    # Get trading status
    status = get_trading_status(config_path=config_path)
    
    print(f"C2506 Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Trading day: {status['is_trading_day']}")
    print(f"Trading time: {status['is_trading_time']}")
    
    # Determine report type
    if mode is None:
        # Auto mode: choose based on trading status
        if status['is_trading_time']:
            mode = 'hourly'
        elif status['is_trading_day'] and status['time_since_last']:
            # Check if market just closed (within 30 minutes)
            if status['time_since_last'].total_seconds() < 1800:
                mode = 'daily'
            else:
                mode = 'status'
        else:
            mode = 'status'
    
    print(f"Report mode: {mode}")
    
    # Fetch data
    data = fetch_c2506_data()
    
    if not data:
        print("Error: Could not fetch price data")
        return
    
    # Generate and send report
    channel_id = config.get('discord_channel_id', '')
    
    if mode == 'hourly':
        report = format_hourly_report(data, config)
        print("\nGenerating hourly report...")
    elif mode == 'daily':
        history = fetch_daily_history(30)
        report = format_daily_summary(data, history, config)
        print("\nGenerating daily summary...")
    else:
        report = format_non_trading_message(config, status)
        print("\nGenerating status message...")
    
    # Send to Discord
    if channel_id:
        send_to_discord(report, channel_id)
    else:
        print("\nNo Discord channel configured. Output only.")
        print(report)
    
    return report


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='C2506 Corn Futures Monitor')
    parser.add_argument('--mode', choices=['hourly', 'daily', 'auto', 'status'],
                       default='auto', help='Report mode')
    parser.add_argument('--config', help='Path to config file')
    parser.add_argument('--test', action='store_true', help='Run in test mode')
    
    args = parser.parse_args()
    
    if args.test:
        print("Running in test mode...")
        print("\n" + "="*60)
        print("TEST: Trading Time Checker")
        print("="*60)
        
        status = get_trading_status()
        print(f"Is trading day: {status['is_trading_day']}")
        print(f"Is trading time: {status['is_trading_time']}")
        
        print("\n" + "="*60)
        print("TEST: Data Fetch")
        print("="*60)
        data = fetch_c2506_data()
        if data:
            print(f"Symbol: {data['symbol']}")
            print(f"Current Price: ¥{data['current_price']:,.0f}")
            print(f"Change: {data['change']:.2f} ({data['change_percent']:.2f}%)")
            print(f"Source: {data['source']}")
        
        print("\n" + "="*60)
        print("TEST: Full Monitor Run")
        print("="*60)
    
    run_monitor(mode=args.mode, config_path=args.config)
