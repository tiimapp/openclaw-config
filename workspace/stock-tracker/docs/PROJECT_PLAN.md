# Stock Tracker - Project Plan 📋

## Status: Phase 1 Complete ✅

---

## Phase 1: Project Setup (DONE)

- [x] Create project folder structure
- [x] Write README.md
- [x] Write REPORT_SPEC.md (detailed specification)
- [x] Create config files (stocks.json, settings.json)
- [x] Document MACD logic and data sources
- [x] Define report format and delivery schedule

**Deliverables:**
- ✅ `/home/admin/.openclaw/workspace/stock-tracker/` created
- ✅ All documentation in place
- ✅ Ready for GitHub initialization

---

## Phase 2: Core Development (TODO - Code_G)

### 2.1 Data Fetcher (`src/fetcher.py`)

- [ ] Implement Sina API price fetcher
- [ ] Parse Sina API response (comma-separated values)
- [ ] Implement news search (Sina + 东方财富 + 上交所)
- [ ] Handle retries and error cases
- [ ] Cache responses for debugging

### 2.2 Analyzer (`src/analyzer.py`)

- [ ] Calculate MACD (12, 26, 9 EMA)
- [ ] Detect buy/sell signals (golden/death cross)
- [ ] Calculate 5-day trend
- [ ] Identify support/resistance levels
- [ ] Generate technical analysis summary

### 2.3 Reporter (`src/reporter.py`)

- [ ] Format report in markdown
- [ ] Insert price data, MACD signals, news
- [ ] Send to Discord via OpenClaw message tool
- [ ] Handle delivery failures gracefully

### 2.4 Main Entry Point (`src/main.py`)

- [ ] Load configuration
- [ ] Orchestrate fetch → analyze → report pipeline
- [ ] Log all operations
- [ ] Handle exceptions and edge cases

---

## Phase 3: Integration & Testing (TODO)

### 3.1 Manual Testing

- [ ] Run script manually
- [ ] Verify price data accuracy
- [ ] Verify MACD calculation
- [ ] Verify news fetching
- [ ] Test Discord delivery

### 3.2 Cron Setup

- [ ] Create OpenClaw cron job
- [ ] Set schedule: 15:30 Asia/Shanghai (Mon-Fri)
- [ ] Test cron trigger
- [ ] Verify automatic delivery

### 3.3 Monitoring

- [ ] Set up log rotation
- [ ] Add error notifications
- [ ] Create health check endpoint (optional)

---

## Phase 4: GitHub & Deployment (TODO)

### 4.1 GitHub Setup

```bash
cd ~/.openclaw/workspace/stock-tracker
git init
git add .
git commit -m "Initial commit: Stock Tracker project structure"
git remote add origin <your-repo-url>
git push -u origin main
```

### 4.2 Documentation

- [ ] Add .gitignore (logs, __pycache__, etc.)
- [ ] Add LICENSE file
- [ ] Update README with GitHub badge
- [ ] Add contribution guidelines (optional)

---

## Timeline

| Phase | Tasks | Owner | ETA |
|-------|-------|-------|-----|
| 1 | Project setup | ClawBot | ✅ Done |
| 2 | Core development | Code_G | TBD |
| 3 | Integration & testing | Both | TBD |
| 4 | GitHub & deployment | ClawBot | TBD |

---

## Next Steps

1. **Initialize Git repo** (awaiting user confirmation)
2. **Delegate to Code_G** for core development
3. **Review & iterate** on first implementation
4. **Deploy cron job** and go live

---

## Open Questions

- [ ] GitHub repo URL? (public or private?)
- [ ] Any additional stocks to track?
- [ ] Preferred Python version? (defaulting to 3.11)
- [ ] Any specific news keywords to filter?

---

**Last Updated:** 2026-03-01  
**Project Owner:** tiim🐮  
**Developer:** Code_G + ClawBot
