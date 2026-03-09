#!/usr/bin/env python3
"""
Trading Time Checker for DCE Corn Futures (C2506)

DCE Corn Futures Trading Hours (Asia/Shanghai UTC+8):
- Day session: 09:00-10:15, 10:30-11:30, 13:30-15:00
- No night session for corn
- Monday-Friday only (exclude weekends & Chinese holidays)
"""

from datetime import datetime, time, timedelta
from typing import Optional, Tuple
import json
import os

# Chinese holidays 2026 (official public holidays - no trading)
# Source: Chinese State Council announcements
CHINESE_HOLIDAYS_2026 = {
    # New Year's Day
    "2026-01-01": "New Year's Day",
    "2026-01-02": "New Year's Holiday",
    "2026-01-03": "New Year's Holiday",
    
    # Spring Festival (Chinese New Year)
    "2026-02-17": "Spring Festival Eve",
    "2026-02-18": "Spring Festival",
    "2026-02-19": "Spring Festival",
    "2026-02-20": "Spring Festival",
    "2026-02-21": "Spring Festival",
    "2026-02-22": "Spring Festival",
    "2026-02-23": "Spring Festival",
    
    # Qingming Festival (Tomb Sweeping Day)
    "2026-04-05": "Qingming Festival",
    "2026-04-06": "Qingming Holiday",
    "2026-04-07": "Qingming Holiday",
    
    # Labor Day
    "2026-05-01": "Labor Day",
    "2026-05-02": "Labor Day Holiday",
    "2026-05-03": "Labor Day Holiday",
    "2026-05-04": "Labor Day Holiday",
    "2026-05-05": "Labor Day Holiday",
    
    # Dragon Boat Festival
    "2026-06-19": "Dragon Boat Festival",
    "2026-06-20": "Dragon Boat Holiday",
    "2026-06-21": "Dragon Boat Holiday",
    
    # Mid-Autumn Festival
    "2026-09-25": "Mid-Autumn Festival",
    "2026-09-26": "Mid-Autumn Holiday",
    "2026-09-27": "Mid-Autumn Holiday",
    
    # National Day (Golden Week)
    "2026-10-01": "National Day",
    "2026-10-02": "National Day Holiday",
    "2026-10-03": "National Day Holiday",
    "2026-10-04": "National Day Holiday",
    "2026-10-05": "National Day Holiday",
    "2026-10-06": "National Day Holiday",
    "2026-10-07": "National Day Holiday",
    "2026-10-08": "National Day Holiday",
}

# Trading sessions (Asia/Shanghai timezone)
# Note: End times include a 5-minute buffer for report generation after market close
# UPDATED 2026-03-09: Added night session based on user feedback and latest search results
TRADING_SESSIONS = [
    (time(9, 0), time(10, 20)),    # Morning session 1 + 5min buffer
    (time(10, 30), time(11, 35)),  # Morning session 2 + 5min buffer
    (time(13, 30), time(15, 5)),   # Afternoon session + 5min buffer (for closing price)
    (time(21, 0), time(23, 5)),    # Night session + 5min buffer (21:00-23:00)
]


def load_custom_holidays(config_path: Optional[str] = None) -> dict:
    """Load custom holidays from config file if available."""
    holidays = CHINESE_HOLIDAYS_2026.copy()
    
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                custom_holidays = config.get('custom_holidays', {})
                holidays.update(custom_holidays)
        except (json.JSONDecodeError, IOError):
            pass
    
    return holidays


def is_trading_day(date: Optional[datetime] = None, config_path: Optional[str] = None) -> bool:
    """
    Check if a given date is a trading day.
    
    Args:
        date: Date to check (defaults to current date/time)
        config_path: Optional path to config file with custom holidays
    
    Returns:
        True if it's a trading day (Mon-Fri, not a holiday)
    """
    if date is None:
        date = datetime.now()
    
    # Check if weekend (Monday=0, Sunday=6)
    if date.weekday() >= 5:
        return False
    
    # Check if holiday
    date_str = date.strftime('%Y-%m-%d')
    holidays = load_custom_holidays(config_path)
    
    if date_str in holidays:
        return False
    
    return True


def is_trading_time(now: Optional[datetime] = None, config_path: Optional[str] = None) -> bool:
    """
    Check if current time is within trading hours.
    
    Args:
        now: Current datetime (defaults to now)
        config_path: Optional path to config file
    
    Returns:
        True if currently in trading hours
    """
    if now is None:
        now = datetime.now()
    
    # First check if it's a trading day
    if not is_trading_day(now, config_path):
        return False
    
    # Check if within any trading session
    current_time = now.time()
    
    for session_start, session_end in TRADING_SESSIONS:
        if session_start <= current_time <= session_end:
            return True
    
    return False


def get_current_session(now: Optional[datetime] = None) -> Optional[Tuple[time, time]]:
    """
    Get the current trading session if in trading hours.
    
    Args:
        now: Current datetime
    
    Returns:
        Tuple of (session_start, session_end) or None if not in trading hours
    """
    if now is None:
        now = datetime.now()
    
    current_time = now.time()
    
    for session_start, session_end in TRADING_SESSIONS:
        if session_start <= current_time <= session_end:
            return (session_start, session_end)
    
    return None


