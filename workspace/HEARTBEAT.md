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
