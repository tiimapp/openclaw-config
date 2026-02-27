# OpenClaw Config Backup - TODO List

## Overview
Set up automated backup of OpenClaw configuration to a local git repository with sanitization.

---

## Tasks

### [x] Step 1: Create Local Repo Folder ✅ COMPLETED
- [x] Create directory `~/openclaw-config-backup`
- [x] Initialize git repo: `git init` (branch: master)
- [x] Create `.gitignore` for Python/runtime files

### [ ] Step 2: Build Python Backup Script
- [ ] Create `~/openclaw-config-backup/backup.py`
- [ ] Implement file discovery from `~/.openclaw/`
- [ ] Add JSON sanitization (remove apiKey, token, auth)
- [ ] Add workspace files copy (HEARTBEAT.md, SOUL.md, etc.)
- [ ] Implement git auto-commit logic
- [ ] Make script executable

### [ ] Step 3: Test the Script
- [ ] Run manually: `python3 ~/openclaw-config-backup/backup.py`
- [ ] Verify files are copied correctly
- [ ] Check secrets are sanitized
- [ ] Confirm git commit works

### [ ] Step 4: Setup Cron Job
- [ ] Create cron job running every 1 hour
- [ ] Point to backup script
- [ ] Use isolated session
- [ ] Disable delivery (no announcements needed)

### [ ] Step 5: Verify Automation
- [ ] Wait for first cron run (or trigger manually)
- [ ] Check git log shows commits
- [ ] Monitor for any errors

---

## Files to Backup

| Source | Destination | Sanitize? |
|--------|-------------|-----------|
| `~/.openclaw/openclaw.json` | `config/openclaw.json` | Yes |
| `~/.openclaw/cron/jobs.json` | `cron/jobs.json` | No |
| `~/.openclaw/workspace/*` | `workspace/*` | No |

---

## Sensitive Fields to Sanitize

- `apiKey` → `<APIKEY>`
- `token` → `<TOKEN>`
- `auth.token` → `<AUTH_TOKEN>`

---

## Cron Schedule

- **Frequency**: Every 1 hour
- **Command**: `python3 ~/openclaw-config-backup/backup.py`
- **Session**: Isolated

---

## Notes

- First backup may be large (all files new)
- Subsequent backups only commit when changes detected
- Git history will show config evolution over time
- Secrets never leave local machine

---

Created: 2026-02-26
