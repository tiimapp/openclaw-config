# Learnings Log

Continuous improvement log for OpenClaw workspace.

---

## [LRN-20260309-001] cron_delivery_failures

**Logged**: 2026-03-09T23:02:00+08:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Multiple C2605 cron jobs failing with "cron announce delivery failed" - Discord channel delivery issues

### Details
- C2605 hourly reports at 10:00, 11:00, 15:00 failing
- Stock Tracker Daily also failing
- Reports execute successfully but can't deliver to Discord
- Error: `cron announce delivery failed`
- Target channel may have changed permissions or been deleted

### Suggested Action
1. Verify Discord channel `#1475775915844960428` still exists
2. Check bot has send permissions in target channels
3. Update channel IDs if channels were recreated
4. Consider fallback delivery method (DM instead of channel)

### Metadata
- Source: health_check
- Related Files: `~/.openclaw/cron/jobs.json`
- Tags: discord, cron, delivery, C2605
- See Also: ERR-20260307-delivery (if exists)

---

## [LRN-20260309-002] thinking_level_configuration

**Logged**: 2026-03-09T20:34:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: config

### Summary
Updated default thinking level from `minimal` to `medium` for better reasoning balance

### Details
- Previous setting: `minimal` (quick responses)
- New setting: `medium` (balanced reasoning)
- Applied to both session config and agent defaults
- Location: `~/.openclaw/agents/main/sessions/sessions.json` and `~/.openclaw/openclaw.json`

### Resolution
- **Resolved**: 2026-03-09T20:34:00+08:00
- **Config**: Added `"thinkingLevel": "medium"` to agents.defaults
- **Notes**: Takes effect on next session start

### Metadata
- Source: user_request
- Related Files: `~/.openclaw/openclaw.json`
- Tags: config, thinking, agent

---

## [LRN-20260309-003] timeout_configuration

**Logged**: 2026-03-09T22:45:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: config

### Summary
Increased agent timeout from 10 minutes to 60 minutes to prevent premature task termination

### Details
- Previous: `timeoutSeconds: 600` (10 min)
- New: `timeoutSeconds: 3600` (60 min)
- Triggered by: "Request timed out before response was generated"
- Location: `~/.openclaw/openclaw.json` agents.defaults

### Resolution
- **Resolved**: 2026-03-09T22:45:00+08:00
- **Config**: Updated `agents.defaults.timeoutSeconds` to 3600
- **Notes**: Allows longer-running tasks to complete

### Metadata
- Source: error_recovery
- Related Files: `~/.openclaw/openclaw.json`
- Tags: config, timeout, agent

---

## [LRN-20260309-004] model_recovery

**Logged**: 2026-03-09T18:08:00+08:00
**Priority**: high
**Status**: resolved
**Area**: infra

### Summary
Primary model recovered after ~6 hour outage

### Details
- Primary model (qwen3.5-plus) was unavailable from ~12:00 to 18:08
- Fallback model (gemini-3-flash-preview) remained operational
- Recovery confirmed via model health check at 18:08

### Resolution
- **Resolved**: 2026-03-09T18:08:00+08:00
- **Notes**: Model health check now passing for both primary and fallback

### Metadata
- Source: model_health_check
- Related Files: `memory/heartbeat-state.json`
- Tags: model, api, outage, recovery

---
