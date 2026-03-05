# C2605 Corn Futures Monitoring Setup

**Symbol:** C2605 (玉米 2605 - May 2026 Corn Futures)
**Exchange:** DCE (大连商品交易所)
**Created:** 2026-03-05

---

## Trading Hours (Asia/Shanghai UTC+8)

### Day Session (Monday-Friday)
- **Morning:** 09:00-10:15, 10:30-11:30
- **Afternoon:** 13:30-15:00

### Night Session (Sunday-Thursday)
- **Night:** 21:00-23:00
- Note: Night session belongs to next trading day (e.g., Monday 21:00 = Tuesday's session)

### Holidays (No Trading)
- Chinese New Year
- Qingming Festival
- Labor Day
- Dragon Boat Festival
- Mid-Autumn Festival
- National Day Golden Week

---

## Cron Job Configuration

### Hourly Report (During Trading)
**Schedule:** Every hour at :00 during trading sessions
- 09:00, 10:00, 11:00 (morning session)
- 14:00, 15:00 (afternoon session)

**Content:**
- Current price & change %
- Session high/low
- Volume
- Last update timestamp

### Daily Summary (After Market Close)
**Schedule:** 15:30 (after market closes)

**Content:**
- OHLC (Open, High, Low, Close)
- Total volume
- Open interest change
- Daily chart summary

---

## Implementation Files

| File | Purpose |
|------|---------|
| `trading_time_checker.py` | Check if currently trading time |
| `c2506_monitor.py` | Main monitoring script |
| `c2506_config.json` | Configuration (symbol, channel, etc.) |
| `cron-c2506.sh` | Cron job wrapper script |

---

## Installation

```bash
# Add to crontab
crontab -e

# Add these lines:
# Hourly during trading (09:00-11:00, 14:00-15:00 Mon-Fri)
0 9-11,14-15 * * 1-5 /path/to/cron-c2506.sh hourly

# Daily summary at 15:30
30 15 * * 1-5 /path/to/cron-c2506.sh daily
```

---

## Manual Testing

```bash
# Test trading time detection
python3 trading_time_checker.py

# Test hourly report
python3 c2506_monitor.py --mode hourly

# Test daily summary
python3 c2506_monitor.py --mode daily
```

---

## Status

- [ ] Trading time checker created
- [ ] Monitor script created
- [ ] Config file created
- [ ] Cron jobs installed
- [ ] Tested successfully
- [ ] Documentation complete

---

**Notes:**
- Uses AKShare for futures data (Sina-based, works overseas)
- Discord delivery to #show-me-the-money channel
- Auto-detects trading vs non-trading time
