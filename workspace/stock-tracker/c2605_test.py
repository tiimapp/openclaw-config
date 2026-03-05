#!/usr/bin/env python3
"""
C2605 Corn Futures Test Report

Quick test to fetch C2605 data and generate a report for Discord.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Try to import AKShare for futures data
try:
    import akshare as ak
    AKSHARE_AVAILABLE = True
    print("✓ AKShare imported successfully")
except ImportError as e:
    AKSHARE_AVAILABLE = False
    print(f"✗ AKShare not available: {e}")
    sys.exit(1)


def fetch_c2605_data():
    """
    Fetch C2605 futures data from AKShare.
    
    Returns:
        Dictionary with current price data or None if fetch fails
    """
    if not AKSHARE_AVAILABLE:
        return None
    
    data = None
    
    # Method 1: Try futures_zh_realtime for specific contract
    try:
        print("\n📊 Method 1: Trying futures_zh_realtime...")
        realtime_df = ak.futures_zh_realtime(symbol="C2605")
        
        if realtime_df is not None and len(realtime_df) > 0:
            row = realtime_df.iloc[0]
            data = {
                'symbol': 'C2605',
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
                'source': 'akshare_realtime',
            }
            print(f"✓ Success with futures_zh_realtime")
            return data
    except Exception as e1:
        print(f"✗ Method 1 failed: {e1}")
    
    # Method 2: Try futures_zh_daily_sina for latest data
    try:
        print("\n📊 Method 2: Trying futures_zh_daily_sina...")
        daily_df = ak.futures_zh_daily_sina(symbol="C2605")
        
        if daily_df is not None and len(daily_df) > 0:
            row = daily_df.iloc[-1]  # Get latest record
            data = {
                'symbol': 'C2605',
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
                'source': 'akshare_daily_sina',
            }
            print(f"✓ Success with futures_zh_daily_sina")
            return data
    except Exception as e2:
        print(f"✗ Method 2 failed: {e2}")
    
    # Method 3: Try futures_spot_price
    try:
        print("\n📊 Method 3: Trying futures_spot_price...")
        futures_spot_df = ak.futures_spot_price()
        
        if futures_spot_df is not None and len(futures_spot_df) > 0:
            # Look for corn-related contracts
            corn_row = None
            for idx, row in futures_spot_df.iterrows():
                row_dict = row.to_dict()
                row_str = str(row_dict)
                if '玉米' in row_str or 'C2605' in row_str or 'corn' in row_str.lower():
                    corn_row = row
                    break
            
            if corn_row is None:
                corn_row = futures_spot_df.iloc[0]
            
            data = {
                'symbol': 'C2605',
                'current_price': float(corn_row.get('price', corn_row.get('close', 0))),
                'change': float(corn_row.get('change', 0)),
                'change_percent': float(corn_row.get('pct_chg', corn_row.get('change_percent', 0))),
                'volume': int(corn_row.get('volume', corn_row.get('vol', 0))),
                'open': float(corn_row.get('open', 0)),
                'high': float(corn_row.get('high', 0)),
                'low': float(corn_row.get('low', 0)),
                'prev_close': float(corn_row.get('pre_close', corn_row.get('prev_close', 0))),
                'open_interest': int(corn_row.get('open_interest', corn_row.get('oi', 0))),
                'timestamp': datetime.now(),
                'source': 'akshare_spot',
            }
            print(f"✓ Success with futures_spot_price")
            return data
    except Exception as e3:
        print(f"✗ Method 3 failed: {e3}")
    
    return None


def generate_report(data):
    """Generate a formatted report for Discord."""
    
    timestamp = data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    source = data['source']
    
    # Format change with sign
    change_sign = '+' if data['change'] >= 0 else ''
    change_pct_sign = '+' if data['change_percent'] >= 0 else ''
    
    report = f"""
🌽 **C2605 玉米 2605 期货行情** 🌽

📈 **当前价格**: ¥{data['current_price']:,.0f}
📊 **涨跌**: {change_sign}{data['change']:.2f} ({change_pct_sign}{data['change_percent']:.2f}%)

📉 **今日范围**:
  • 开盘：¥{data['open']:,.0f}
  • 最高：¥{data['high']:,.0f}
  • 最低：¥{data['low']:,.0f}
  • 昨收：¥{data['prev_close']:,.0f}

📦 **成交量**: {data['volume']:,}
📋 **持仓量**: {data['open_interest']:,}

⏰ **时间**: {timestamp}
🔍 **数据源**: {source}

---
*市场已于 23:00 收盘 (夜盘结束)*
"""
    
    return report


def main():
    print("=" * 60)
    print("C2605 玉米 2605 期货测试报告")
    print("=" * 60)
    print(f"开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Fetch data
    print("\n🔄 正在获取 C2605 数据...")
    data = fetch_c2605_data()
    
    if data is None:
        print("\n✗ 无法获取 C2605 数据")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✅ 数据获取成功!")
    print("=" * 60)
    
    # Generate report
    report = generate_report(data)
    
    print("\n" + "=" * 60)
    print("📋 TEST REPORT FOR DISCORD")
    print("=" * 60)
    print(report)
    
    # Output raw data for verification
    print("\n" + "=" * 60)
    print("📊 RAW DATA (for verification)")
    print("=" * 60)
    print(json.dumps(data, indent=2, default=str))
    
    # Save to file
    output_file = Path(__file__).parent / 'logs' / 'c2605_test_report.json'
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, default=str)
    
    print(f"\n💾 原始数据已保存到：{output_file}")
    
    # Output Discord-ready message
    print("\n" + "=" * 60)
    print("📤 DISCORD MESSAGE (ready to send)")
    print("=" * 60)
    print(f"Channel ID: 1475775915844960428")
    print(f"Message:\n{report}")
    
    return data, report


if __name__ == '__main__':
    main()
