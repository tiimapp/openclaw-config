# Stock Tracker 📊

Automated daily stock report system for Chinese A-shares (科创板).

## Overview

This project fetches real-time stock data and news, analyzes trends with MACD signals, and delivers a concise daily report to Discord.

## Target Stock

- **Name:** 中控技术
- **Symbol:** 688777 (SH)
- **Market:** 科创板 (STAR Market)

## Schedule

- **Run Time:** 15:30 Asia/Shanghai (daily, trading days)
- **Delivery:** Discord #show-me-the-money channel

## Features

- ✅ Real-time price data from Sina Finance API
- ✅ MACD buy/sell signal analysis
- ✅ News aggregation from multiple sources
- ✅ Automated daily reports via Discord
- ✅ GitHub version control

## Project Structure

```
stock-tracker/
├── README.md           # This file
├── REPORT_SPEC.md      # Detailed report specification
├── src/
│   ├── fetcher.py      # Data fetching (price + news)
│   ├── analyzer.py     # Technical analysis (MACD, trends)
│   ├── reporter.py     # Report generation & Discord delivery
│   └── main.py         # Entry point
├── config/
│   ├── stocks.json     # Stock symbols to track
│   └── settings.json   # Configuration (time, channels, etc.)
├── logs/               # Runtime logs
└── docs/               # Additional documentation
```

## Quick Start

```bash
# Install dependencies
pip install requests pandas numpy

# Run manually
python src/main.py

# Check logs
tail -f logs/stock-tracker.log
```

## Configuration

Edit `config/settings.json`:

```json
{
  "schedule": "15:30",
  "timezone": "Asia/Shanghai",
  "discord_channel": "1475775915844960428",
  "stocks": ["sh688777"]
}
```

## Data Sources

| Type | Provider | Endpoint |
|------|----------|----------|
| Price | Sina Finance | `https://hq.sinajs.cn/list={symbol}` |
| News | Sina Finance | Web search + fetch |
| News | 东方财富网 | Web search + fetch |
| News | 上交所公告 | Web search |

## MACD Signal Logic

```
BUY:  MACD line crosses above Signal line (golden cross)
SELL: MACD line crosses below Signal line (death cross)
HOLD: No crossover, maintain previous signal
```

## Cron Job

Managed via OpenClaw cron system:
- Job runs daily at 15:30 Shanghai time
- Automatic retry on failure
- Logs stored in `logs/` directory

## Author

Created for tiim🐮 - Discord Server: 1238361831328845896

## License

Private project

---

# C2506 Corn Futures Monitor 🌽

Automated monitoring system for DCE Corn Futures (C2506 - 玉米 2605 contract).

## Overview

This module fetches real-time corn futures data from DCE (Dalian Commodity Exchange) and delivers periodic reports to Discord during trading hours, plus a daily summary after market close.

## Contract Details

- **Name:** 玉米 2605 (Corn May 2026)
- **Symbol:** C2506
- **Exchange:** DCE (大连商品交易所)
- **Trading Hours:** Day session only (no night session)

## Trading Hours (Asia/Shanghai UTC+8)

| Session | Time |
|---------|------|
| Morning 1 | 09:00 - 10:15 |
| Morning 2 | 10:30 - 11:30 |
| Afternoon | 13:30 - 15:00 |

**Trading Days:** Monday - Friday (excluding Chinese public holidays)

## Schedule

| Report Type | Time | Frequency |
|-------------|------|-----------|
| Hourly Report | 09:00, 10:00, 11:00, 14:00, 15:00 | During trading hours |
| Daily Summary | 15:30 | After market close |

## Features

- ✅ Real-time price data from AKShare
- ✅ Trading time detection (includes Chinese holiday calendar)
- ✅ Hourly intraday reports during trading
- ✅ Daily summary with OHLCV data
- ✅ Automated Discord delivery
- ✅ Systemd timer or cron job support

## Project Files

