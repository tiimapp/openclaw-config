#!/usr/bin/env python3
"""
C2605 Corn Futures Hourly Monitor
Generates hourly reports for C2605 (May 2026 Corn Futures) from DCE
"""

import sys
import os
import json
import logging
from datetime import datetime, timezone
import argparse

# Add stock-tracker to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.hybrid_fetcher import fetch_price_data, DATA_DELAY_WARNING
from src.reporter import format_report

def main():
    parser = argparse.ArgumentParser(description='C2605 Corn Futures Monitor')
    parser.add_argument('--type', choices=['hourly', 'daily'], default='hourly',
                       help='Report type: hourly or daily')
    args = parser.parse_args()
    
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        # Fetch C2605 futures data
        symbol = "C2605"
        logging.info(f"Fetching {symbol} corn futures data...")
        
        price_data = fetch_price_data(symbol, symbol_type="futures", retry=3)
        
        if not price_data:
            print(f"❌ Failed to fetch {symbol} data")
            return 1
            
        # Add metadata
        price_data['symbol'] = symbol
        price_data['name'] = '玉米2605 (May 2026 Corn Futures)'
        price_data['exchange'] = 'DCE'
        price_data['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        price_data['data_delay_warning'] = DATA_DELAY_WARNING
        
        # Format report
        if args.type == 'hourly':
            report = format_hourly_report(price_data)
        else:
            report = format_daily_report(price_data)
            
        print(report)
        return 0
        
    except Exception as e:
        logging.error(f"Error in C2605 monitor: {e}")
        print(f"❌ Error: {e}")
        return 1

def format_hourly_report(data):
    """Format hourly report for Discord"""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    # Extract key fields
    price = data.get('current_price', 'N/A')
    change_pct = data.get('change_pct', 'N/A')
    high = data.get('high', 'N/A')
    low = data.get('low', 'N/A')
    volume = data.get('volume', 'N/A')
    
    report = f"""🌽 **C2605 玉米期货 - 小时报告**
📅 {current_time} (Asia/Shanghai)

💰 **当前价格**: {price}
📈 **涨跌幅**: {change_pct}%
📊 **今日高/低**: {high} / {low}
📦 **成交量**: {volume}

📍 **交易所**: 大连商品交易所 (DCE)
{data.get('data_delay_warning', '')}

#corn_futures #C2605 #commodities"""
    
    return report

def format_daily_report(data):
    """Format daily summary report"""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    open_price = data.get('open', 'N/A')
    high = data.get('high', 'N/A')
    low = data.get('low', 'N/A')
    close = data.get('current_price', 'N/A')
    volume = data.get('volume', 'N/A')
    
    report = f"""🌽 **C2605 玉米期货 - 日报**
📅 {current_time} (Asia/Shanghai)

📊 **OHLC**:
- 开盘: {open_price}
- 最高: {high}
- 最低: {low}
- 收盘: {close}

📦 **成交量**: {volume}
📍 **交易所**: 大连商品交易所 (DCE)
{data.get('data_delay_warning', '')}

#corn_futures #C2605 #daily_report #commodities"""
    
    return report

if __name__ == "__main__":
    sys.exit(main())
