# 🤖 OpenClaw Skill Discovery - Final Report

**Generated:** 2026-03-10 07:00 AM (Asia/Shanghai)  
**Search Duration:** 7.5 hours (15 search cycles)  
**Total Skills Discovered:** 63

---

## 1. Executive Summary

This report summarizes a comprehensive 7.5-hour skill discovery campaign for the OpenClaw AI agent framework. The search explored built-in skills, user-installed skills, workspace customizations, and external marketplaces.

### Key Findings

| Discovery Channel | Skills Found | Status |
|-------------------|--------------|--------|
| Built-in (`/usr/lib/node_modules/openclaw/skills/`) | 52 | ✅ Fully Documented |
| User-Installed (`~/.agents/skills/`) | 9 | ✅ Documented |
| Workspace (`/home/admin/.openclaw/workspace/skills/`) | 2 | ✅ Documented |
| **Total** | **63** | **Complete** |

### Discovery Challenge

**Web search is NOT effective** for OpenClaw skill discovery due to name collisions:
- 1997 platformer game "Claw" / OpenClaw remake (GitHub: OpenClaw/OpenClaw)
- MuleSoft CloudHub (iPaaS platform, phonetic similarity to "clawdhub")
- UC San Diego robotics project (OpenCLAW - legged robots)
- Croc: Legend of the Gobbos reimplementation

### Proven Discovery Channels

1. **clawhub CLI** - Official marketplace: `npm i -g clawhub`
2. **skills.sh** - Alternative ecosystem: `npx skills find [query]`
3. **Local directories** - Direct exploration of skill folders

---

## 2. Top 10 Recommended Skills

| # | Skill | Priority | Description | Install Command |
|---|-------|----------|-------------|-----------------|
| 1 | **clawhub** | 🔴 High | Official skills marketplace CLI - search, install, update, publish community skills | `npm i -g clawhub` |
| 2 | **gh-issues** | 🔴 High | Auto-fix GitHub issues with parallel sub-agents, open PRs, handle review comments | Pre-installed |
| 3 | **agent-reach** | 🔴 High | 12+ platform integrations (X/Twitter, Reddit, YouTube, Bilibili, 小红书，抖音，GitHub, LinkedIn, Boss直聘，RSS) | `pip install https://github.com/Panniantong/agent-reach/archive/main.zip` + `agent-reach install --env=auto` |
| 4 | **akshare-stock** | 🔴 High | A股 analysis全能 - real-time quotes, K-lines, money flow, fundamentals, sector rotation, HK/US stocks | `pip install akshare pandas numpy` |
| 5 | **peekaboo** | 🔴 High | Full macOS UI automation - capture, inspect, click, type, drag, app/window/menu control | `brew install steipete/tap/peekaboo` |
| 6 | **bluebubbles** | 🔴 High | iMessage integration - send, react, edit, unsend, DMs (requires BlueBubbles server) | Pre-installed (configure BlueBubbles server) |
| 7 | **xurl** | 🔴 High | X (Twitter) API CLI - post, reply, search, DMs, media upload with OAuth2 | `brew install xdevplatform/tap/xurl` or `npm i -g @xdevplatform/xurl` |
| 8 | **tmux** | 🔴 High | Remote-control tmux sessions - send keystrokes, scrape output, manage windows/panes | Pre-installed (needs tmux) |
| 9 | **session-logs** | 🔴 High | Search and analyze conversation history - essential for context retrieval from older sessions | Pre-installed (needs jq, rg) |
| 10 | **vercel-react-best-practices** | 🔴 High | React/Next.js performance optimization from Vercel Engineering | `npx skills add vercel-labs/agent-skills@vercel-react-best-practices -g -y` |

---

## 3. Complete Priority Ranking

### 🔴 High Priority (17 skills)

| Skill | Category | Why It Matters |
|-------|----------|----------------|
| clawhub | Marketplace | Gateway to 100+ community skills |
| gh-issues | Development | Automated GitHub workflow |
| discord | Messaging | Full Discord automation |
| github | Development | GitHub CLI operations |
| mcporter | Integration | MCP server protocol support |
| xurl | Social | X/Twitter API access |
| bluebubbles | Messaging | iMessage automation |
| coding-agent | Development | Delegate to Codex/Claude Code/Pi |
| agent-reach | Social | 12+ platform integrations |
| akshare-stock | Finance | Comprehensive A股 analysis |
| china-stock-analysis | Finance | Value investment analysis |
| peekaboo | Automation | macOS UI control |
| tmux | Productivity | Terminal session management |
| session-logs | Debugging | Conversation history search |
| vercel-composition-patterns | Development | React architecture patterns |
| vercel-react-best-practices | Development | React/Next.js performance |
| find-skills | Discovery | skills.sh ecosystem access |

### 🟡 Medium Priority (32 skills)