```
stock-tracker/
├── c2506_monitor.py          # Main monitoring script
├── trading_time_checker.py   # Trading time detection module
├── c2506_config.json         # Configuration file
├── cron-c2506.sh             # Cron job wrapper script
├── c2506-monitor.service     # Systemd service (hourly)
├── c2506-monitor.timer       # Systemd timer (hourly)
├── c2506-monitor-daily.service  # Systemd service (daily)
├── c2506-monitor-daily.timer    # Systemd timer (daily)
└── install-systemd-timers.sh    # Installation script
```

## Quick Start

### Option 1: Cron Job

```bash
# Make scripts executable
chmod +x cron-c2506.sh

# Add to crontab (run: crontab -e)
# Hourly reports during trading hours
0 9,10,11,14,15 * * 1-5 /home/admin/.openclaw/workspace/stock-tracker/cron-c2506.sh

# Daily summary after market close
30 15 * * 1-5 /home/admin/.openclaw/workspace/stock-tracker/cron-c2506.sh
```

### Option 2: Systemd Timers (Recommended)

```bash
# Install systemd timers (requires sudo)
sudo ./install-systemd-timers.sh

# Verify installation
systemctl list-timers | grep c2506

# Check status
systemctl status c2506-monitor.timer
systemctl status c2506-monitor-daily.timer

# View logs
journalctl -u c2506-monitor.service -f
journalctl -u c2506-monitor-daily.service -f
```

### Manual Testing

```bash
# Test trading time detection
python3 trading_time_checker.py

# Test hourly report
python3 c2506_monitor.py --mode hourly

# Test daily summary
python3 c2506_monitor.py --mode daily

# Full test mode
python3 c2506_monitor.py --test
```

## Configuration

Edit `c2506_config.json`:

```json
{
  "symbol": "C2506",
  "symbol_name": "玉米 2605",
  "discord_channel_id": "1475775915844960428",
  "trading_hours": {
    "sessions": [
      {"start": "09:00", "end": "10:15"},
      {"start": "10:30", "end": "11:30"},
      {"start": "13:30", "end": "15:00"}
    ]
  },
  "chinese_holidays_2026": {
    "2026-01-01": "New Year's Day",
    "2026-02-17": "Spring Festival",
    // ... more holidays
  }
}
```

## Modifying Trading Hours

1. Edit `c2506_config.json`
2. Update the `trading_hours.sessions` array
3. Update `trading_time_checker.py` if needed
4. Restart systemd timers or reload cron

## Modifying Holidays

1. Edit `c2506_config.json`
2. Update the `chinese_holidays_2026` object
3. Add new holidays in format: `"YYYY-MM-DD": "Holiday Name"`
4. No restart needed - config is loaded on each run

## Report Formats

### Hourly Report (盘中快报)
- Current price and change %
- Session high/low
- Volume and open interest
- Last update timestamp

### Daily Summary (每日总结)
- OHLC (Open, High, Low, Close)
- Daily change %
- K-line pattern (Bullish/Bearish/Doji)
- Total volume and open interest
- 5-day price trend summary

## Data Sources

| Source | Type | Fallback |
|--------|------|----------|
| AKShare | Real-time futures data | Mock data for testing |
| Sina Finance | Historical data | Mock history |

## Troubleshooting

### No data from AKShare
- Check internet connection
- Verify AKShare is installed: `pip install akshare`
- The script falls back to mock data if AKShare fails

### Timer not running
```bash
# Check timer status
systemctl list-timers | grep c2506

# Restart timers
sudo systemctl restart c2506-monitor.timer
sudo systemctl restart c2506-monitor-daily.timer

# Check logs
journalctl -u c2506-monitor.service --since today
```

### Discord not receiving messages
- Verify channel ID in `c2506_config.json`
- Check Discord bot permissions
- Review logs for delivery errors

## Dependencies

```bash
pip install akshare pandas numpy
```

## Author

Created for tiim🐮 - Discord Server: 1238361831328845896

## License

Private project
