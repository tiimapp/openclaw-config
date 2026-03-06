# MEMORY.md - Long-Term Memory

## Projects

### Stock Tracker
- **Repository:** https://github.com/tiimapp/stock-tracker
- **Status:** All 4 phases complete (as of 2026-03-04)
- **Phase 5 (Futures Support):** Planned (2026-03-05)
- **Security:** Credentials file removed before push
- **Notes:** Successfully pushed to GitHub after completing project plan

### AKShare Integration
- **Status:** ✅ COMPLETE (2026-03-05)
- **Finding:** Codebase already uses AKShare v2.0 (migrated earlier today)
- **Audit Report:** Created and pushed - documents existing AKShare usage
- **Purpose:** Futures price data fetching (e.g., Corn Futures C2605)

## System Configuration
- **Gateway:** Running on port 18789 (LAN binding: 0.0.0.0, PID 263786)
- **Note:** ws:// security warning is expected for local LAN use (not critical for local-only access)

## C2605 Corn Futures Monitoring
- **Status:** ✅ COMPLETE (2026-03-06)
- **Trading Hours:** 09:00-10:15, 10:30-11:30, 13:30-15:00 (Mon-Fri, no night session)
- **Hourly Reports:** 09:00, 10:00, 11:00, 14:00, 15:00 (during trading hours only)
- **Daily Summary:** 15:30 (after market close)
- **First Run:** Monday 2026-03-09 09:00 (cron jobs created after trading hours on 2026-03-06)
- **Scripts:** c2605_monitor.py with trading time verification + Chinese holiday calendar

## Collaboration
- **Code_G:** Configured and ready (allowAgents: ["*"]) - gateway restart needed to activate

---
*Last updated: 2026-03-06*