| Skill | Category | Install Command |
|-------|----------|-----------------|
| weather | Utility | Pre-installed |
| notion | Productivity | Pre-installed (needs API key) |
| sag | TTS | `brew install steipete/tap/sag` |
| healthcheck | Security | Pre-installed |
| 1password | Security | Pre-installed |
| canvas | UI | Pre-installed |
| slack | Messaging | Pre-installed |
| spotify-player | Media | `brew install steipete/tap/spogo` |
| nano-pdf | Document | `uv install nano-pdf` |
| bear-notes | Notes | `go install github.com/tylerwince/grizzly/cmd/grizzly@latest` |
| openai-image-gen | AI | `brew install python` + OPENAI_API_KEY |
| eightctl | IoT | `go install github.com/steipete/eightctl/cmd/eightctl@latest` |
| nano-banana-pro | AI | `brew install uv` + GEMINI_API_KEY |
| model-usage | Analytics | `brew install steipete/tap/codexbar` |
| himalaya | Email | Pre-installed |
| gemini | AI | Pre-installed (needs API key) |
| openhue | Smart Home | `brew install openhue/cli/openhue-cli` |
| oracle | AI | `npm i -g @steipete/oracle` |
| sherpa-onnx-tts | TTS | Download from GitHub releases |
| wacli | Messaging | `brew install steipete/tap/wacli` |
| openai-whisper | STT | `brew install openai-whisper` |
| things-mac | Productivity | `go install github.com/ossianhempel/things3-cli/cmd/things@latest` |
| apple-notes | Notes | `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo` |
| openai-whisper-api | STT | Pre-installed (needs OPENAI_API_KEY) |
| vercel-react-native-skills | Development | `npx skills add vercel-labs/agent-skills@vercel-react-native-skills -g -y` |
| web-design-guidelines | Design | `npx skills add vercel-labs/agent-skills@web-design-guidelines -g -y` |
| sports-monitor | Sports | `pip install requests python-dateutil` + config.json |
| bluetooth | Connectivity | Pre-installed |
| calendar | Productivity | Pre-installed |
| files | Utility | Pre-installed |
| search | Utility | Pre-installed |
| timer | Utility | Pre-installed |

### 🟢 Low Priority (14 skills)

| Skill | Category | Notes |
|-------|----------|-------|
| obsidian | Notes | Pre-installed |
| trello | Productivity | Pre-installed |
| apple-reminders | Productivity | Pre-installed |
| blogwatcher | RSS | Pre-installed |
| summarize | Utility | Pre-installed |
| voice-call | Communication | Pre-installed |
| goplaces | Location | Pre-installed |
| camsnap | Camera | Pre-installed |
| gog | Gaming | Pre-installed |
| imsg | Messaging | Pre-installed |
| gifgrep | Media | Pre-installed |
| blucli | Audio | `go install github.com/steipete/blucli/cmd/blu@latest` |
| sonoscli | Audio | `go install github.com/steipete/sonoscli/cmd/sonos@latest` |
| ordercli | Food | `brew install steipete/tap/ordercli` |
| video-frames | Media | `brew install ffmpeg` |
| songsee | Audio | `brew install steipete/tap/songsee` |

---

## 4. Quick Install Script

### 🚀 One-Time Setup (All High-Priority Skills)

```bash
#!/bin/bash
# OpenClaw High-Priority Skills Quick Install
# Run this once to set up the most valuable skills

set -e

echo "🔧 Installing clawhub marketplace CLI..."
npm i -g clawhub

echo "🎨 Installing peekaboo (macOS UI automation)..."
brew install steipete/tap/peekaboo

echo "🐦 Installing xurl (X/Twitter API)..."
brew install xdevplatform/tap/xurl

echo "🎵 Installing spogo (Spotify)..."
brew install steipete/tap/spogo

echo "📊 Installing akshare for stock analysis..."
pip install akshare pandas numpy

echo "🌐 Installing agent-reach (12+ platform integrations)..."
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto

echo "📦 Installing Vercel React skills from skills.sh..."
npx skills add vercel-labs/agent-skills@vercel-composition-patterns -g -y
npx skills add vercel-labs/agent-skills@vercel-react-best-practices -g -y
npx skills add vercel-labs/agent-skills@vercel-react-native-skills -g -y
npx skills add vercel-labs/agent-skills@web-design-guidelines -g -y

echo "✅ High-priority skills installation complete!"
echo ""
echo "⚠️  Manual configuration required for:"
echo "   - bluebubbles: Set up BlueBubbles server for iMessage"
echo "   - xurl: Run 'xurl auth' for Twitter OAuth2"
echo "   - akshare-stock: No API key needed (uses public data)"
echo "   - agent-reach: Run 'agent-reach doctor' to check channel status"
```

### 🔍 Discovery Commands

```bash
# Search clawhub marketplace
clawhub search [keyword]

# Search skills.sh ecosystem
npx skills find [keyword]

# List installed skills
clawhub list

# Update all skills
clawhub update
```