def get_next_trading_time(now: Optional[datetime] = None, config_path: Optional[str] = None) -> Optional[datetime]:
    """
    Get the next trading session start time.
    
    Args:
        now: Current datetime (defaults to now)
        config_path: Optional path to config file
    
    Returns:
        Datetime of next trading session start, or None if can't determine
    """
    if now is None:
        now = datetime.now()
    
    # Start from current time
    check_date = now.replace(second=0, microsecond=0)
    
    # Check up to 14 days ahead (covers holidays + weekends)
    for _ in range(14):
        # If it's a trading day, check sessions
        if is_trading_day(check_date, config_path):
            current_time = check_date.time()
            
            for session_start, session_end in TRADING_SESSIONS:
                session_datetime = check_date.replace(
                    hour=session_start.hour,
                    minute=session_start.minute,
                    second=0,
                    microsecond=0
                )
                
                # If session hasn't started yet today
                if session_datetime > now:
                    return session_datetime
            
            # All sessions for today have passed, move to next day
            check_date = check_date + timedelta(days=1)
            continue
        else:
            # Not a trading day, move to next day
            check_date = check_date + timedelta(days=1)
    
    return None


def get_previous_trading_time(now: Optional[datetime] = None, config_path: Optional[str] = None) -> Optional[datetime]:
    """
    Get the previous trading session end time.
    
    Args:
        now: Current datetime
        config_path: Optional path to config file
    
    Returns:
        Datetime of previous trading session end
    """
    if now is None:
        now = datetime.now()
    
    # Start from current time
    check_date = now.replace(second=0, microsecond=0)
    
    # Check up to 14 days back
    for _ in range(14):
        if is_trading_day(check_date, config_path):
            current_time = check_date.time()
            
            # Check sessions in reverse order
            for session_start, session_end in reversed(TRADING_SESSIONS):
                session_datetime = check_date.replace(
                    hour=session_end.hour,
                    minute=session_end.minute,
                    second=0,
                    microsecond=0
                )
                
                if session_datetime < now:
                    return session_datetime
            
            # All sessions for today are in the future, go to previous day
            check_date = check_date - timedelta(days=1)
            continue
        else:
            check_date = check_date - timedelta(days=1)
    
    return None


def get_time_to_next_session(now: Optional[datetime] = None, config_path: Optional[str] = None) -> Optional[timedelta]:
    """
    Get time remaining until next trading session starts.
    
    Args:
        now: Current datetime
        config_path: Optional path to config file
    
    Returns:
        Timedelta until next session, or None
    """
    next_time = get_next_trading_time(now, config_path)
    if next_time is None:
        return None
    
    if now is None:
        now = datetime.now()
    
    return next_time - now


def get_time_since_last_session(now: Optional[datetime] = None, config_path: Optional[str] = None) -> Optional[timedelta]:
    """
    Get time elapsed since last trading session ended.
    
    Args:
        now: Current datetime
        config_path: Optional path to config file
    
    Returns:
        Timedelta since last session ended
    """
    prev_time = get_previous_trading_time(now, config_path)
    if prev_time is None:
        return None
    
    if now is None:
        now = datetime.now()
    
    return now - prev_time


def get_trading_status(now: Optional[datetime] = None, config_path: Optional[str] = None) -> dict:
    """
    Get comprehensive trading status.
    
    Args:
        now: Current datetime
        config_path: Optional path to config file
    
    Returns:
        Dictionary with trading status information
    """
    if now is None:
        now = datetime.now()
    
    status = {
        'is_trading_day': is_trading_day(now, config_path),
        'is_trading_time': is_trading_time(now, config_path),
        'current_session': None,
        'next_trading_time': None,
        'previous_trading_time': None,
        'time_to_next': None,
        'time_since_last': None,
    }
    
    if status['is_trading_time']:
        status['current_session'] = get_current_session(now)
    
    next_time = get_next_trading_time(now, config_path)
    if next_time:
        status['next_trading_time'] = next_time
        status['time_to_next'] = get_time_to_next_session(now, config_path)
    
    prev_time = get_previous_trading_time(now, config_path)
    if prev_time:
        status['previous_trading_time'] = prev_time
        status['time_since_last'] = get_time_since_last_session(now, config_path)
    
    return status


if __name__ == '__main__':
    # Test the module
    print("Trading Time Checker Test")
    print("=" * 50)
    
    now = datetime.now()
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Day of week: {now.strftime('%A')}")
    
    status = get_trading_status(now)
    print(f"\nIs trading day: {status['is_trading_day']}")
    print(f"Is trading time: {status['is_trading_time']}")
    
    if status['current_session']:
        start, end = status['current_session']
        print(f"Current session: {start.strftime('%H:%M')} - {end.strftime('%H:%M')}")
    
    if status['next_trading_time']:
        print(f"Next trading time: {status['next_trading_time'].strftime('%Y-%m-%d %H:%M')}")
    
    if status['time_to_next']:
        hours, remainder = divmod(int(status['time_to_next'].total_seconds()), 3600)
        minutes, _ = divmod(remainder, 60)
        print(f"Time to next session: {hours}h {minutes}m")
