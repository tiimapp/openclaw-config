# HEARTBEAT.md - Periodic Checks

## Check Schedule (every 2 hours)

### 1. System Status
- Check OpenClaw gateway status
- Verify cron jobs are running

### 2. Model Health Check
- **Primary Model:** qwen3.5-plus (qwen3-max-2026-01-23 provider)
- **Fallback Model:** gemini-3-flash-preview (custom-G provider)
- Test both models respond to simple requests
- Alert user if either model fails

### 3. Memory Maintenance  
- Review recent memory files (last 2-3 days)
- Summarize important events to MEMORY.md if needed

### 4. Notifications
- Check for any urgent alerts or messages

### 5. Daily Trading Day Verification ⭐ (FIRST heartbeat only)
**When:** First heartbeat of each day (before 10:00)
**State File:** `memory/heartbeat-state.json`
**Script:** `heartbeat_trading_check.py`

**Check Steps:**
1. Run: `python3 heartbeat_trading_check.py`
2. Script reads `memory/heartbeat-state.json` to check if already verified today
3. If NOT verified → Run trading day check → Update state
4. If already verified → Skip (don't repeat)

**Decision Logic:**
| Result | A-Share Report | C2605 Futures Report |
|--------|----------------|---------------------|
| Trading Day | ✅ Send at 15:30 | ✅ Send hourly + 15:30 |
| Non-Trading Day | ❌ Skip | ❌ Skip |

**State File After Check:**
```json
{
  "lastChecks": {
    "trading_day_verify": "2026-03-10",
    "is_trading_day": true
  },
  "reportSchedule": {
    "ashare_daily": "15:30",
    "c2605_hourly": "09:00,10:00,11:00,14:00,15:00,21:00,22:00,23:00",
    "c2605_daily": "15:30"
  }
}
```

**Test Commands:**
```bash
# Normal check (skips if already verified today)
python3 heartbeat_trading_check.py

# Force re-verification
python3 heartbeat_trading_check.py --force

# JSON output (for automation)
python3 heartbeat_trading_check.py --json
```

### 6. C2605 Night Trading Verification ⭐ NEW
**When:** Daily (can be combined with trading day check)
**State File:** `memory/dce-trading-state.json`
**Script:** `stock-tracker/dce_trading_verifier.py`

**Purpose:** Verify if DCE Corn Futures (C2605) has night trading session (21:00-23:00)

**Current Status:** ⚠️ **UNCERTAIN** (sources conflict)
- Some sources say: Night trading ENABLED (21:00-23:00)
- Other sources say: Night trading DISABLED
- DCE official website: Inaccessible from overseas

**Recommendation:** Continue monitoring (keep night reports active)

**Test Commands:**
```bash
# Normal verification
cd /home/admin/.openclaw/workspace/stock-tracker
python3 dce_trading_verifier.py

# Force re-verification
python3 dce_trading_verifier.py --force

# JSON output
python3 dce_trading_verifier.py --json
```

**Documentation:** `stock-tracker/docs/C2605-night-trading-research.md`

#### 🔍 Tavily Search Verification (Recommended Data Source)

**Setup:**
```bash
# Install Tavily SDK
pip install tavily-python

# Set API Key (add to ~/.openclaw/.env)
export TAVILY_API_KEY='tvly-xxxxxxxxxxxxxxxxxxxx'
```

**Quick Verification:**
```python
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])
response = client.search(
    query="大连商品交易所 玉米期货 夜盘交易时间 2026",
    search_depth="advanced",
    max_results=5,
    include_answer=True,
    topic="finance",  # Finance topic filter
    days=7  # Last 7 days only
)

print(response['answer'])  # AI-synthesized answer
print(response['results'])  # Sources with URLs
```

**Advantages:**
- ✅ AI-generated direct answer (no manual reading)
- ✅ Time filtering (`days=7` for latest info)
- ✅ Topic filtering (`topic="finance"`)
- ✅ Cited sources with URLs (traceable)
- ✅ Clean results, no ads (agent-optimized)

**Integration:** Add Tavily verification to `dce_trading_verifier.py` as primary data source.

### 7. C2605 Trading Time Check (During Trading Hours)
- Verify hourly reports are being generated
- Alert if reports missed during active trading

**Trading Hours (Asia/Shanghai UTC+8):**
- Morning: 09:00-10:15, 10:30-11:30
- Afternoon: 13:30-15:00
- **Night: 21:00-23:00** ⭐
- Days: Monday-Friday (exclude Chinese holidays)

**Report Generation Buffer:** +5 minutes after each session end for closing price capture
- 10:20 (after morning session 1)
- 11:35 (after morning session 2)
- 15:05 (after afternoon session - closing price)
- 23:05 (after night session - closing price)

---

## State File Management

**File:** `memory/heartbeat-state.json`

**Purpose:** Track what has been checked today to avoid redundant verification

**Reset:** Date check resets at midnight (new day = new verification)

**Example Structure:**
```json
{
  "lastChecks": {
    "trading_day_verify": "2026-03-06",
    "is_trading_day": true,
    "email": 1703275200,
    "calendar": 1703260800
  }
}
```

---

## When to Notify User

**Reach out when:**
- Cron job failures detected
- Model health check fails (primary or fallback)
- Trading day verification complete (report schedule confirmed)
- Important system events occur
- It's been >8h since last interaction (and not late night)

**Stay quiet when:**
- Late night (23:00-08:00) unless urgent
- Nothing new since last check
- Just checked <2 hours ago

## When to Notify User

**Reach out when:**
- Cron job failures detected
- Model health check fails (primary or fallback)
- Important system events occur
- It's been >8h since last interaction (and not late night)

**Stay quiet when:**
- Late night (23:00-08:00) unless urgent
- Nothing new since last check
- Just checked <2 hours ago

## Model Test Commands

```bash
# Primary model test
curl -s -X POST https://coding.dashscope.aliyuncs.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-sp-92055d32b2ee4988bb5cb8d468e64c46" \
  -d '{"model":"qwen3.5-plus","messages":[{"role":"user","content":"Hi"}],"max_tokens":5}'

# Fallback model test
curl -s -X POST https://api.xstx.info/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-2G7U1NaQ4JpJlthIUDZgLP5rPnv532rhV0cMlsA6hjbP419e" \
  -d '{"model":"gemini-3-flash-preview","messages":[{"role":"user","content":"Hi"}],"max_tokens":5}'
```

---
Last updated: 2026-03-04