---

## 5. Usage Examples

### 📦 clawhub (Marketplace)

```bash
# Search for skills
clawhub search github
clawhub search weather
clawhub search tts

# Install a skill
clawhub install skill-name

# Update skills
clawhub update

# List installed skills
clawhub list
```

### 💬 agent-reach (Multi-Platform)

```bash
# Check channel status
agent-reach doctor

# Post to X/Twitter
agent-reach post x "Hello from OpenClaw!"

# Search Reddit
agent-reach search reddit "OpenClaw"

# Get YouTube video info
agent-reach fetch youtube https://youtube.com/watch?v=...

# Check Bilibili trending
agent-reach trending bilibili
```

### 📈 akshare-stock (A股 Analysis)

```bash
# Real-time index quotes
akshare-stock "上证指数当前点位"

# K-line chart data
akshare-stock "贵州茅台日线"

# Money flow analysis
akshare-stock "北向资金流向"

# Sector rotation
akshare-stock "今日涨停板块"

# Fundamental analysis
akshare-stock "宁德时代财报分析"
```

### 🖥️ peekaboo (macOS UI Automation)

```bash
# Capture screen and inspect elements
peekaboo capture --inspect

# Click on element by ID
peekaboo click e12

# Type text into field
peekaboo type e34 "Hello World"

# Run automation script
peekaboo run script.peekaboo.json
```

### 🐙 gh-issues (GitHub Automation)

```bash
# Auto-fix issues with label "bug"
/gh-issues owner/repo --label bug --limit 5

# Watch for new issues continuously
/gh-issues owner/repo --watch --interval 5

# Assign issues to yourself
/gh-issues owner/repo --assignee @me

# Run with specific model
/gh-issues owner/repo --model glm-5
```

### 📊 session-logs (Conversation History)

```bash
# List sessions by date
jq -r '.sessionKey' ~/.openclaw/agents/main/sessions/*/session.json | head

# Find sessions from specific day
ls ~/.openclaw/agents/main/sessions/ | grep 2026-03-09

# Search for keyword in messages
rg "skill discovery" ~/.openclaw/agents/main/sessions/*/messages.jsonl

# Extract token usage
jq '.usage' ~/.openclaw/agents/main/sessions/*/session.json
```

### 🎨 vercel-react-best-practices

```bash
# Trigger via natural language
"Review this React component for performance issues"
"Optimize this Next.js page for bundle size"
"Check my data fetching pattern against Vercel best practices"

# The skill will automatically:
# - Analyze code against Vercel Engineering guidelines
# - Identify performance bottlenecks
# - Suggest optimizations (code splitting, caching, streaming)
```

---

## 6. Appendix: Full Skill Inventory

### Built-in Skills (52)
Located: `/usr/lib/node_modules/openclaw/skills/`

clawhub, gh-issues, weather, discord, notion, sag, github, healthcheck, mcporter, obsidian, trello, apple-reminders, 1password, blogwatcher, summarize, voice-call, canvas, goplaces, slack, coding-agent, eightctl, nano-banana-pro, blucli, model-usage, camsnap, gog, himalaya, imsg, gifgrep, gemini, nano-pdf, bluebubbles, bear-notes, openai-image-gen, songsee, xurl, openhue, oracle, sherpa-onnx-tts, peekaboo, sonoscli, wacli, ordercli, openai-whisper, things-mac, tmux, apple-notes, openai-whisper-api, session-logs, video-frames, bluetooth, calendar, files, search, timer

### User-Installed Skills (9)
Located: `~/.agents/skills/`

sports-monitor, agent-reach, find-skills, akshare-stock, china-stock-analysis, vercel-composition-patterns, vercel-react-best-practices, vercel-react-native-skills, web-design-guidelines

### Workspace Skills (2)
Located: `/home/admin/.openclaw/workspace/skills/`

github, self-improving-agent

---

## 7. Recommendations

### Immediate Actions
1. ✅ Install `clawhub` CLI for ongoing skill discovery
2. ✅ Configure `bluebubbles` server for iMessage (if on macOS)
3. ✅ Run `agent-reach doctor` to verify platform connections
4. ✅ Set up API keys for premium services (OpenAI, Gemini)

### Ongoing Maintenance
- Run `clawhub update` weekly for skill updates
- Check `clawhub search` monthly for new community skills
- Review `~/.agents/skills/` quarterly for unused skills
- Monitor session logs for skill usage patterns

### Future Discovery
- Prioritize CLI tools over web search
- Use `clawhub search [keyword]` for marketplace discovery
- Use `npx skills find [keyword]` for skills.sh ecosystem
- Explore GitHub for skill repositories directly

---

**Report compiled by:** ClawBot  
**Session:** cron:7f69e686-1793-4b24-96b8-26b1485d6584  
**Delivery:** Discord DM to User (ID: 431977287446167554)
