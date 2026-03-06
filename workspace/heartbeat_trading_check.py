#!/usr/bin/env python3
"""
Heartbeat Trading Day Verifier

Checks if today's trading day verification has been completed.
If not, runs the verification and updates the state file.

Usage:
    python3 heartbeat_trading_check.py [--force]

Returns:
    - Exit code 0: Verification complete (is_trading_day in state)
    - Exit code 1: Error occurred
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# State file location
STATE_FILE = Path(__file__).parent / 'memory' / 'heartbeat-state.json'
TRADING_CHECKER = Path(__file__).parent / 'stock-tracker' / 'trading_time_checker.py'


def load_state() -> dict:
    """Load heartbeat state from JSON file."""
    default_state = {
        "lastChecks": {
            "trading_day_verify": None,
            "is_trading_day": None,
        },
        "reportSchedule": {
            "ashare_daily": None,
            "c2605_hourly": None,
            "c2605_daily": None,
        }
    }
    
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                state = json.load(f)
                # Merge with defaults
                for key, value in default_state.items():
                    if key not in state:
                        state[key] = value
                    elif isinstance(value, dict):
                        for subkey, subvalue in value.items():
                            if subkey not in state[key]:
                                state[key][subkey] = subvalue
                return state
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load state: {e}")
    
    return default_state


def save_state(state: dict):
    """Save heartbeat state to JSON file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def is_already_verified_today(state: dict) -> bool:
    """Check if trading day verification was already done today."""
    last_verify = state.get('lastChecks', {}).get('trading_day_verify')
    
    if not last_verify:
        return False
    
    today = datetime.now().strftime('%Y-%m-%d')
    return last_verify == today


def run_trading_check() -> bool:
    """
    Run the trading time checker to determine if today is a trading day.
    
    Returns:
        True if it's a trading day, False otherwise
    """
    try:
        # Import the trading time checker
        sys.path.insert(0, str(TRADING_CHECKER.parent))
        from trading_time_checker import is_trading_day, is_trading_time
        
        # Check if today is a trading day
        trading_day = is_trading_day()
        
        return trading_day
        
    except Exception as e:
        print(f"Error running trading check: {e}")
        # Default to False on error (safer to skip reports)
        return False


def update_report_schedule(state: dict, is_trading: bool):
    """Update report schedule based on trading day status."""
    if 'reportSchedule' not in state:
        state['reportSchedule'] = {}
    
    if is_trading:
        # Enable all reports
        state['reportSchedule']['ashare_daily'] = '15:30'
        state['reportSchedule']['c2605_hourly'] = '09:00,10:00,11:00,14:00,15:00'
        state['reportSchedule']['c2605_daily'] = '15:30'
    else:
        # Disable all reports
        state['reportSchedule']['ashare_daily'] = None
        state['reportSchedule']['c2605_hourly'] = None
        state['reportSchedule']['c2605_daily'] = None
    
    return state


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Heartbeat Trading Day Verifier')
    parser.add_argument('--force', action='store_true', 
                       help='Force re-verification even if already done today')
    parser.add_argument('--json', action='store_true',
                       help='Output result as JSON')
    
    args = parser.parse_args()
    
    # Load current state
    state = load_state()
    
    # Check if already verified today
    if not args.force and is_already_verified_today(state):
        result = {
            'status': 'already_verified',
            'date': state['lastChecks']['trading_day_verify'],
            'is_trading_day': state['lastChecks']['is_trading_day'],
            'reportSchedule': state.get('reportSchedule', {})
        }
        
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"✅ Already verified today ({result['date']})")
            print(f"   Trading day: {result['is_trading_day']}")
            if result['is_trading_day']:
                print(f"   Reports enabled: A-Share daily, C2605 hourly+daily")
            else:
                print(f"   Reports: All disabled (non-trading day)")
        
        return 0
    
    # Run trading check
    print("🔍 Running trading day verification...")
    is_trading = run_trading_check()
    
    # Update state
    today = datetime.now().strftime('%Y-%m-%d')
    state['lastChecks']['trading_day_verify'] = today
    state['lastChecks']['is_trading_day'] = is_trading
    state = update_report_schedule(state, is_trading)
    
    # Save state
    save_state(state)
    
    # Output result
    result = {
        'status': 'verified',
        'date': today,
        'is_trading_day': is_trading,
        'reportSchedule': state.get('reportSchedule', {})
    }
    
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"✅ Verification complete ({today})")
        print(f"   Trading day: {is_trading}")
        if is_trading:
            print(f"   📈 A-Share daily report: 15:30")
            print(f"   🌽 C2605 hourly reports: 09:00, 10:00, 11:00, 14:00, 15:00")
            print(f"   🌽 C2605 daily summary: 15:30")
        else:
            print(f"   📭 All reports disabled (weekend or holiday)")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
