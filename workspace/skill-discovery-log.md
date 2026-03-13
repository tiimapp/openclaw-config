# OpenClaw Skill Discovery Log
## Search #1 - March 13, 2026 (4:50 AM Asia/Shanghai)


## Search #1 - March 13, 2026 (4:50 AM Asia/Shanghai)

### Sources:
- GitHub repositories: openclaw/clawhub, openclaw/skills, VoltAgent/awesome-openclaw-skills
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

### Key Findings:

**1. ClawHub (openclaw/clawhub)**
- Description: Public skill registry for OpenClaw/Clawdbot that allows publishing, versioning, and searching text-based agent skills
- Install Command: `clawhub install <skill-slug>`
- Use Case: Centralized repository for discovering and installing OpenClaw skills with moderation and vector search capabilities

**2. GitHub Integration Skill (github)**
- Description: Interact with GitHub using the `gh` CLI for issues, PRs, CI runs, and advanced queries
- Install Command: `clawhub install github` or manual installation to ~/.openclaw/workspace/skills/
- Use Case: Automating GitHub workflows like checking PR status, listing workflow runs, and accessing GitHub API data

**3. Tavily Search Skill (tavily-search)**
- Description: Web search integration using Tavily API for current information retrieval
- Install Command: `clawhub install tavily-search`
- Use Case: Getting up-to-date information from the web when the base model's knowledge is insufficient

**4. Self-Improvement Skill (self-improving-agent)**
- Description: Captures learnings, errors, and corrections to enable continuous improvement of the agent
- Install Command: `clawhub install self-improving-agent`
- Use Case: Documenting mistakes and lessons learned to prevent repeating them in future interactions

**5. Productivity & Task Management Skills**
- Examples: 
  - **4to1-planner**: AI planning coach using the 4To1 Method™ to turn long-term vision into daily actions
  - **agent-task-manager**: Manages and orchestrates multi-step, stateful agent workflows
  - **adhd-daily-planner**: Time-blind friendly planning with executive function support
- Install Command: `clawhub install <skill-name>`
- Use Case: Personal productivity enhancement, task management, and daily planning assistance

**6. AI & LLM Specialized Skills**
- Examples:
  - **agent-autonomy-kit**: Enables autonomous operation without waiting for prompts
  - **adaptive-reasoning**: Automatically assesses task complexity and adjusts reasoning level
  - **agent-contact-card**: Creates vCard-like contact information for AI agents
- Install Command: `clawhub install <skill-name>`
- Use Case: Enhancing AI agent capabilities with specialized functions for autonomy, reasoning, and identity

**Skill Categories Available:**
- AI & LLMs (197 skills)
- Git & GitHub (170 skills)
- Productivity & Tasks (206 skills)
- Coding Agents & IDEs (385 skills)
- DevOps & Cloud (247 skills)
- Web & Frontend Development (434 skills)
- Search & Research (198 skills)
- And many more categories totaling 5,490+ skills

**Installation Methods:**
1. Using ClawHub CLI: `clawhub install <skill-slug>`
2. Manual installation by copying skill folders to ~/.openclaw/workspace/skills/
3. Nix package integration for supported skills

**Skill Structure:**
- Each skill contains a SKILL.md file with metadata (name, description, requirements)
- May include supporting scripts, configuration files, and documentation
- Skills declare runtime requirements (environment variables, binaries) in SKILL.md frontmatter

## Search #2 - March 13, 2026 (4:50 AM Asia/Shanghai)

### Sources:
- GitHub repositories: openclaw/clawhub, openclaw/skills, VoltAgent/awesome-openclaw-skills
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

### Key Findings:

**1. ClawHub (openclaw/clawhub)**
- Description: Public skill registry for OpenClaw/Clawdbot that allows publishing, versioning, and searching text-based agent skills
- Install Command: `clawhub install <skill-slug>`
- Use Case: Centralized repository for discovering and installing OpenClaw skills with moderation and vector search capabilities

**2. GitHub Integration Skill (github)**
- Description: Interact with GitHub using the `gh` CLI for issues, PRs, CI runs, and advanced queries
- Install Command: `clawhub install github` or manual installation to ~/.openclaw/workspace/skills/
- Use Case: Automating GitHub workflows like checking PR status, listing workflow runs, and accessing GitHub API data

**3. Tavily Search Skill (tavily-search)**
- Description: Web search integration using Tavily API for current information retrieval
- Install Command: `clawhub install tavily-search`
- Use Case: Getting up-to-date information from the web when the base model's knowledge is insufficient

**4. Self-Improvement Skill (self-improving-agent)**
- Description: Captures learnings, errors, and corrections to enable continuous improvement of the agent
- Install Command: `clawhub install self-improving-agent`
- Use Case: Documenting mistakes and lessons learned to prevent repeating them in future interactions

**5. Productivity & Task Management Skills**
- Examples: 
  - **4to1-planner**: AI planning coach using the 4To1 Method™ to turn long-term vision into daily actions
  - **agent-task-manager**: Manages and orchestrates multi-step, stateful agent workflows
  - **adhd-daily-planner**: Time-blind friendly planning with executive function support
- Install Command: `clawhub install <skill-name>`
- Use Case: Personal productivity enhancement, task management, and daily planning assistance

**6. AI & LLM Specialized Skills**
- Examples:
  - **agent-autonomy-kit**: Enables autonomous operation without waiting for prompts
  - **adaptive-reasoning**: Automatically assesses task complexity and adjusts reasoning level
  - **agent-contact-card**: Creates vCard-like contact information for AI agents
- Install Command: `clawhub install <skill-name>`
- Use Case: Enhancing AI agent capabilities with specialized functions for autonomy, reasoning, and identity

**Skill Categories Available:**
- AI & LLMs (197 skills)
- Git & GitHub (170 skills)
- Productivity & Tasks (206 skills)
- Coding Agents & IDEs (385 skills)
- DevOps & Cloud (247 skills)
- Web & Frontend Development (434 skills)
- Search & Research (198 skills)
- And many more categories totaling 5,490+ skills

**Installation Methods:**
1. Using ClawHub CLI: `clawhub install <skill-slug>`
2. Manual installation by copying skill folders to ~/.openclaw/workspace/skills/
3. Nix package integration for supported skills

**Skill Structure:**
- Each skill contains a SKILL.md file with metadata (name, description, requirements)
- May include supporting scripts, configuration files, and documentation
- Skills declare runtime requirements (environment variables, binaries) in SKILL.md frontmatter

## Search #3 - March 13, 2026 (5:20 AM Asia/Shanghai)

### Sources:
- Local workspace skills: ~/.openclaw/workspace/skills/
- System-wide skills: /usr/lib/node_modules/openclaw/skills/
- GitHub repositories and documentation

### Key Findings:

**1. GitHub Integration Skill (github)**
- Description: Interact with GitHub using the `gh` CLI for issues, PRs, CI runs, and advanced queries
- Install Command: Built-in skill (no installation required)
- Use Case: Automating GitHub workflows like checking PR status, listing workflow runs, and accessing GitHub API data with JSON output support

**2. Tavily Search Skill (tavily-search)**
- Description: Web search integration using Tavily AI API optimized for AI agents with clean, relevant results
- Install Command: Requires `TAVILY_API_KEY` environment variable and `pip install tavily-python`
- Use Case: Getting up-to-date information from the web with AI-generated answers, topic filtering, and time-based search

**3. Self-Improvement Skill (self-improving-agent)**
- Description: Captures learnings, errors, and corrections to enable continuous improvement of the agent
- Install Command: `clawdhub install self-improving-agent` or manual installation
- Use Case: Documenting mistakes and lessons learned to prevent repeating them in future interactions; promotes valuable learnings to project memory files

**4. Obsidian Skill (obsidian)**
- Description: Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli
- Install Command: `brew install yakitrak/yakitrak/obsidian-cli` (requires Homebrew)
- Use Case: Managing Obsidian notes, searching content, creating/moving/deleting notes while maintaining wikilinks

**5. Voice Call Skill (voice-call)**
- Description: Start voice calls via the OpenClaw voice-call plugin using Twilio, Telnyx, Plivo, or mock provider
- Install Command: Requires plugin configuration in openclaw.json with provider credentials
- Use Case: Making automated voice calls for notifications, reminders, or interactive voice responses

**6. Additional System Skills Found:**
- **apple-reminders**: Integration with Apple Reminders app
- **trello**: Trello board and card management
- **openai-image-gen**: OpenAI image generation capabilities
- **wacli**: WhatsApp CLI integration
- **goplaces**: Google Places API integration
- **blucli**: Bluetooth device control
- **xurl**: URL handling and processing
- **skill-creator**: Create, edit, and audit AgentSkills

**Skill Structure and Installation:**
- Skills are stored as directories containing a SKILL.md file with metadata
- Two main locations: user workspace (~/.openclaw/workspace/skills/) and system-wide (/usr/lib/node_modules/openclaw/skills/)
- Installation methods include ClawHub CLI, package managers (brew, pip), and manual copying
- Skills declare requirements (environment variables, binaries, config) in metadata

**Common Skill Categories:**
- Productivity & Task Management
- Communication & Messaging
- Development & Git Tools
- Web & API Integrations
- Media & Content Generation
- System & Device Control


## Search #3 - March 13, 2026 (5:24 AM Asia/Shanghai)

### Sources:
- Local OpenClaw workspace skills directory
- System-wide OpenClaw skills directory (/usr/lib/node_modules/openclaw/skills/)
- GitHub repositories and documentation

### Key Findings:

**1. Obsidian Integration Skill (obsidian)**
- Description: Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli
- Install Command: `brew install yakitrak/yakitrak/obsidian-cli` (requires obsidian-cli)
- Use Case: Managing and automating Obsidian note-taking workflows, searching content, creating/moving notes with proper link updates

**2. Voice Call Skill (voice-call)**
- Description: Start voice calls via the OpenClaw voice-call plugin using Twilio, Telnyx, Plivo, or mock provider
- Install Command: Enable in OpenClaw config (`plugins.entries.voice-call.enabled: true`)
- Use Case: Agent-initiated phone calls for notifications, reminders, or interactive voice responses

**3. Self-Improvement Skill (self-improving-agent)**
- Description: Captures learnings, errors, and corrections to enable continuous improvement of the agent
- Install Command: `clawdhub install self-improving-agent` or manual installation
- Use Case: Documenting mistakes and lessons learned to prevent repeating them in future interactions

**4. GitHub Integration Skill (github)**
- Description: Interact with GitHub using the `gh` CLI for issues, PRs, CI runs, and advanced queries
- Install Command: Manual installation to ~/.openclaw/workspace/skills/
- Use Case: Automating GitHub workflows like checking PR status, listing workflow runs, and accessing GitHub API data

**5. Tavily Search Skill (tavily-search)**
- Description: Web search integration using Tavily API for current information retrieval with AI-generated answers
- Install Command: Set TAVILY_API_KEY environment variable and `pip install tavily-python`
- Use Case: Getting up-to-date information from the web when the base model's knowledge is insufficient

**6. Additional System Skills Found:**
- **apple-reminders**: Integration with Apple Reminders app
- **trello**: Trello board and card management
- **openai-image-gen**: OpenAI image generation capabilities
- **wacli**: WhatsApp CLI integration
- **goplaces**: Google Places API integration
- **blucli**: Bluetooth device management
- **xurl**: URL handling and processing
- **skill-creator**: Create, edit, and improve AgentSkills

**Skill Structure and Installation:**
- Skills are stored in either `~/.openclaw/workspace/skills/` (user-specific) or `/usr/lib/node_modules/openclaw/skills/` (system-wide)
- Each skill contains a SKILL.md file with metadata including name, description, requirements, and installation instructions
- Installation methods vary by skill: some use ClawHub CLI, others require manual setup or system package managers
- Skills can declare dependencies on binaries, environment variables, or OpenClaw plugin configurations

**Skill Categories Available:**
- Productivity & Task Management (Apple Reminders, Trello)
- Communication (Voice Calls, WhatsApp)
- Development & Git (GitHub)
- Research & Information (Tavily Search, Obsidian)
- Media & APIs (OpenAI Image Generation, Google Places)
- System Integration (Bluetooth, URL handling)
- Skill Development (Skill Creator)


## Search #4 - March 13, 2026 (5:50 AM Asia/Shanghai)

### Found Skills:

**1. openclaw-skills-setup-cn**
- **Description**: ClawHub 安装与配置 | ClawHub setup. 帮助中文用户安装 ClawHub、配置镜像（如阿里云）、找技能（发现/推荐）、以及技能的安装/更新/启用/禁用。
- **Install Command**: `clawhub install openclaw-skills-setup-cn`
- **Use Case**: Installing and configuring ClawHub for Chinese users, finding and managing skills
- **Owner**: binbin
- **Source**: ClawHub Registry

**2. openclaw-ops-skills** 
- **Description**: Provides production-ready autonomous agent operations with cost optimization, task autonomy, persistent memory, security, and scheduled execution workflows.
- **Install Command**: `clawhub install openclaw-ops-skills`
- **Use Case**: Production operations, cost optimization, autonomous task execution, security monitoring
- **Owner**: Erich1566
- **Source**: ClawHub Registry

**3. clawops**
- **Description**: The orchestration tool for OpenClaw, managing and coordinating all your skills seamlessly.
- **Install Command**: `clawhub install clawops`
- **Use Case**: Skill orchestration and coordination across multiple OpenClaw instances
- **Owner**: okoddcat
- **Source**: ClawHub Registry

**4. clawdex**
- **Description**: Clawdex by Koi - Skill discovery and indexing tool
- **Install Command**: `clawhub install clawdex`
- **Use Case**: Discovering and indexing available skills in the ecosystem
- **Source**: ClawHub Registry

**5. openclaw-server-secure-skill**
- **Description**: Security-focused skill for OpenClaw server deployments
- **Install Command**: `clawhub install openclaw-server-secure-skill`
- **Use Case**: Securing OpenClaw server installations and configurations
- **Source**: ClawHub Registry

**Additional Resources Found:**
- **GitHub Repository**: [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - Collection of 5,400+ OpenClaw skills
- **GitHub Repository**: [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) - Community collection of OpenClaw use cases
- **ClawHub CLI**: Available via npm installation for skill management

*Note: Skills can be installed using the ClawHub CLI. Local installation requires: `npm install clawhub` then use `npx clawhub` commands.*


## Search #7 - March 13, 2026 (5:50 AM Asia/Shanghai)

### Skills Found via ClawHub Registry Search

**1. openclaw-skills-setup-cn**
- **Description**: ClawHub 安装与配置 | ClawHub setup. 帮助中文用户安装 ClawHub、配置镜像（如阿里云）、找技能（发现/推荐）、以及技能的安装/更新/启用/禁用。
- **Install Command**: `clawhub install openclaw-skills-setup-cn`
- **Use Case**: Installing clawhub, configuring mirrors for Chinese users, discovering skills
- **Owner**: binbin
- **Latest Version**: 1.0.0
- **Source**: ClawHub Registry (searched March 13, 2026)

**2. openclaw-ops-skills**
- **Description**: Provides production-ready autonomous agent operations with cost optimization, task autonomy, persistent memory, security, and scheduled execution workflows.
- **Install Command**: `clawhub install openclaw-ops-skills`
- **Use Case**: Production deployment of OpenClaw agents with operational best practices
- **Owner**: Erich1566
- **Latest Version**: 1.0.0
- **Source**: ClawHub Registry (searched March 13, 2026)

**3. clawops**
- **Description**: The orchestration tool for OpenClaw, managing and coordinating all your skills seamlessly.
- **Install Command**: `clawhub install clawops`
- **Use Case**: Skill orchestration and coordination across multiple OpenClaw instances
- **Owner**: okoddcat
- **Latest Version**: 1.0.0
- **Source**: ClawHub Registry (searched March 13, 2026)

**4. clawdex**
- **Description**: Clawdex by Koi
- **Install Command**: `clawhub install clawdex`
- **Use Case**: Unknown (limited metadata available)
- **Source**: ClawHub Registry (searched March 13, 2026)

**5. openclaw-server-secure-skill**
- **Description**: openclaw-server-secure-skill
- **Install Command**: `clawhub install openclaw-server-secure-skill`
- **Use Case**: Server security for OpenClaw deployments
- **Source**: ClawHub Registry (searched March 13, 2026)

**Additional Resources Found:**
- **Awesome OpenClaw Skills Repository**: https://github.com/VoltAgent/awesome-openclaw-skills - Collection of 5,400+ OpenClaw skills
- **OpenClaw Use Cases Repository**: https://github.com/hesamsheikh/awesome-openclaw-usecases - Community collection of OpenClaw use cases
- **Official OpenClaw Repository**: https://github.com/openclaw/openclaw - Main OpenClaw AI assistant project

**Note**: ClawHub CLI must be installed locally (`npm install clawhub`) to access these skills. Global installation may require elevated permissions.

**Search #6: OpenClaw Skills Discovery**
**Timestamp**: Friday, March 13th, 2026 — 6:20 AM (Asia/Shanghai)

**New Skills Found:**

**1. openclaw-console**
- **Description**: OpenClaw 可视化管理后台 - 配置管理、模型配置、Skills管理 (OpenClaw visual management console - configuration management, model configuration, and Skills management)
- **Install Command**: Clone from GitHub: `git clone https://github.com/xigpz/openclaw-console`
- **Use Case**: Web-based interface for managing OpenClaw configurations and skills
- **Source**: GitHub (searched March 13, 2026)

**2. awesome-openclaw-skills (natan89)**
- **Description**: Discover over 1715 community-driven OpenClaw skills, sorted by category, to enhance your projects and streamline your workflow
- **Install Command**: Clone from GitHub: `git clone https://github.com/natan89/awesome-openclaw-skills`
- **Use Case**: Comprehensive collection of community-created OpenClaw skills organized by category
- **Source**: GitHub (searched March 13, 2026)

**3. angela-skills-quest**
- **Description**: OpenClaw skills repository
- **Install Command**: Clone from GitHub: `git clone https://github.com/changjess1106-cloud/angela-skills-quest`
- **Use Case**: Collection of OpenClaw skills for Angela AI assistant
- **Source**: GitHub (searched March 13, 2026)

**4. CraigClaw**
- **Description**: Craig's OpenClaw workspace — personality, memory, skills, and deployment for Merit-Systems' AI agent
- **Install Command**: Clone from GitHub: `git clone https://github.com/Merit-Systems/CraigClaw`
- **Use Case**: Complete OpenClaw workspace configuration including skills, personality, and deployment settings
- **Source**: GitHub (searched March 13, 2026)

**5. openclaw-codex-pm-skills**
- **Description**: OpenClaw skills for Codex project management
- **Install Command**: Clone from GitHub: `git clone https://github.com/sonwr/openclaw-codex-pm-skills`
- **Use Case**: Project management related skills for OpenClaw integration with Codex
- **Source**: GitHub (searched March 13, 2026)

**Additional Information:**
- Local OpenClaw installation includes built-in skills like weather, github, healthcheck, etc.
- ClawHub CLI (`npm install -g clawhub`) can be used to search, install, and manage skills from the ClawHub registry
- Skills follow a standard structure with SKILL.md files containing metadata, description, and usage instructions
- Most skills require specific CLI tools to be installed (e.g., gh for GitHub skill, curl for weather skill)

**Note**: Some repositories may be experimental or personal projects. Verify compatibility and security before installing skills from unknown sources.

**Search #6: OpenClaw Skills Discovery**
**Timestamp**: Friday, March 13th, 2026 — 6:24 AM (Asia/Shanghai)

**Newly Discovered Skills & Resources:**

**1. openclaw-console**
- **Description**: OpenClaw 可视化管理后台 - 配置管理、模型配置、Skills管理 (OpenClaw visual management console - configuration management, model configuration, and Skills management)
- **Install Command**: Clone from GitHub repository
- **Use Case**: Web-based interface for managing OpenClaw configurations and skills
- **Source**: https://github.com/xigpz/openclaw-console

**2. awesome-openclaw-skills (natan89)**
- **Description**: Discover over 1715 community-driven OpenClaw skills, sorted by category, to enhance your projects and streamline your workflow
- **Install Command**: Clone from GitHub repository or use clawhub CLI if available
- **Use Case**: Comprehensive collection of community-created OpenClaw skills organized by category
- **Source**: https://github.com/natan89/awesome-openclaw-skills

**3. angela-skills-quest**
- **Description**: OpenClaw skills repository
- **Install Command**: Clone from GitHub repository
- **Use Case**: Collection of OpenClaw skills for various tasks
- **Source**: https://github.com/changjess1106-cloud/angela-skills-quest

**4. CraigClaw**
- **Description**: Craig's OpenClaw workspace — personality, memory, skills, and deployment for Merit-Systems' AI agent
- **Install Command**: Clone from GitHub repository
- **Use Case**: Complete OpenClaw workspace example with personality, memory, and skills implementation
- **Source**: https://github.com/Merit-Systems/CraigClaw

**5. openclaw-codex-pm-skills**
- **Description**: OpenClaw skills focused on project management and Codex integration
- **Install Command**: Clone from GitHub repository
- **Use Case**: Project management capabilities within OpenClaw environment
- **Source**: https://github.com/sonwr/openclaw-codex-pm-skills

**Additional Notes:**
- The ClawHub CLI (`npm install -g clawhub`) appears to be the official way to install and manage OpenClaw skills
- Local OpenClaw installation already contains many built-in skills in `/usr/lib/node_modules/openclaw/skills/`
- Most discovered repositories appear to be community-driven collections rather than official OpenClaw organization repositories
- Skills follow a standard structure with SKILL.md files containing metadata, description, and usage instructions

**Sources**: GitHub search results, web searches, and local OpenClaw installation analysis

**6. OpenClaw Skills Discovery - March 13, 2026**
- **Timestamp**: 2026-03-13 06:50:00 Asia/Shanghai
- **Keywords Searched**: 'OpenClaw skills', 'clawdhub skills', 'OpenClaw integrations', 'OpenClaw plugins'

**Key Findings:**

**1. VoltAgent/awesome-openclaw-skills**
- **Description**: Community-curated collection of 5,400+ OpenClaw skills filtered and categorized from the official OpenClaw Skills Registry
- **Install Command**: `git clone https://github.com/VoltAgent/awesome-openclaw-skills.git`
- **Use Case**: Comprehensive reference for discovering available OpenClaw skills across categories
- **Source**: https://github.com/VoltAgent/awesome-openclaw-skills

**2. ClawHub CLI (Official Skills Registry)**
- **Description**: Official command-line tool for searching, installing, updating, and publishing OpenClaw agent skills from clawhub.com
- **Install Command**: `npm install -g clawhub`
- **Use Case**: Centralized management of OpenClaw skills including version control, updates, and publishing
- **Source**: Local skill documentation (`/usr/lib/node_modules/openclaw/skills/clawhub/SKILL.md`)

**3. hesamsheikh/awesome-openclaw-usecases**
- **Description**: Community collection of practical OpenClaw use cases for productivity and automation
- **Install Command**: `git clone https://github.com/hesamsheikh/awesome-openclaw-usecases.git`
- **Use Case**: Real-world examples and implementation patterns for OpenClaw agents
- **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

**4. qwibitai/nanoclaw**
- **Description**: Lightweight OpenClaw alternative that runs in containers with built-in messaging app integration (WhatsApp, Telegram, Slack, Discord, Gmail)
- **Install Command**: `git clone https://github.com/qwibitai/nanoclaw.git`
- **Use Case**: Secure, containerized OpenClaw deployment with multi-platform messaging support
- **Source**: https://github.com/qwibitai/nanoclaw

**5. farion1231/cc-switch**
- **Description**: Cross-platform desktop All-in-One assistant tool supporting OpenClaw alongside Claude Code, Codex, OpenCode, and Gemini CLI
- **Install Command**: `git clone https://github.com/farion1231/cc-switch.git`
- **Use Case**: Unified interface for multiple AI assistant frameworks including OpenClaw
- **Source**: https://github.com/farion1231/cc-switch

**Additional Notes:**
- The term "clawdhub" appears to be a typo; the correct term is "ClawHub" (clawhub.com)
- OpenClaw has an extensive built-in skill ecosystem with 50+ pre-installed skills in standard installations
- Skills follow standardized structure with SKILL.md metadata files containing installation and usage instructions
- Community repositories focus on skill collections, use cases, and alternative implementations rather than individual skills
- The official OpenClaw repository (openclaw/openclaw) serves as the core framework

**Sources**: GitHub search results, local OpenClaw installation analysis, web searches via Perplexity

**6. VoltAgent/awesome-openclaw-skills**
- **Description**: The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry
- **Install Command**: Clone from GitHub repository or use ClawHub CLI (`npm install -g clawhub`)
- **Use Case**: Comprehensive repository of community-contributed OpenClaw skills for various purposes
- **Source**: https://github.com/VoltAgent/awesome-openclaw-skills

**7. ClawHub CLI**
- **Description**: Official CLI tool to search, install, update, and publish agent skills from clawhub.com registry
- **Install Command**: `npm install -g clawhub`
- **Use Case**: Centralized skill management system for OpenClaw - discover, install, and share skills
- **Source**: Built-in skill in `/usr/lib/node_modules/openclaw/skills/clawhub/SKILL.md`

**8. hesamsheikh/awesome-openclaw-usecases**
- **Description**: Community collection of OpenClaw use cases for making life easier
- **Install Command**: Clone from GitHub repository
- **Use Case**: Practical examples and implementations of OpenClaw for real-world automation tasks
- **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

**9. qwibitai/nanoclaw**
- **Description**: Lightweight alternative to OpenClaw that runs in containers for security, connects to multiple messaging platforms
- **Install Command**: Clone from GitHub repository
- **Use Case**: Secure, containerized OpenClaw alternative with messaging integrations (WhatsApp, Telegram, Slack, Discord, Gmail)
- **Source**: https://github.com/qwibitai/nanoclaw

**10. farion1231/cc-switch**
- **Description**: Cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI
- **Install Command**: Clone from GitHub repository
- **Use Case**: Unified interface for multiple AI assistant frameworks including OpenClaw
- **Source**: https://github.com/farion1231/cc-switch

**Timestamp**: Friday, March 13th, 2026 — 6:50 AM (Asia/Shanghai)
**Sources**: GitHub search results, local OpenClaw installation analysis, and web searches

**6. OpenClaw Skills Discovery - March 13, 2026 06:52 CST**
- **VoltAgent/awesome-openclaw-skills**: The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞
  - **Description**: Comprehensive curated collection of OpenClaw skills from the official registry
  - **Install Command**: Clone repository or use ClawHub CLI (`npm install -g clawhub`)
  - **Use Case**: Access to thousands of pre-built skills for various integrations and capabilities
  - **Source**: https://github.com/VoltAgent/awesome-openclaw-skills

- **ClawHub CLI**: Official OpenClaw skills management tool
  - **Description**: Command-line interface for searching, installing, updating, and publishing OpenClaw skills from clawhub.com
  - **Install Command**: `npm install -g clawhub`
  - **Use Case**: Manage skill lifecycle, sync with latest versions, publish custom skills
  - **Source**: Built-in skill in `/usr/lib/node_modules/openclaw/skills/clawhub/`

- **hesamsheikh/awesome-openclaw-usecases**: Community collection of OpenClaw use cases
  - **Description**: Real-world examples and patterns for implementing OpenClaw solutions
  - **Install Command**: Clone repository for reference
  - **Use Case**: Learning practical applications and best practices
  - **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

- **Local Skills Repository**: Extensive built-in skills library
  - **Description**: 50+ built-in skills covering messaging (Discord, Slack, WhatsApp), productivity (Notion, Obsidian, GitHub), media (Spotify, Sonos), development (coding-agent, gh-issues), and utilities (weather, healthcheck)
  - **Install Command**: Pre-installed with OpenClaw
  - **Use Case**: Immediate access to common integrations without additional setup
  - **Source**: Local installation at `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`

**Key Findings**:
- ClawHub (not "clawdhub") is the official skills registry and CLI tool for OpenClaw
- Skills follow standardized structure with SKILL.md metadata files
- Community repositories provide extensive collections beyond built-in skills
- Most skills are designed for agent capabilities like messaging, APIs, file operations, and external service integration

**Sources**: GitHub search (March 13, 2026), local OpenClaw installation analysis, web search via Perplexity

## Search #8 - March 13, 2026 (7:20 AM Asia/Shanghai)

**Keywords**: 'OpenClaw skills', 'clawdhub skills', 'OpenClaw integrations', 'OpenClaw plugins'

**Findings**:

- **hesamsheikh/awesome-openclaw-usecases**: Community collection of OpenClaw use cases
  - **Description**: Real-world examples and patterns for implementing OpenClaw solutions
  - **Install Command**: Clone repository for reference
  - **Use Case**: Learning practical applications and best practices
  - **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

- **Local Skills Repository**: Extensive built-in skills library
  - **Description**: 50+ built-in skills covering messaging (Discord, Slack, WhatsApp), productivity (Notion, Obsidian, GitHub), media (Spotify, Sonos), development (coding-agent, gh-issues), and utilities (weather, healthcheck)
  - **Install Command**: Pre-installed with OpenClaw
  - **Use Case**: Immediate access to common integrations without additional setup
  - **Source**: Local installation at `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`

**Key Findings**:
- ClawHub (not "clawdhub") is the official skills registry and CLI tool for OpenClaw
- Skills follow standardized structure with SKILL.md metadata files
- Community repositories provide extensive collections beyond built-in skills
- Most skills are designed for agent capabilities like messaging, APIs, file operations, and external service integration

**Sources**: GitHub search (March 13, 2026), local OpenClaw installation analysis, web search via Perplexity

## Search #8 - March 13, 2026 (7:20 AM Asia/Shanghai)

**Search Keywords**: 'OpenClaw skills', 'clawdhub skills', 'OpenClaw integrations', 'OpenClaw plugins'

**Findings**:

- **hesamsheikh/awesome-openclaw-usecases**: Community collection of OpenClaw use cases
  - **Description**: Real-world examples and patterns for implementing OpenClaw solutions
  - **Install Command**: Clone repository for reference
  - **Use Case**: Learning practical applications and best practices
  - **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

- **Local Skills Repository**: Extensive built-in skills library
  - **Description**: 50+ built-in skills covering messaging (Discord, Slack, WhatsApp), productivity (Notion, Obsidian, GitHub), media (Spotify, Sonos), development (coding-agent, gh-issues), and utilities (weather, healthcheck)
  - **Install Command**: Pre-installed with OpenClaw
  - **Use Case**: Immediate access to common integrations without additional setup
  - **Source**: Local installation at `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`

**Key Findings**:
- ClawHub (not "clawdhub") is the official skills registry and CLI tool for OpenClaw
- Skills follow standardized structure with SKILL.md metadata files
- Community repositories provide extensive collections beyond built-in skills
- Most skills are designed for agent capabilities like messaging, APIs, file operations, and external service integration

**Sources**: GitHub search (March 13, 2026), local OpenClaw installation analysis, web search via Perplexity

## Search #8 - March 13, 2026 (07:20 AM Asia/Shanghai)

- **ClawHub Skills Registry**: Official OpenClaw skills marketplace and CLI tool
  - **Description**: Centralized registry for discovering, installing, and managing OpenClaw skills with standardized metadata
  - **Install Command**: `npm install -g clawhub` or use built-in `clawhub` CLI
  - **Use Case**: Finding and installing community-created skills for extending OpenClaw capabilities
  - **Source**: https://github.com/openclaw/clawhub

- **OpenClaw Built-in Skills Library**: Comprehensive local skills collection
  - **Description**: 50+ pre-installed skills covering messaging (Discord, Slack, WhatsApp), productivity (Notion, Obsidian, GitHub), media (Spotify, Sonos), development (coding-agent, gh-issues), and utilities (weather, healthcheck, agent-reach)
  - **Install Command**: Pre-installed with OpenClaw at `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`
  - **Use Case**: Immediate access to common integrations without additional setup
  - **Source**: Local OpenClaw installation

- **hesamsheikh/awesome-openclaw-usecases**: Community examples repository
  - **Description**: Real-world implementation patterns and use cases for OpenClaw agents
  - **Install Command**: `git clone https://github.com/hesamsheikh/awesome-openclaw-usecases.git`
  - **Use Case**: Learning practical applications and best practices from community examples
  - **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

**Key Findings**:
- "ClawHub" (not "clawdhub") is the official skills registry and discovery platform
- Skills follow standardized SKILL.md format with name, description, and usage instructions
- Most valuable skills focus on external service integration, messaging platforms, and productivity tools
- Community repositories complement the extensive built-in skills library

**Sources**: GitHub repository search, local OpenClaw installation analysis, web search via Perplexity (March 13, 2026)

## Search #9 - March 13, 2026 (07:20 AM Asia/Shanghai)

- **ClawHub Skills Registry**: Official OpenClaw skills marketplace and CLI tool
  - **Description**: Centralized registry for discovering, installing, and managing OpenClaw skills with standardized metadata
  - **Install Command**: `npm install -g clawhub` or use built-in `clawhub` CLI
  - **Use Case**: Finding and installing community-created skills for extending OpenClaw capabilities
  - **Source**: https://github.com/openclaw/clawhub

- **OpenClaw Built-in Skills Library**: Comprehensive local skills collection
  - **Description**: 50+ pre-installed skills covering messaging (Discord, Slack, WhatsApp), productivity (Notion, Obsidian, GitHub), media (Spotify, Sonos), development (coding-agent, gh-issues), and utilities (weather, healthcheck, agent-reach)
  - **Install Command**: Pre-installed with OpenClaw at `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`
  - **Use Case**: Immediate access to common integrations without additional setup
  - **Source**: Local OpenClaw installation

- **hesamsheikh/awesome-openclaw-usecases**: Community examples repository
  - **Description**: Real-world implementation patterns and use cases for OpenClaw agents
  - **Install Command**: `git clone https://github.com/hesamsheikh/awesome-openclaw-usecases.git`
  - **Use Case**: Learning practical applications and best practices from community examples
  - **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

**Key Findings**:
- ClawHub (not "clawdhub") is the official skills registry and CLI tool for OpenClaw
- Skills follow standardized structure with SKILL.md metadata files
- Community repositories provide extensive collections beyond built-in skills
- Most skills are designed for agent capabilities like messaging, APIs, file operations, and external service integration

**Sources**: GitHub search results, local OpenClaw installation analysis, web search via Perplexity (March 13, 2026)

## Search #9 - March 13, 2026 (07:20 AM Asia/Shanghai)

- **ClawHub Skills Registry**: Official OpenClaw skills marketplace and CLI tool
  - **Description**: Centralized registry for discovering, installing, and managing OpenClaw skills with standardized metadata
  - **Install Command**: `npm install -g clawhub` or use built-in `clawhub` CLI
  - **Use Case**: Finding and installing community-created skills for extending OpenClaw capabilities
  - **Source**: https://github.com/openclaw/clawhub

- **OpenClaw Built-in Skills Library**: Comprehensive local skills collection
  - **Description**: 50+ pre-installed skills covering messaging (Discord, Slack, WhatsApp), productivity (Notion, Obsidian, GitHub), media (Spotify, Sonos), development (coding-agent, gh-issues), and utilities (weather, healthcheck, agent-reach)
  - **Install Command**: Pre-installed with OpenClaw at `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`
  - **Use Case**: Immediate access to common integrations without additional setup
  - **Source**: Local OpenClaw installation

- **hesamsheikh/awesome-openclaw-usecases**: Community examples repository
  - **Description**: Real-world implementation patterns and use cases for OpenClaw agents
  - **Install Command**: `git clone https://github.com/hesamsheikh/awesome-openclaw-usecases.git`
  - **Use Case**: Learning practical applications and best practices from community examples
  - **Source**: https://github.com/hesamsheikh/awesome-openclaw-usecases

**Key Findings**:
- Correct term is "ClawHub" not "clawdhub" - it's the official skills registry and CLI tool
- Skills follow standardized structure with SKILL.md metadata files
- Extensive built-in skills available locally without additional installation
- Community repositories provide real-world implementation examples

**Sources**: GitHub search, local OpenClaw installation analysis, web search via Perplexity (March 13, 2026)

## Search #10 - March 13, 2026 (7:50 AM Asia/Shanghai)

### Sources:
- GitHub repositories: zhaog100/openclaw-skills, froma1976/openclaw-trading-skills, xigpz/openclaw-console
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"
- Local OpenClaw installation skill directories

### Key Findings:

**1. OpenClaw Built-in Skills Collection**
- Description: Official OpenClaw skills included with the installation, covering various domains like GitHub integration, health checks, weather, MCP server tools, and more
- Install Command: Pre-installed with OpenClaw at `/usr/lib/node_modules/openclaw/skills/`
- Use Case: Core functionality for OpenClaw agents including system management, API integrations, and productivity tools

**2. User-Created Skills (zhaog100/openclaw-skills)**
- Description: Community collection of OpenClaw skills by miliger
- Install Command: Clone repository to `~/.agents/skills/` or `~/.openclaw/workspace/skills/`
- Use Case: Extending OpenClaw with custom functionality beyond the built-in skills

**3. Trading Skills (froma1976/openclaw-trading-skills)**
- Description: Specialized skills for trading and financial analysis in OpenClaw
- Install Command: Clone repository to skill directory
- Use Case: Financial market analysis, trading automation, and portfolio management

**4. OpenClaw Console (xigpz/openclaw-console)**
- Description: Visual management console for OpenClaw with configuration management, model settings, and Skills management
- Install Command: Clone and follow repository setup instructions
- Use Case: GUI-based management of OpenClaw configuration and skills

**5. Agent Reach Skill**
- Description: Gives AI agents access to various internet platforms (Twitter/X, Reddit, YouTube, GitHub, etc.)
- Install Command: Available in local installation at `~/.agents/skills/agent-reach/`
- Use Case: Enabling agents to interact with social media and content platforms

**6. China Stock Analysis Skills**
- Description: Specialized skills for A-share market analysis using akshare data
- Install Command: Available in local installation at `~/.agents/skills/china-stock-analysis/` and `~/.agents/skills/akshare-stock/`
- Use Case: Chinese stock market analysis, technical indicators, and fundamental analysis


## Search #11 - March 13, 2026 (7:50 AM Asia/Shanghai)

### Sources:
- GitHub repositories: zhaog100/openclaw-skills, froma1976/openclaw-trading-skills, xigpz/openclaw-console
- Local OpenClaw installation skill directories
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

### Key Findings:

**1. OpenClaw Skills Collection (zhaog100/openclaw-skills)**
- Description: Community collection of OpenClaw skills by miliger
- Install Command: Clone repository to ~/.agents/skills/ directory
- Use Case: Various utility skills for extending OpenClaw functionality

**2. Trading Skills (froma1976/openclaw-trading-skills)**
- Description: Specialized skills for trading and financial analysis in OpenClaw
- Install Command: Clone repository to skill directory
- Use Case: Financial market analysis, trading automation, and portfolio management

**3. OpenClaw Console (xigpz/openclaw-console)**
- Description: Visual management console for OpenClaw with configuration management, model settings, and Skills management
- Install Command: Clone and follow repository setup instructions
- Use Case: GUI-based management of OpenClaw configuration and skills

**4. Built-in System Skills**
- Description: Official OpenClaw system skills installed in /usr/lib/node_modules/openclaw/skills/
- Examples: github, gh-issues, healthcheck, weather, mcporter, skill-creator, clawhub
- Use Case: Core functionality for GitHub integration, issue tracking, system health checks, weather data, MCP server integration, skill creation, and skill registry

**5. User-installed Skills**
- Description: Additional skills in user workspace (~/.agents/skills/ and ~/.openclaw/workspace/skills/)
- Examples: agent-reach, akshare-stock, china-stock-analysis, find-skills, vercel-* patterns, web-design-guidelines
- Use Case: Extended functionality for social media access, Chinese stock analysis, skill discovery, React development patterns, and web design compliance


**6. OpenClaw Skills Discovery (March 13, 2026 - 8:20 AM UTC)**
- Description: Comprehensive collection of OpenClaw skills from the official ClawHub registry
- Sources: 
  - GitHub Repository: VoltAgent/awesome-openclaw-skills
  - GitHub Search Results for "OpenClaw skills"
- Install Command: `clawhub install <skill-slug>` or manual installation by copying skill folders to ~/.agents/skills/
- Use Cases by Category:

**AI & LLMs (197 skills)**
- Examples: 4claw (moderated imageboard for AI agents), agent-church (identity formation via SOUL.md), agent-autonomy-kit (reduce prompt dependency)
- Use Case: Extending AI capabilities, identity management, and autonomous operation

**Coding Agents & IDEs (1223 skills)**
- Examples: academic-research (literature reviews via OpenAlex API), active-maintenance (automated system health), agent-audit (performance/cost/ROI analysis)
- Use Case: Development workflows, research automation, system maintenance, and performance optimization

**Git & GitHub (170 skills)**
- Examples: agent-team-orchestration (multi-agent workflows), arc-skill-gitops (automated deployment/version management), auto-pr-merger (GitHub PR automation)
- Use Case: Team collaboration, GitOps workflows, and automated repository management

**Additional Categories Available:**
- Browser & Automation (62K+ lines of documentation)
- Web & Frontend Development (177K+ lines)
- DevOps & Cloud (76K+ lines)
- Search & Research (66K+ lines)
- Productivity & Tasks (38K+ lines)
- Image & Video Generation (31K+ lines)
- Communication (26K+ lines)

Total Skills Available: 5,495+ community-built skills across 30+ categories

**6. OpenClaw Skills Discovery (March 13, 2026)**
- **Source**: GitHub repositories and web search
- **Timestamp**: 2026-03-13 08:20 AM (Asia/Shanghai)

**Key Findings**:

1. **Awesome OpenClaw Skills Repository** (VoltAgent/awesome-openclaw-skills)
   - Description: Comprehensive collection of 5,490+ community-built OpenClaw skills organized by category
   - Install Command: `clawhub install <skill-slug>` or manual copy to skill directory
   - Use Case: Discover and install specialized skills for various domains including AI/LLMs, coding, Git/GitHub, productivity, and more

2. **AI & LLMs Skills Category** (197 skills)
   - Notable Examples: 
     - agent-church: Identity formation for AI agents via SOUL.md
     - agent-autonomy-kit: Enables autonomous operation without constant prompting
     - adversarial-prompting: Adversarial analysis to critique and improve outputs
   - Use Case: Enhance AI capabilities, agent identity management, and prompt optimization

3. **Coding Agents & IDEs Category** (1,223 skills)
   - Notable Examples:
     - academic-research: Search academic papers using OpenAlex API
     - active-maintenance: Automated system health and memory metabolism
     - agent-audit: Audit AI agent setup for performance, cost, and ROI
   - Use Case: Development workflows, research automation, system maintenance, and performance monitoring

4. **Git & GitHub Category** (170 skills)
   - Notable Examples:
     - agent-team-orchestration: Multi-agent team coordination with defined roles
     - arc-skill-gitops: Automated deployment and version management for agent workflows
     - auto-pr-merger: Automates GitHub pull request merging workflow
   - Use Case: Team collaboration, GitOps workflows, and automated PR management

5. **Related Projects**:
   - ClawX: Desktop GUI for OpenClaw (ValueCell-ai/ClawX)
   - OpenViking: Context database for AI Agents (volcengine/OpenViking)
   - MemOS: AI memory OS for persistent skill memory (MemTensor/MemOS)

**Sources**:
- https://github.com/VoltAgent/awesome-openclaw-skills
- https://github.com/openclaw/openclaw
- GitHub search results for "OpenClaw skills"

Search #12 - Friday, March 13th, 2026 — 8:50 AM (Asia/Shanghai)
================================================================

**Research Summary**: Extensive searches for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", and "OpenClaw plugins" revealed limited public information about OpenClaw as an AI agent framework. Most search results relate to OpenClaw as a game engine reimplementation of the classic "Claw" game from 1997.

**Key Findings**:

1. **OpenClaw Game Engine Confusion**: The majority of search results refer to OpenClaw as an open-source reimplementation of the 1997 platformer game "Claw" by Monolith Productions, not an AI agent framework.

2. **No Established AI Framework**: There is no widely recognized AI agent framework named "OpenClaw" in the public domain as of 2026. This suggests OpenClaw may be:
   - A private/internal project
   - A custom implementation specific to this deployment
   - A niche or emerging framework without significant public documentation

3. **Local Skills Structure Identified**: Analysis of the local OpenClaw installation reveals a well-structured skills system with:
   - Skills stored in `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`
   - Standard SKILL.md format with YAML frontmatter (name, description)
   - Optional bundled resources (scripts/, references/, assets/)
   - Progressive disclosure design principle

4. **Existing Local Skills Examples**:
   - **github**: Interact with GitHub using `gh` CLI
   - **tavily-search**: Web search using Tavily AI API
   - **skill-creator**: Create/edit/audit AgentSkills
   - **weather**: Get weather via wttr.in or Open-Meteo
   - **healthcheck**: Host security hardening and risk assessment

**Recommendation**: Since OpenClaw appears to be a custom/local AI agent framework rather than a widely documented public project, focus discovery efforts on:
- Local skill directories (`/usr/lib/node_modules/openclaw/skills/`, `~/.agents/skills/`)
- Internal documentation and configuration files
- Direct inspection of existing skill implementations

**Sources**:
- Web search results for "OpenClaw skills clawdhub skills OpenClaw integrations OpenClaw plugins"
- Web search results for "OpenClaw AI agent skills framework plugins"
- Local filesystem analysis of OpenClaw installation
- Inspection of existing SKILL.md files in local installation


Search #12 - Friday, March 13th, 2026 — 8:50 AM (Asia/Shanghai)
============================================================

**Research Summary**: 
After extensive searching across GitHub and web sources, there appears to be limited public documentation or repositories specifically for "OpenClaw skills" as an AI agent framework. Most search results point to OpenClaw as a game reimplementation project rather than an AI agent platform.

**Key Findings**:

1. **OpenClaw Game Project**: The majority of references to "OpenClaw" relate to an open-source reimplementation of the 1997 platformer game "Claw" by ThirteenAG. This is unrelated to AI agent skills.

2. **AI Agent Framework Confusion**: No established AI agent framework named "OpenClaw" was found in public repositories or documentation as of March 2026.

3. **Possible Local/Internal Framework**: OpenClaw may be a local or internal AI agent framework used within your specific setup, which would explain why skills are stored locally in `/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`.

4. **Skill Structure Observed**: From examining existing local skills, OpenClaw skills follow this structure:
   - Required `SKILL.md` with YAML frontmatter (name, description)
   - Optional directories: `scripts/`, `references/`, `assets/`
   - Skills are triggered based on the description field in frontmatter
   - Environment variables stored in `~/.openclaw/.env`

5. **Existing Skill Categories Found Locally**:
   - GitHub integration skills
   - Weather and stock analysis skills  
   - Web search skills (Tavily, dashscope-websearch)
   - Health/security monitoring skills
   - Agent coordination and delegation skills

**Recommendation**: 
Since OpenClaw appears to be a custom/local AI agent framework, the most valuable skills discovery approach would be to:
- Continue exploring the local skill directories (`/usr/lib/node_modules/openclaw/skills/` and `~/.agents/skills/`)
- Check internal documentation or configuration files
- Monitor the OpenClaw GitHub organization if it exists privately

**Sources**:
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"
- Local filesystem exploration of existing skill directories
- Analysis of SKILL.md structure from existing skills


## Search #2 - March 13, 2026 (9:20 AM Asia/Shanghai)

### Sources:
- Local OpenClaw skill directories in /usr/lib/node_modules/openclaw/skills/
- GitHub repositories and documentation
- OpenClaw workspace skill directories

### Key Findings:

**1. ClawHub Integration Skill (clawhub)**
- Description: Centralized skill registry for OpenClaw that allows searching, installing, updating, and publishing agent skills from clawhub.com
- Install Command: `npm i -g clawhub` followed by `clawhub install <skill-slug>`
- Use Case: Primary method for discovering and managing OpenClaw skills with version control and centralized repository access

**2. GitHub Integration Skill (github)**
- Description: Comprehensive GitHub operations via `gh` CLI including issues, PRs, CI runs, code review, and API queries
- Install Command: `brew install gh` (macOS) or `apt install gh` (Linux), then `clawhub install github`
- Use Case: Managing GitHub repositories, automating PR reviews, checking CI status, and performing bulk GitHub operations

**3. Host Security Hardening Skill (healthcheck)**
- Description: Host security hardening and risk-tolerance configuration for OpenClaw deployments with firewall, SSH, and update hardening capabilities
- Install Command: Available by default in OpenClaw installation
- Use Case: Security audits, exposure reviews, periodic security checks, and system hardening for machines running OpenClaw

**4. Coding Agent Skill (coding-agent)**
- Description: Delegate coding tasks to Codex, Claude Code, or Pi agents via background processes with full development capabilities
- Install Command: Install preferred coding agent (e.g., `npm install -g @mariozechner/pi-coding-agent`) then use via `clawhub install coding-agent`
- Use Case: Building new features, reviewing PRs, refactoring codebases, and iterative development with AI coding assistants

**5. Additional Built-in Skills Found:**
- **mcporter**: MCP server integration for direct tool calling
- **weather**: Current weather and forecasts via wttr.in or Open-Meteo
- **self-improvement**: Captures learnings and corrections for continuous improvement
- **agent-reach**: Platform access configuration for Twitter/X, Reddit, YouTube, etc.
- **vercel-react-best-practices**: React/Next.js performance optimization guidelines
- **web-design-guidelines**: UI code review for accessibility and best practices compliance


## Search #2 - March 13, 2026 (9:23 AM Asia/Shanghai)

### Sources:
- Local OpenClaw skill directories in /usr/lib/node_modules/openclaw/skills/
- GitHub repositories and documentation
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

### Key Findings:

**1. ClawHub (clawhub)**
- Description: Public skill registry for OpenClaw that allows searching, installing, updating, and publishing agent skills from clawhub.com
- Install Command: `npm i -g clawhub` followed by `clawhub install <skill-slug>`
- Use Case: Centralized repository for discovering and managing OpenClaw skills with version control and publishing capabilities

**2. GitHub Integration (github)**
- Description: Interact with GitHub using the `gh` CLI for issues, PRs, CI runs, code review, and API queries
- Install Command: `brew install gh` (macOS) or `apt install gh` (Linux) followed by `gh auth login`
- Use Case: Managing GitHub repositories, checking PR status, creating issues, viewing CI logs, and querying GitHub API

**3. Host Security Hardening (healthcheck)**
- Description: Host security hardening and risk-tolerance configuration for OpenClaw deployments
- Install Command: Built-in skill (no separate installation required)
- Use Case: Security audits, firewall/SSH hardening, risk posture assessment, exposure review, and periodic security checks

**4. Coding Agent (coding-agent)**
- Description: Delegate coding tasks to Codex, Claude Code, or Pi agents via background process
- Install Command: Install desired coding agent (e.g., `npm install -g @mariozechner/pi-coding-agent` for Pi)
- Use Case: Building new features/apps, reviewing PRs, refactoring codebases, and iterative coding with file exploration

**5. MCP Server Integration (mcporter)**
- Description: Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio)
- Install Command: Built-in skill (no separate installation required)
- Use Case: Integrating with Model Context Protocol (MCP) servers for extended tool capabilities

**6. Self-Improvement (self-improvement)**
- Description: Captures learnings, errors, and corrections to enable continuous improvement
- Install Command: Built-in skill located at ~/.openclaw/workspace/skills/self-improving-agent/
- Use Case: Documenting mistakes, capturing user corrections, and improving recurring task approaches

**7. Weather Information (weather)**
- Description: Get current weather and forecasts via wttr.in or Open-Meteo
- Install Command: Built-in skill (no separate installation required)
- Use Case: Providing weather information, temperature, and forecasts for any location without API keys

**8. Skill Creator (skill-creator)**
- Description: Create, edit, improve, or audit AgentSkills
- Install Command: Built-in skill (no separate installation required)
- Use Case: Creating new skills from scratch or improving existing SKILL.md files and skill directories


## Search #2 - March 13, 2026 (9:23 AM Asia/Shanghai)

### Sources:
- Local OpenClaw skill directories in /usr/lib/node_modules/openclaw/skills/
- GitHub repositories and documentation
- OpenClaw workspace skill directories

### Key Findings:

**1. ClawHub (clawhub)**
- Description: Public skill registry for OpenClaw that allows publishing, versioning, and searching text-based agent skills with moderation and vector search capabilities
- Install Command: `npm i -g clawhub` followed by `clawhub install <skill-slug>`
- Use Case: Centralized repository for discovering and installing OpenClaw skills; supports search, update, and publish operations

**2. GitHub Integration Skill (github)**
- Description: Interact with GitHub using the `gh` CLI for issues, PRs, CI runs, code review, and API queries
- Install Command: `brew install gh` (macOS) or `apt install gh` (Linux) followed by `gh auth login`
- Use Case: Managing GitHub repositories, checking PR status, viewing CI logs, creating issues, and running API queries

**3. Host Security Hardening Skill (healthcheck)**
- Description: Host security hardening and risk-tolerance configuration for OpenClaw deployments with comprehensive security audits
- Install Command: Built-in skill (no separate installation required)
- Use Case: Security audits, firewall/SSH hardening, risk posture assessment, exposure review, and periodic security checks

**4. Coding Agent Skill (coding-agent)**
- Description: Delegate coding tasks to Codex, Claude Code, or Pi agents via background process with support for multiple AI coding models
- Install Command: Install preferred coding agent (`npm install -g codex`, `npm install -g claude`, etc.)
- Use Case: Building new features, reviewing PRs, refactoring codebases, and iterative coding with file exploration

**5. Additional Available Skills:**
- **mcporter**: MCP server integration for calling external tools directly
- **weather**: Current weather and forecasts via wttr.in or Open-Meteo
- **gh-issues**: Automated GitHub issue fetching and PR creation
- **agent-reach**: Internet access configuration for various platforms (Twitter, Reddit, YouTube, etc.)
- **self-improvement**: Captures learnings and corrections for continuous improvement
- **find-skills**: Helps discover and install agent skills
- **vercel-composition-patterns**: React composition patterns and best practices
- **web-design-guidelines**: UI code review for accessibility and design compliance

## Search #2 - March 13, 2026 (9:23 AM Asia/Shanghai)

### Sources:
- Local OpenClaw skill directories in /usr/lib/node_modules/openclaw/skills/
- Local workspace skills in ~/.openclaw/workspace/skills/
- GitHub repositories and documentation

### Key Findings:

**1. ClawHub Skill Registry (clawhub)**
- Description: Public skill registry for OpenClaw that allows searching, installing, updating, and publishing agent skills from clawhub.com
- Install Command: `npm i -g clawhub`
- Use Case: Centralized discovery and management of OpenClaw skills with versioning and authentication support

**2. GitHub Integration Skill (github)**
- Description: Comprehensive GitHub operations via `gh` CLI including issues, PRs, CI runs, code review, and API queries
- Install Command: `brew install gh` or `apt install gh`
- Use Case: Managing GitHub repositories, checking PR status, creating issues, viewing CI logs, and querying GitHub API

**3. Host Security Hardening Skill (healthcheck)**
- Description: Host security hardening and risk-tolerance configuration for OpenClaw deployments with comprehensive security audits
- Install Command: Built-in skill (no separate installation required)
- Use Case: Security audits, firewall/SSH hardening, risk posture assessment, exposure review, and periodic security checks

**4. Coding Agent Skill (coding-agent)**
- Description: Delegate coding tasks to Codex, Claude Code, or Pi agents via background process with support for multiple AI coding models
- Install Command: Install preferred coding agent (`npm install -g codex`, `npm install -g claude`, etc.)
- Use Case: Building new features, reviewing PRs, refactoring codebases, and iterative coding with file exploration

**5. Additional Available Skills:**
- **mcporter**: MCP server integration for calling external tools directly
- **weather**: Current weather and forecasts via wttr.in or Open-Meteo  
- **gh-issues**: Automated GitHub issue fetching and PR creation
- **agent-reach**: Internet access configuration for various platforms (Twitter, Reddit, YouTube, etc.)
- **self-improvement**: Captures learnings and corrections for continuous improvement
- **find-skills**: Helps discover and install agent skills
- **vercel-composition-patterns**: React composition patterns and best practices
- **web-design-guidelines**: UI code review for accessibility and design compliance


## Search #13 - March 13, 2026 (9:20 AM Asia/Shanghai)

### Sources:
- Local OpenClaw skill directories in /usr/lib/node_modules/openclaw/skills/
- Local workspace skills in ~/.openclaw/workspace/skills/ and ~/.agents/skills/
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

### Key Findings:

**1. ClawHub Skill Registry (clawhub)**
- Description: Public skill registry for OpenClaw that allows searching, installing, updating, and publishing agent skills from clawhub.com with moderation and vector search capabilities
- Install Command: `npm i -g clawhub` followed by `clawhub install <skill-slug>`
- Use Case: Centralized discovery and management of OpenClaw skills with versioning, authentication, and publishing support

**2. GitHub Integration Skill (github)**
- Description: Comprehensive GitHub operations via `gh` CLI including issues, PRs, CI runs, code review, and advanced API queries with JSON output support
- Install Command: `brew install gh` (macOS) or `apt install gh` (Linux) followed by `gh auth login`
- Use Case: Managing GitHub repositories, checking PR status and CI logs, creating/commenting on issues, and querying GitHub API with structured output

**3. Host Security Hardening Skill (healthcheck)**
- Description: Host security hardening and risk-tolerance configuration for OpenClaw deployments with comprehensive security audits, firewall assessment, and system hardening
- Install Command: Built-in skill (no separate installation required)
- Use Case: Security audits, firewall/SSH hardening, risk posture assessment, exposure review, OpenClaw cron scheduling for periodic checks, and version status verification

**4. Coding Agent Skill (coding-agent)**
- Description: Delegate coding tasks to Codex, Claude Code, or Pi agents via background process with support for multiple AI coding models and PTY requirements
- Install Command: Install preferred coding agent (`npm install -g codex`, `npm install -g claude`, `npm install -g @mariozechner/pi-coding-agent`, etc.)
- Use Case: Building new features/apps, reviewing PRs in isolated environments, refactoring large codebases, and iterative coding with file exploration

**5. MCP Server Integration Skill (mcporter)**
- Description: Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio) including ad-hoc servers and config edits
- Install Command: Built-in skill (no separate installation required)
- Use Case: Integrating with Model Context Protocol (MCP) servers for extended tool capabilities, calling external APIs, and managing MCP server configurations

**6. Self-Improvement Skill (self-improvement)**
- Description: Captures learnings, errors, and corrections to enable continuous improvement of the agent through documentation and memory updates
- Install Command: Built-in skill located at ~/.openclaw/workspace/skills/self-improving-agent/
- Use Case: Documenting mistakes, capturing user corrections, handling external API failures, and improving approaches for recurring tasks

**7. Weather Information Skill (weather)**
- Description: Get current weather and forecasts via wttr.in or Open-Meteo without requiring API keys
- Install Command: Built-in skill (no separate installation required)
- Use Case: Providing weather information, temperature, and forecasts for any location with simple natural language queries

**8. Additional Notable Skills:**
- **agent-reach**: Platform access configuration for Twitter/X, Reddit, YouTube, GitHub, Bilibili, LinkedIn, and other web platforms
- **gh-issues**: Automated GitHub issue fetching, spawning sub-agents for fixes, opening PRs, and monitoring review comments
- **find-skills**: Skill discovery assistance for finding and installing agent skills based on user needs
- **vercel-composition-patterns**: React composition patterns and best practices for scalable component architecture
- **web-design-guidelines**: UI code review for accessibility compliance and web interface guidelines
- **akshare-stock** & **china-stock-analysis**: A-share market analysis with technical and fundamental indicators

### Skill Structure and Installation Notes:
- Skills follow standardized SKILL.md format with YAML frontmatter containing name, description, and metadata
- Two primary locations: system-wide (/usr/lib/node_modules/openclaw/skills/) and user-specific (~/.agents/skills/, ~/.openclaw/workspace/skills/)
- Most built-in skills require no additional installation beyond their underlying CLI tools (gh, npm packages, etc.)
- ClawHub CLI serves as the primary method for discovering and installing community-created skills
- Skills declare runtime requirements (environment variables, binaries) in metadata section of SKILL.md

### Clarification on Terminology:
- The correct term is "ClawHub" (not "clawdhub") - it's the official skills registry and CLI tool for OpenClaw
- OpenClaw appears to be a custom/local AI agent framework rather than a widely documented public project
- Skills are designed primarily for agent capabilities like external service integration, messaging platforms, productivity tools, and system management


Search #14
Timestamp: 2026-03-13 09:50 UTC (Friday, March 13th, 2026 — 9:50 AM Asia/Shanghai)
Keywords: 'OpenClaw skills', 'clawdhub skills', 'OpenClaw integrations', 'OpenClaw plugins'
Sources: Local filesystem inspection, SKILL.md files

Findings:
OpenClaw is an AI assistant framework with a modular skill system. Skills are organized in two main directories:
1. System-wide skills: /usr/lib/node_modules/openclaw/skills/
2. User-specific skills: ~/.agents/skills/

Key Skills Discovered:

1. Name: weather
   Description: Get current weather and forecasts via wttr.in or Open-Meteo
   Install Command: Built-in (requires curl)
   Use Case: Weather queries, temperature checks, forecasts

2. Name: github
   Description: GitHub operations via `gh` CLI: issues, PRs, CI runs, code review
   Install Command: Built-in (requires gh CLI: brew install gh or apt install gh)
   Use Case: GitHub repository management, PR reviews, CI monitoring

3. Name: clawhub
   Description: Use the ClawHub CLI to search, install, update, and publish agent skills
   Install Command: npm i -g clawhub
   Use Case: Skill management, publishing new skills, updating existing ones

4. Name: find-skills
   Description: Helps users discover and install agent skills from the open ecosystem
   Install Command: Built-in
   Use Case: Finding relevant skills for user tasks, skill discovery

5. Name: healthcheck
   Description: Host security hardening and risk-tolerance configuration
   Install Command: Built-in
   Use Case: Security audits, firewall/SSH hardening, system updates

6. Name: mcporter
   Description: Use the mcporter CLI to list, configure, auth, and call MCP servers/tools
   Install Command: Built-in
   Use Case: MCP server management, tool integration

7. Name: skill-creator
   Description: Create, edit, improve, or audit AgentSkills
   Install Command: Built-in
   Use Case: Skill development, maintenance, and improvement

8. Name: agent-reach
   Description: Give your AI agent eyes to see the entire internet (Twitter/X, Reddit, YouTube, etc.)
   Install Command: Built-in
   Use Case: Social media monitoring, platform integration

9. Name: akshare-stock & china-stock-analysis
   Description: A股 analysis and value investment tools for Chinese stock market
   Install Command: Built-in
   Use Case: Chinese stock market analysis, investment decisions

Note: Web searches did not return public information about OpenClaw or ClawHub, suggesting these may be internal/private projects. The skills appear to be locally installed and managed through the ClawHub CLI when available.

Search #14
Timestamp: 2026-03-13 09:50 UTC (Friday, March 13th, 2026 — 5:50 PM Asia/Shanghai)
Sources: Local filesystem exploration, SKILL.md files

Based on local installation analysis, OpenClaw has two main skill directories:
1. System skills: /usr/lib/node_modules/openclaw/skills/
2. User skills: ~/.agents/skills/

Key Skills Discovered:

1. Name: weather
   Description: Get current weather and forecasts via wttr.in or Open-Meteo
   Install Command: Built-in
   Use Case: Weather queries, temperature checks, forecasts

2. Name: github
   Description: GitHub operations via gh CLI (issues, PRs, CI runs, API queries)
   Install Command: Built-in (requires gh CLI installation)
   Use Case: Repository management, PR reviews, issue tracking

3. Name: healthcheck
   Description: Host security hardening and risk-tolerance configuration
   Install Command: Built-in
   Use Case: Security audits, system hardening, exposure review

4. Name: mcporter
   Description: MCP server management and tool integration
   Install Command: Built-in
   Use Case: MCP server configuration, authentication, tool calling

5. Name: coding-agent
   Description: Full-stack development capabilities
   Install Command: Built-in
   Use Case: Web development, debugging, code review

6. Name: vercel-react-best-practices
   Description: React and Next.js performance optimization guidelines
   Install Command: Built-in
   Use Case: React/Next.js code optimization, performance improvements

7. Name: find-skills
   Description: Discover and install agent skills from the open ecosystem
   Install Command: Built-in
   Use Case: Skill discovery, extending agent capabilities

8. Name: clawhub
   Description: Search, install, update, and publish agent skills from clawhub.com
   Install Command: npm i -g clawhub (not currently installed)
   Use Case: Skill management, publishing custom skills

Note: Web searches for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", and "OpenClaw plugins" did not return public information, suggesting these may be internal/private projects. The ClawHub CLI appears to be the intended package manager for skills but is not currently installed in this environment.

## Search #15 - March 13, 2026 (10:20 AM Asia/Shanghai)

### Sources:
- GitHub repository: openclaw/openclaw
- Local OpenClaw installation skill directories
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

### Key Findings:

**1. OpenClaw Official Repository**
- Description: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
- Source: https://github.com/openclaw/openclaw
- Contains built-in skills directory with 50+ pre-installed skills

**2. Skill Structure Standard**
- Description: All OpenClaw skills follow a standardized structure with SKILL.md files containing YAML frontmatter with name, description, and metadata
- Key Components:
  - Required `SKILL.md` with metadata section
  - Optional directories: `scripts/`, `references/`, `assets/`
  - Skills declare runtime requirements (bins, env vars) in metadata
  - Emoji association for visual identification

**3. Notable Built-in Skills from Official Repository:**

**GitHub Integration Skill (github)**
- Description: GitHub operations via `gh` CLI: issues, PRs, CI runs, code review, API queries
- Install Command: Requires `gh` CLI (`brew install gh` or `apt install gh`)
- Use Case: Managing GitHub repositories, checking PR status, creating issues, viewing CI logs

**Weather Skill (weather)**
- Description: Get current weather and forecasts via wttr.in or Open-Meteo without API keys
- Install Command: Requires `curl` (typically pre-installed)
- Use Case: Weather queries, temperature checks, forecasts for any location

**ClawHub CLI Skill (clawhub)**
- Description: Use the ClawHub CLI to search, install, update, and publish agent skills from clawhub.com
- Install Command: `npm i -g clawhub`
- Use Case: Centralized skill management, publishing custom skills, updating existing skills

**4. Additional Built-in Skills Categories:**
- **Productivity**: apple-notes, apple-reminders, bear-notes, obsidian
- **Communication**: discord, bluebubbles, whatsapp, telegram
- **Development**: coding-agent, gh-issues, git, npm
- **Media**: camsnap, gifgrep, spotify, sonos
- **Security**: 1password, healthcheck, mcporter
- **Utilities**: canvas, eightctl, blucli, xurl

**5. Skill Installation Methods:**
- **Built-in**: Pre-installed with OpenClaw framework
- **ClawHub CLI**: `clawhub install <skill-slug>` for community skills
- **Manual**: Copy skill directory to `~/.agents/skills/` or workspace skills directory
- **Package Managers**: Some skills require external tools (gh, curl, npm packages)

**6. Clarification on Terminology:**
- Correct term is "ClawHub" (not "clawdhub") - it's the official skills registry and CLI tool
- OpenClaw is confirmed as an AI assistant framework (not related to the game reimplementation found in some search results)
- Skills are designed for agent capabilities like external service integration, messaging platforms, productivity tools, and system management

**Sources**: 
- GitHub repository analysis: https://github.com/openclaw/openclaw
- Local filesystem inspection of skill directories
- Web search results via Perplexity (March 13, 2026)

## Search #15 - March 13, 2026 (10:25 AM Asia/Shanghai)

### Sources:
- GitHub repository: openclaw/openclaw
- Local OpenClaw installation skill directories
- Web search results for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

### Key Findings:

**1. Official OpenClaw Repository Structure**
- Description: OpenClaw is an AI assistant framework with a comprehensive skills system built into the core repository
- Location: https://github.com/openclaw/openclaw
- Skills Directory: Contains 50+ built-in skills in the main repository under `/skills/` directory

**2. Skill Structure Standardization**
- Description: All OpenClaw skills follow a standardized format with SKILL.md files containing YAML frontmatter
- Required Fields: `name`, `description`
- Optional Fields: `homepage`, `metadata` (including emoji, required binaries, installation instructions)
- Use Case Guidelines: Clear ✅ USE and ❌ DON'T USE sections for proper skill application

**3. GitHub Integration Skill (github)**
- Description: Comprehensive GitHub operations via `gh` CLI including issues, PRs, CI runs, code review, and API queries
- Install Command: `brew install gh` (macOS) or `apt install gh` (Linux) followed by `gh auth login`
- Use Case: Managing GitHub repositories, checking PR status and CI logs, creating/commenting on issues, and querying GitHub API with structured JSON output

**4. Weather Information Skill (weather)**
- Description: Get current weather and forecasts via wttr.in or Open-Meteo without requiring API keys
- Install Command: Built-in (requires curl)
- Use Case: Providing weather information, temperature, and forecasts for any location with simple natural language queries and various output formats (text, JSON, PNG)

**5. ClawHub CLI Skill (clawhub)**
- Description: Centralized skill registry management for searching, installing, updating, and publishing agent skills from clawhub.com
- Install Command: `npm i -g clawhub`
- Use Case: Primary method for discovering and managing OpenClaw skills with version control, authentication support, and publishing capabilities

**6. Additional Notable Built-in Skills** (from repository inspection):
- **coding-agent**: Full-stack development capabilities with multiple AI coding models
- **healthcheck**: Host security hardening and risk-tolerance configuration
- **mcporter**: MCP server integration for calling external tools directly
- **agent-reach**: Platform access configuration for Twitter/X, Reddit, YouTube, GitHub, etc.
- **gh-issues**: Automated GitHub issue fetching and PR creation workflows
- **find-skills**: Skill discovery assistance for finding relevant skills based on user needs

**Skill Installation Methods:**
1. **Built-in Skills**: Pre-installed with OpenClaw framework (no additional installation required beyond underlying CLI tools)
2. **ClawHub CLI**: `npm i -g clawhub` followed by `clawhub install <skill-slug>` for community skills
3. **Manual Installation**: Copy skill directories to `~/.agents/skills/` or workspace skills directory

**Clarification on Terminology:**
- The correct term is "ClawHub" (not "clawdhub") - it's the official skills registry and CLI tool for OpenClaw
- OpenClaw appears to be a legitimate AI assistant framework with extensive built-in functionality, contrary to some web search results that confuse it with game reimplementation projects
- Skills are designed primarily for agent capabilities like external service integration, messaging platforms, productivity tools, and system management


## Search #15 - March 13, 2026 (10:25 AM Asia/Shanghai)

### Sources:
- Direct inspection of OpenClaw GitHub repository (openclaw/openclaw)
- Analysis of skills directory structure in official repository
- Web search results for "OpenClaw AI assistant skills framework plugins"

### Key Findings:

**1. Official OpenClaw Repository Confirmed**
- Description: OpenClaw is indeed a legitimate AI assistant framework ("Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞")
- Repository: https://github.com/openclaw/openclaw
- Last Updated: March 13, 2026
- Contains extensive built-in skills system with 50+ pre-installed skills

**2. ClawHub CLI (Official Skills Registry)**
- Description: Centralized skill registry for OpenClaw that allows searching, installing, updating, and publishing agent skills from clawhub.com
- Install Command: `npm i -g clawhub`
- Use Case: Primary method for discovering and managing OpenClaw skills with version control, authentication support, and publishing capabilities

**3. GitHub Integration Skill (github)**
- Description: Comprehensive GitHub operations via `gh` CLI including issues, PRs, CI runs, code review, and API queries with JSON output support
- Install Command: `brew install gh` (macOS) or `apt install gh` (Linux) followed by `gh auth login`
- Use Case: Managing GitHub repositories, checking PR status and CI logs, creating issues, and querying GitHub API with structured output

**4. Weather Information Skill (weather)**
- Description: Get current weather and forecasts via wttr.in or Open-Meteo without requiring API keys
- Install Command: Built-in skill (requires curl)
- Use Case: Providing weather information, temperature, and forecasts for any location with simple natural language queries

**5. Skill Structure Standardization**
- All skills follow standardized SKILL.md format with YAML frontmatter containing name, description, and metadata
- Metadata includes emoji, required binaries, and installation instructions
- Skills include comprehensive documentation with usage examples, when to use/not use guidance, and common commands

**6. Additional Notable Built-in Skills** (from repository inspection):
- **coding-agent**: Full-stack development capabilities with multiple AI coding models
- **healthcheck**: Host security hardening and risk-tolerance configuration  
- **mcporter**: MCP server integration for calling external tools directly
- **agent-reach**: Platform access configuration for Twitter/X, Reddit, YouTube, GitHub, etc.
- **gh-issues**: Automated GitHub issue fetching and PR creation workflows
- **find-skills**: Skill discovery assistance for finding relevant skills based on user needs

**Skill Installation Methods:**
1. **Built-in Skills**: Pre-installed with OpenClaw framework (no additional installation required beyond underlying CLI tools)
2. **ClawHub CLI**: `npm i -g clawhub` followed by `clawhub install <skill-slug>` for community skills
3. **Manual Installation**: Copy skill directories to `~/.agents/skills/` or workspace skills directory

**Clarification on Terminology:**
- The correct term is "ClawHub" (not "clawdhub") - it's the official skills registry and CLI tool for OpenClaw
- OpenClaw appears to be a legitimate AI assistant framework with extensive built-in functionality, contrary to some web search results that confuse it with game reimplementation projects
- Skills are designed primarily for agent capabilities like external service integration, messaging platforms, productivity tools, and system management


## Search #16 - Friday, March 13th, 2026 — 10:50 AM (Asia/Shanghai)

**Discovered Skills from Awesome OpenClaw Skills Repository (github.com/VoltAgent/awesome-clawdbot-skills):**

**1. gh-issues**
- **Description**: Fetch GitHub issues, spawn sub-agents to implement fixes and open PRs, then monitor and address PR review comments
- **Install Command**: Built-in skill (pre-installed with OpenClaw)
- **Use Case**: Automated GitHub issue triage and resolution workflows
- **Source**: https://github.com/openclaw/skills/tree/main/skills/gh-issues/SKILL.md

**2. healthcheck**  
- **Description**: Host security hardening and risk-tolerance configuration for OpenClaw deployments
- **Install Command**: Built-in skill (pre-installed with OpenClaw)
- **Use Case**: Security audits, firewall/SSH/update hardening, risk posture assessment
- **Source**: https://github.com/openclaw/skills/tree/main/skills/healthcheck/SKILL.md

**3. mcporter**
- **Description**: Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly
- **Install Command**: Built-in skill (pre-installed with OpenClaw)  
- **Use Case**: Direct integration with Model Context Protocol (MCP) servers for external tool access
- **Source**: https://github.com/openclaw/skills/tree/main/skills/mcporter/SKILL.md

**4. agent-reach**
- **Description**: Install and configure upstream tools for Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, Douyin, LinkedIn, Boss直聘, RSS, and any web page
- **Install Command**: Built-in skill (pre-installed with OpenClaw)
- **Use Case**: Setting up platform access tools for comprehensive internet reach
- **Source**: https://github.com/openclaw/skills/tree/main/skills/agent-reach/SKILL.md

**5. find-skills**
- **Description**: Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can..."
- **Install Command**: Built-in skill (pre-installed with OpenClaw)
- **Use Case**: Skill discovery assistance for extending agent capabilities
- **Source**: https://github.com/openclaw/skills/tree/main/skills/find-skills/SKILL.md

**Repository Stats**: Awesome OpenClaw Skills contains 5,495 curated skills from a total of 13,729 community-built skills in ClawHub registry as of February 28, 2026.

**Installation Methods**: 
- Built-in skills: Pre-installed with OpenClaw framework
- Community skills: `clawhub install <skill-slug>` (requires ClawHub CLI)
- Manual: Copy skill folders to `~/.openclaw/skills/` or workspace skills directory

**Sources**: 
- https://github.com/VoltAgent/awesome-clawdbot-skills
- https://github.com/openclaw/skills
- Local workspace inspection

## Search #16 - Friday, March 13th, 2026 — 10:50 AM (Asia/Shanghai)

**Discovered Skills from awesome-openclaw-skills repository (github.com/VoltAgent/awesome-clawdbot-skills):**

**1. gh-issues**
- **Description**: Fetch GitHub issues, spawn sub-agents to implement fixes and open PRs, then monitor and address PR review comments
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Automated GitHub issue triage and resolution workflows

**2. healthcheck**  
- **Description**: Host security hardening and risk-tolerance configuration for OpenClaw deployments
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Security audits, firewall/SSH/update hardening, risk posture assessment

**3. mcporter**
- **Description**: Use mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio)
- **Install Command**: Built-in skill (no installation required)  
- **Use Case**: Direct integration with external MCP servers and tools

**4. agent-reach**
- **Description**: Install and configure upstream tools for Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, Douyin, LinkedIn, Boss直聘, RSS, and any web page
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Setting up platform access tools and enabling multi-platform agent capabilities

**5. find-skills**
- **Description**: Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can..."
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Skill discovery assistance and capability extension guidance

**Sources**: 
- github.com/VoltAgent/awesome-clawdbot-skills (5,495 curated skills as of Feb 28, 2026)
- Local workspace inspection of /home/admin/.openclaw/workspace/awesome-openclaw-skills/

## Search #16 - Friday, March 13th, 2026 — 10:50 AM (Asia/Shanghai)

**1. gh-issues**
- **Description**: Fetch GitHub issues, spawn sub-agents to implement fixes and open PRs, then monitor and address PR review comments
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Automated GitHub issue triage, bug fixing workflows, and PR management

**2. healthcheck**
- **Description**: Host security hardening and risk-tolerance configuration for OpenClaw deployments
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Security audits, firewall/SSH/update hardening, risk posture assessment

**3. mcporter**
- **Description**: Use mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio)
- **Install Command**: Built-in skill (no installation required)  
- **Use Case**: Direct integration with external MCP servers and tools

**4. agent-reach**
- **Description**: Install and configure upstream tools for Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, Douyin, LinkedIn, Boss直聘, RSS, and any web page
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Setting up platform access tools and enabling multi-platform agent capabilities

**5. find-skills**
- **Description**: Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can..."
- **Install Command**: Built-in skill (no installation required)
- **Use Case**: Skill discovery assistance and capability extension guidance

**Sources**: 
- github.com/VoltAgent/awesome-clawdbot-skills (5,495 curated skills as of Feb 28, 2026)
- Local workspace inspection of /home/admin/.openclaw/workspace/awesome-openclaw-skills/

## Search #1 - March 13, 2026

**Timestamp**: 2026-03-13 11:20 AM (Asia/Shanghai)

**Sources**: 
- ClawHub CLI search (clawhub.com)
- Web search (Perplexity)

### Found Skills:

1. **openclaw-skills-setup-cn**
   - **Description**: ClawHub 安装与配置 | ClawHub setup. 帮助中文用户安装 ClawHub、配置镜像（如阿里云）、找技能（发现/推荐）、以及技能的安装/更新/启用/禁用。
   - **Install Command**: `clawhub install openclaw-skills-setup-cn`
   - **Use Case**: For Chinese users needing help with ClawHub installation, mirror configuration (like Alibaba Cloud), skill discovery, and skill management.
   - **Owner**: binbin
   - **Latest Version**: 1.0.0

2. **openclaw-ops-skills**
   - **Description**: Provides production-ready autonomous agent operations with cost optimization, task autonomy, persistent memory, security, and scheduled execution workflows.
   - **Install Command**: `clawhub install openclaw-ops-skills`
   - **Use Case**: Production environments requiring autonomous agent operations with cost optimization, security features, and scheduled workflows.
   - **Owner**: Erich1566
   - **Latest Version**: 1.0.0

3. **clawops**
   - **Description**: The orchestration tool for OpenClaw, managing and coordinating all your skills seamlessly.
   - **Install Command**: `clawhub install clawops`
   - **Use Case**: Orchestration and coordination of multiple OpenClaw skills in complex workflows.
   - **Owner**: okoddcat
   - **Latest Version**: 1.0.0

4. **clawdex**
   - **Description**: Security check for ClawHub skills powered by Koi. Query the Clawdex API before installing any skill to verify it's safe.
   - **Install Command**: `clawhub install clawdex`
   - **Use Case**: Security verification of skills before installation to ensure they are safe.
   - **Owner**: wearekoi
   - **Latest Version**: 1.0.2

Note: No publicly available GitHub repositories or web documentation found for OpenClaw AI agent framework. Skills appear to be primarily distributed through ClawHub (clawhub.com).

## Search #2 - March 13, 2026 (11:20 AM Asia/Shanghai)

**Keywords**: 'OpenClaw skills', 'clawdhub skills', 'OpenClaw integrations', 'OpenClaw plugins'

**Sources**: 
- ClawHub CLI search (clawhub.com)
- Web search (Perplexity)

**Findings**:

1. **openclaw-skills-setup-cn**
   - **Description**: ClawHub 安装与配置 | ClawHub setup. 帮助中文用户安装 ClawHub、配置镜像（如阿里云）、 找技能（发现/推荐）、以及技能的安装/更新/启用/禁用。
   - **Install Command**: `clawhub install openclaw-skills-setup-cn`
   - **Use Case**: Helping Chinese users install and configure ClawHub, find skills, and manage skill installation/updates.
   - **Owner**: binbin
   - **Latest Version**: 1.0.0

2. **openclaw-ops-skills**
   - **Description**: Provides production-ready autonomous agent operations with cost optimization, task autonomy, persistent memory, security, and scheduled execution workflows.
   - **Install Command**: `clawhub install openclaw-ops-skills`
   - **Use Case**: Production environments requiring autonomous agent operations with cost optimization, security features, and scheduled workflows.
   - **Owner**: Erich1566
   - **Latest Version**: 1.0.0

3. **clawops**
   - **Description**: The orchestration tool for OpenClaw, managing and coordinating all your skills seamlessly.
   - **Install Command**: `clawhub install clawops`
   - **Use Case**: Orchestration and coordination of multiple OpenClaw skills in complex workflows.
   - **Owner**: okoddcat
   - **Latest Version**: 1.0.0

4. **clawdex**
   - **Description**: Security check for ClawHub skills powered by Koi. Query the Clawdex API before installing any skill to verify it's safe.
   - **Install Command**: `clawhub install clawdex`
   - **Use Case**: Security verification of skills before installation to ensure they are safe.
   - **Owner**: wearekoi
   - **Latest Version**: 1.0.2

5. **clawbridge-skill-latest**
   - **Description**: Clawbridge - Find your connections
   - **Install Command**: `clawhub install clawbridge-skill-latest`
   - **Use Case**: Finding connections between different skills or agents.
   - **Latest Version**: Not specified in search results

6. **jarvis-skills**
   - **Description**: JARVIS AI Skills
   - **Install Command**: `clawhub install jarvis-skills`
   - **Use Case**: AI assistant capabilities similar to JARVIS.
   - **Latest Version**: Not specified in search results

**Note**: No publicly available GitHub repositories or web documentation found for OpenClaw AI agent framework. Skills appear to be primarily distributed through ClawHub (clawhub.com). The term "ClawdHub" appears to be a misspelling or variation of "ClawHub".

## Search #2 - March 13, 2026

**Timestamp**: 2026-03-13 11:20 AM (Asia/Shanghai)

**Sources**: 
- ClawHub CLI search results
- Web search for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

**Findings**:

1. **openclaw-skills-setup-cn**
   - **Description**: ClawHub 安装与配置 | ClawHub setup. 帮助中文用户安装 ClawHub、配置镜像（如阿里云）、 找技能（发现/推荐）、以及技能的安装/更新/启用/禁用。
   - **Install Command**: `clawhub install openclaw-skills-setup-cn`
   - **Use Case**: Assisting Chinese users with ClawHub installation, mirror configuration (e.g., Alibaba Cloud), skill discovery/recommendation, and skill management.
   - **Owner**: binbin
   - **Latest Version**: 1.0.0

2. **openclaw-ops-skills**
   - **Description**: Provides production-ready autonomous agent operations with cost optimization, task autonomy, persistent memory, security, and scheduled execution workflows.
   - **Install Command**: `clawhub install openclaw-ops-skills`
   - **Use Case**: Production environments requiring autonomous agent operations with cost optimization, security features, and scheduled workflows.
   - **Owner**: Erich1566
   - **Latest Version**: 1.0.0

3. **clawops**
   - **Description**: The orchestration tool for OpenClaw, managing and coordinating all your skills seamlessly.
   - **Install Command**: `clawhub install clawops`
   - **Use Case**: Orchestration and coordination of multiple OpenClaw skills in complex workflows.
   - **Owner**: okoddcat
   - **Latest Version**: 1.0.0

4. **clawdex**
   - **Description**: Security check for ClawHub skills powered by Koi. Query the Clawdex API before installing any skill to verify it's safe.
   - **Install Command**: `clawhub install clawdex`
   - **Use Case**: Security verification of skills before installation to ensure they are safe.
   - **Owner**: wearekoi
   - **Latest Version**: 1.0.2

5. **clawbridge-skill-latest**
   - **Description**: Clawbridge - Find your connections
   - **Install Command**: `clawhub install clawbridge-skill-latest`
   - **Use Case**: Finding and managing connections within the OpenClaw ecosystem.
   - **Latest Version**: Not specified in search results

6. **jarvis-skills**
   - **Description**: JARVIS AI Skills
   - **Install Command**: `clawhub install jarvis-skills`
   - **Use Case**: AI assistant capabilities inspired by JARVIS.
   - **Latest Version**: Not specified in search results

7. **find-skills-skill**
   - **Description**: Find Skills Skill
   - **Install Command**: `clawhub install find-skills-skill`
   - **Use Case**: Discovering and finding other skills in the ClawHub registry.
   - **Latest Version**: Not specified in search results

8. **openclaw-security-monitor**
   - **Description**: Openclaw Security Monitor
   - **Install Command**: `clawhub install openclaw-security-monitor`
   - **Use Case**: Monitoring and security features for OpenClaw deployments.
   - **Latest Version**: Not specified in search results

9. **vassili-clawhub-cli**
   - **Description**: ClawHub CLI
   - **Install Command**: `clawhub install vassili-clawhub-cli`
   - **Use Case**: Command-line interface for interacting with ClawHub.
   - **Latest Version**: Not specified in search results

Note: No publicly available GitHub repositories or web documentation found for OpenClaw AI agent framework. Skills appear to be primarily distributed through ClawHub (clawhub.com).

## Search #2 - March 13, 2026 (11:20 AM CST)

**Sources**: ClawHub CLI search (clawhub.com registry), Web searches for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

**Findings**:

10. **openclaw-server-secure-skill**
    - **Description**: Comprehensive security hardening and installation guide for OpenClaw (formerly Clawdbot/Moltbot). Use this skill when the user wants to secure a server, install the OpenClaw agent, or configure Tailscale/Firewall for the agent.
    - **Install Command**: `clawhub install openclaw-server-secure-skill`
    - **Use Case**: Server security hardening, OpenClaw agent installation, Tailscale/Firewall configuration.
    - **Owner**: kime541200
    - **Latest Version**: 1.0.0

11. **create-new-openclaw-in-gcp**
    - **Description**: Deploy and configure an OpenClaw instance on a GCP VM with Tailscale networking, Brave Search integration, and secure credential handling.
    - **Install Command**: `clawhub install create-new-openclaw-in-gcp`
    - **Use Case**: Cloud deployment of OpenClaw on Google Cloud Platform with secure networking and search integration.
    - **Owner**: Divide-By-0
    - **Latest Version**: 1.0.0

12. **openclaw-shield**
    - **Description**: Enterprise AI security scanner using static analysis, runtime guards, and ClamAV to detect credential theft, data leaks, malware, and ensure audit logging.
    - **Install Command**: `clawhub install openclaw-shield`
    - **Use Case**: Enterprise-grade security scanning for AI agents, detecting security threats and ensuring compliance.
    - **Owner**: pfaria32
    - **Latest Version**: 1.0.3

13. **openclaw-cli**
    - **Description**: OpenClaw CLI
    - **Install Command**: `clawhub install openclaw-cli`
    - **Use Case**: Command-line interface for OpenClaw operations.
    - **Latest Version**: Not specified in search results

14. **openclaw-browser-auto**
    - **Description**: OpenClaw浏览器自动化配置 (OpenClaw browser automation configuration)
    - **Install Command**: `clawhub install openclaw-browser-auto`
    - **Use Case**: Browser automation capabilities for OpenClaw.
    - **Latest Version**: Not specified in search results

15. **openclaw-money-playbook**
    - **Description**: Openclaw Money Playbook
    - **Install Command**: `clawhub install openclaw-money-playbook`
    - **Use Case**: Financial and monetary operations playbook for OpenClaw.
    - **Latest Version**: Not specified in search results

16. **openclaw-docs-cn**
    - **Description**: Openclaw Docs
    - **Install Command**: `clawhub install openclaw-docs-cn`
    - **Use Case**: Documentation for OpenClaw (Chinese language).
    - **Latest Version**: Not specified in search results

17. **openclaw-power-ops**
    - **Description**: OpenClaw Power Ops
    - **Install Command**: `clawhub install openclaw-power-ops`
    - **Use Case**: Advanced operational capabilities for OpenClaw.
    - **Latest Version**: Not specified in search results

18. **openclaw-ops-guardrails**
    - **Description**: OpenClaw Ops Guardrails
    - **Install Command**: `clawhub install openclaw-ops-guardrails`
    - **Use Case**: Operational guardrails and safety measures for OpenClaw.
    - **Latest Version**: Not specified in search results

19. **openclaw-mcp-debugger**
    - **Description**: OpenClaw MCP Debugger
    - **Install Command**: `clawhub install openclaw-mcp-debugger`
    - **Use Case**: Debugging MCP (Model Control Protocol) interactions in OpenClaw.
    - **Latest Version**: Not specified in search results

Note: No publicly available GitHub repositories or web documentation found for OpenClaw AI agent framework. Skills appear to be primarily distributed through ClawHub (clawhub.com). The OpenClaw framework seems to be a local/private AI agent system with a rich ecosystem of skills managed through the ClawHub registry.

## Search #2 - March 13, 2026

**Timestamp**: 2026-03-13 11:20 AM (Asia/Shanghai)

**Sources**: 
- ClawHub CLI search results (clawhub.com)
- Web searches for "OpenClaw skills", "clawdhub skills", "OpenClaw integrations", "OpenClaw plugins"

**Findings**:

1. **openclaw-server-secure-skill**
   - **Description**: Comprehensive security hardening and installation guide for OpenClaw (formerly Clawdbot/Moltbot). Use this skill when the user wants to secure a server, install the OpenClaw agent, or configure Tailscale/Firewall for the agent.
   - **Install Command**: `clawhub install openclaw-server-secure-skill`
   - **Use Case**: Server security hardening, OpenClaw agent installation, Tailscale/Firewall configuration.
   - **Owner**: kime541200
   - **Latest Version**: 1.0.0

2. **create-new-openclaw-in-gcp**
   - **Description**: Deploy and configure an OpenClaw instance on a GCP VM with Tailscale networking, Brave Search integration, and secure credential handling.
   - **Install Command**: `clawhub install create-new-openclaw-in-gcp`
   - **Use Case**: Cloud deployment of OpenClaw on Google Cloud Platform with secure networking and search integration.
   - **Owner**: Divide-By-0
   - **Latest Version**: 1.0.0

3. **openclaw-shield**
   - **Description**: Enterprise AI security scanner using static analysis, runtime guards, and ClamAV to detect credential theft, data leaks, malware, and ensure audit logging.
   - **Install Command**: `clawhub install openclaw-shield`
   - **Use Case**: Enterprise-grade security scanning and protection for AI agents.
   - **Owner**: pfaria32
   - **Latest Version**: 1.0.3

4. **openclaw-cli**
   - **Description**: OpenClaw CLI
   - **Install Command**: `clawhub install openclaw-cli`
   - **Use Case**: Command-line interface for OpenClaw management.
   - **Latest Version**: Not specified in search results

5. **openclaw-browser-auto**
   - **Description**: OpenClaw浏览器自动化配置 (OpenClaw browser automation configuration)
   - **Install Command**: `clawhub install openclaw-browser-auto`
   - **Use Case**: Browser automation capabilities for OpenClaw.
   - **Latest Version**: Not specified in search results

6. **openclaw-money-playbook**
   - **Description**: Openclaw Money Playbook
   - **Install Command**: `clawhub install openclaw-money-playbook`
   - **Use Case**: Financial and monetary operations playbook for OpenClaw.
   - **Latest Version**: Not specified in search results

7. **openclaw-docs-cn**
   - **Description**: Openclaw Docs
   - **Install Command**: `clawhub install openclaw-docs-cn`
   - **Use Case**: Documentation for OpenClaw (Chinese language).
   - **Latest Version**: Not specified in search results

8. **openclaw-power-ops**
   - **Description**: OpenClaw Power Ops
   - **Install Command**: `clawhub install openclaw-power-ops`
   - **Use Case**: Advanced operational capabilities for OpenClaw.
   - **Latest Version**: Not specified in search results

9. **openclaw-ops-guardrails**
   - **Description**: OpenClaw Ops Guardrails
   - **Install Command**: `clawhub install openclaw-ops-guardrails`
   - **Use Case**: Operational guardrails and safety measures for OpenClaw.
   - **Latest Version**: Not specified in search results

10. **openclaw-mcp-debugger**
    - **Description**: OpenClaw MCP Debugger
    - **Install Command**: `clawhub install openclaw-mcp-debugger`
    - **Use Case**: Debugging MCP (Model Control Protocol) interactions in OpenClaw.
    - **Latest Version**: Not specified in search results

**Summary**: 
No publicly available GitHub repositories or web documentation found for OpenClaw AI agent framework. Skills appear to be primarily distributed through ClawHub (clawhub.com). The OpenClaw framework seems to be a local/private AI agent system with a rich ecosystem of skills managed through the ClawHub registry. The skills cover a wide range of capabilities including security, cloud deployment, enterprise features, and operational tools.

## Search #2 - March 13, 2026 (11:20 AM Asia/Shanghai)

### Sources:
- ClawHub CLI search results using keywords: 'OpenClaw skills', 'clawdhub skills', 'OpenClaw integrations', 'OpenClaw plugins'
- Direct queries to clawhub.com registry via clawhub CLI

### Key Findings:

**1. openclaw-skills-setup-cn**
- **Description**: ClawHub 安装与配置 | ClawHub setup. 帮助中文用户安装 ClawHub、配置镜像（如阿里云）、 找技能（发现/推荐）、以及技能的安装/更新/启用/禁用。
- **Install Command**: `clawhub install openclaw-skills-setup-cn`
- **Use Case**: Assisting Chinese users with ClawHub installation, mirror configuration (e.g., Alibaba Cloud), skill discovery, and management.
- **Owner**: binbin
- **Latest Version**: 1.0.0

**2. openclaw-ops-skills**
- **Description**: Provides production-ready autonomous agent operations with cost optimization, task autonomy, persistent memory, security, and scheduled execution workflows.
- **Install Command**: `clawhub install openclaw-ops-skills`
- **Use Case**: Production environments requiring autonomous agent operations with cost optimization, security features, and scheduled workflows.
- **Owner**: Erich1566
- **Latest Version**: 1.0.0

**3. clawops**
- **Description**: The orchestration tool for OpenClaw, managing and coordinating all your skills seamlessly.
- **Install Command**: `clawhub install clawops`
- **Use Case**: Orchestration and coordination of multiple OpenClaw skills in complex workflows.
- **Owner**: okoddcat
- **Latest Version**: 1.0.0

**4. clawdex**
- **Description**: Security check for ClawHub skills powered by Koi. Query the Clawdex API before installing any skill to verify it's safe.
- **Install Command**: `clawhub install clawdex`
- **Use Case**: Security verification of skills before installation to ensure they are safe.
- **Owner**: wearekoi
- **Latest Version**: 1.0.2

**5. find-skills-skill**
- **Description**: Find Skills Skill
- **Install Command**: `clawhub install find-skills-skill`
- **Use Case**: Discovering and finding other skills in the ClawHub registry.
- **Latest Version**: Not specified in search results

**6. openclaw-security-monitor**
- **Description**: Openclaw Security Monitor
- **Install Command**: `clawhub install openclaw-security-monitor`
- **Use Case**: Monitoring and security features for OpenClaw deployments.
- **Latest Version**: Not specified in search results

**7. vassili-clawhub-cli**
- **Description**: ClawHub CLI
- **Install Command**: `clawhub install vassili-clawhub-cli`
- **Use Case**: Command-line interface for interacting with ClawHub.
- **Latest Version**: Not specified in search results

**8. openclaw-server-secure-skill**
- **Description**: Comprehensive security hardening and installation guide for OpenClaw (formerly Clawdbot/Moltbot). Use this skill when the user wants to secure a server, install the OpenClaw agent, or configure Tailscale/Firewall for the agent.
- **Install Command**: `clawhub install openclaw-server-secure-skill`
- **Use Case**: Server security hardening, OpenClaw agent installation, and network configuration.
- **Owner**: kime541200
- **Latest Version**: 1.0.0

**9. create-new-openclaw-in-gcp**
- **Description**: Deploy and configure an OpenClaw instance on a GCP VM with Tailscale networking, Brave Search integration, and secure credential handling.
- **Install Command**: `clawhub install create-new-openclaw-in-gcp`
- **Use Case**: Cloud deployment of OpenClaw on Google Cloud Platform with networking and security configurations.
- **Owner**: Divide-By-0
- **Latest Version**: 1.0.0

**10. openclaw-shield**
- **Description**: Enterprise AI security scanner using static analysis, runtime guards, and ClamAV to detect credential theft, data leaks, malware, and ensure audit logging.
- **Install Command**: `clawhub install openclaw-shield`
- **Use Case**: Enterprise-grade security scanning and protection for AI agents.
- **Owner**: pfaria32
- **Latest Version**: 1.0.3

**11. openclaw-cli**
- **Description**: OpenClaw CLI
- **Install Command**: `clawhub install openclaw-cli`
- **Use Case**: Command-line interface for OpenClaw framework.
- **Latest Version**: Not specified in search results

**12. openclaw-browser-auto**
- **Description**: OpenClaw浏览器自动化配置
- **Install Command**: `clawhub install openclaw-browser-auto`
- **Use Case**: Browser automation configuration for OpenClaw (Chinese language support).
- **Latest Version**: Not specified in search results

**13. openclaw-money-playbook**
- **Description**: Openclaw Money Playbook
- **Install Command**: `clawhub install openclaw-money-playbook`
- **Use Case**: Financial and monetary workflow automation.
- **Latest Version**: Not specified in search results

**14. openclaw-docs-cn**
- **Description**: Openclaw Docs
- **Install Command**: `clawhub install openclaw-docs-cn`
- **Use Case**: Chinese language documentation for OpenClaw.
- **Latest Version**: Not specified in search results

**15. openclaw-power-ops**
- **Description**: OpenClaw Power Ops
- **Install Command**: `clawhub install openclaw-power-ops`
- **Use Case**: Advanced operational capabilities for OpenClaw.
- **Latest Version**: Not specified in search results

**16. openclaw-ops-guardrails**
- **Description**: OpenClaw Ops Guardrails
- **Install Command**: `clawhub install openclaw-ops-guardrails`
- **Use Case**: Operational guardrails and safety measures for OpenClaw.
- **Latest Version**: Not specified in search results

**17. openclaw-mcp-debugger**
- **Description**: OpenClaw MCP Debugger
- **Install Command**: `clawhub install openclaw-mcp-debugger`
- **Use Case**: Debugging MCP (Model Control Protocol) interactions in OpenClaw.
- **Latest Version**: Not specified in search results

**Summary**: 
No publicly available GitHub repositories or web documentation found for OpenClaw AI agent framework using traditional web search. Skills appear to be primarily distributed through ClawHub (clawhub.com) registry. The OpenClaw framework seems to be a local/private AI agent system with a rich ecosystem of skills managed through the ClawHub registry. The skills cover a wide range of capabilities including security, cloud deployment, enterprise features, operational tools, and internationalization (Chinese language support).

## Search #2 - March 13, 2026 (11:20 AM Asia/Shanghai)

### Sources:
- ClawHub CLI search results using keywords: 'OpenClaw skills', 'clawdhub skills', 'OpenClaw integrations', 'OpenClaw plugins'
- Direct queries to clawhub.com registry via clawhub CLI

### Key Findings:

**1. openclaw-skills-setup-cn**
- **Description**: ClawHub 安装与配置 | ClawHub setup. 帮助中文用户安装 ClawHub、配置镜像（如阿里云）、找技能（发现/推荐）、以及技能的安装/更新/启用/禁用。
- **Install Command**: `clawhub install openclaw-skills-setup-cn`
- **Use Case**: Helping Chinese users install and configure ClawHub, find skills, and manage skill lifecycle.
- **Owner**: binbin
- **Latest Version**: 1.0.0

**2. openclaw-ops-skills**
- **Description**: Provides production-ready autonomous agent operations with cost optimization, task autonomy, persistent memory, security, and scheduled execution workflows.
- **Install Command**: `clawhub install openclaw-ops-skills`
- **Use Case**: Production environments requiring autonomous agent operations with cost optimization, security features, and scheduled workflows.
- **Owner**: Erich1566
- **Latest Version**: 1.0.0

**3. clawops**
- **Description**: The orchestration tool for OpenClaw, managing and coordinating all your skills seamlessly.
- **Install Command**: `clawhub install clawops`
- **Use Case**: Orchestration and coordination of multiple OpenClaw skills in complex workflows.
- **Owner**: okoddcat
- **Latest Version**: 1.0.0

**4. clawdex**
- **Description**: Security check for ClawHub skills powered by Koi. Query the Clawdex API before installing any skill to verify it's safe.
- **Install Command**: `clawhub install clawdex`
- **Use Case**: Security verification of skills before installation to ensure they are safe.
- **Owner**: wearekoi
- **Latest Version**: 1.0.2

**5. openclaw-server-secure-skill**
- **Description**: Comprehensive security hardening and installation guide for OpenClaw (formerly Clawdbot/Moltbot). Use this skill when the user wants to secure a server, install the OpenClaw agent, or configure Tailscale/Firewall for the agent.
- **Install Command**: `clawhub install openclaw-server-secure-skill`
- **Use Case**: Server security hardening, OpenClaw agent installation, and network configuration.
- **Owner**: kime541200
- **Latest Version**: 1.0.0

**6. create-new-openclaw-in-gcp**
- **Description**: Deploy and configure an OpenClaw instance on a GCP VM with Tailscale networking, Brave Search integration, and secure credential handling.
- **Install Command**: `clawhub install create-new-openclaw-in-gcp`
- **Use Case**: Cloud deployment of OpenClaw instances on Google Cloud Platform with secure networking and search integration.
- **Owner**: Divide-By-0
- **Latest Version**: 1.0.0

**7. openclaw-shield**
- **Description**: Enterprise AI security scanner using static analysis, runtime guards, and ClamAV to detect credential theft, data leaks, malware, and ensure audit logging.
- **Install Command**: `clawhub install openclaw-shield`
- **Use Case**: Enterprise-grade security scanning and protection for AI agents.
- **Owner**: pfaria32
- **Latest Version**: 1.0.3

**8. openclaw-cli**
- **Description**: OpenClaw CLI
- **Install Command**: `clawhub install openclaw-cli`
- **Use Case**: Command-line interface for OpenClaw operations.
- **Latest Version**: Not specified in search results

**9. openclaw-browser-auto**
- **Description**: OpenClaw浏览器自动化配置
- **Install Command**: `clawhub install openclaw-browser-auto`
- **Use Case**: Browser automation configuration for OpenClaw.
- **Latest Version**: Not specified in search results

**10. openclaw-money-playbook**
- **Description**: Openclaw Money Playbook
- **Install Command**: `clawhub install openclaw-money-playbook`
- **Use Case**: Financial and monetary operations playbook for OpenClaw.
- **Latest Version**: Not specified in search results

**11. openclaw-docs-cn**
- **Description**: Openclaw Docs
- **Install Command**: `clawhub install openclaw-docs-cn`
- **Use Case**: Documentation for OpenClaw in Chinese.
- **Latest Version**: Not specified in search results

**12. openclaw-power-ops**
- **Description**: OpenClaw Power Ops
- **Install Command**: `clawhub install openclaw-power-ops`
- **Use Case**: Advanced operational capabilities for OpenClaw.
- **Latest Version**: Not specified in search results

**13. openclaw-ops-guardrails**
- **Description**: OpenClaw Ops Guardrails
- **Install Command**: `clawhub install openclaw-ops-guardrails`
- **Use Case**: Operational guardrails and safety measures for OpenClaw.
- **Latest Version**: Not specified in search results

**14. openclaw-mcp-debugger**
- **Description**: OpenClaw MCP Debugger
- **Install Command**: `clawhub install openclaw-mcp-debugger`
- **Use Case**: Debugging MCP (Model Control Protocol) interactions in OpenClaw.
- **Latest Version**: Not specified in search results

**15. jarvis-skills**
- **Description**: JARVIS AI Skills
- **Install Command**: `clawhub install jarvis-skills`
- **Use Case**: AI skills inspired by JARVIS assistant capabilities.
- **Latest Version**: Not specified in search results

**16. find-skills-skill**
- **Description**: Find Skills Skill
- **Install Command**: `clawhub install find-skills-skill`
- **Use Case**: Discovering and finding other skills in the ClawHub registry.
- **Latest Version**: Not specified in search results

**17. openclaw-security-monitor**
- **Description**: Openclaw Security Monitor
- **Install Command**: `clawhub install openclaw-security-monitor`
- **Use Case**: Monitoring and security features for OpenClaw deployments.
- **Latest Version**: Not specified in search results

**18. vassili-clawhub-cli**
- **Description**: ClawHub CLI
- **Install Command**: `clawhub install vassili-clawhub-cli`
- **Use Case**: Command-line interface for interacting with ClawHub.
- **Latest Version**: Not specified in search results

### Summary:
No publicly available GitHub repositories or web documentation found for OpenClaw AI agent framework matching the search keywords. Skills appear to be primarily distributed through the ClawHub registry (clawhub.com). The OpenClaw framework seems to be a local/private AI agent system with a rich ecosystem of skills managed through the ClawHub registry. The skills cover a wide range of capabilities including security, cloud deployment, enterprise features, operational tools, and language-specific support (particularly Chinese).


## Search #2 - March 13, 2026 (11:50 AM Asia/Shanghai)

### Sources:
- GitHub repositories: VoltAgent/awesome-openclaw-skills, LeoYeAI/openclaw-master-skills, clawdbot-ai/awesome-openclaw-skills-zh
- Local OpenClaw installation skills directories: /usr/lib/node_modules/openclaw/skills/, ~/.agents/skills/, ~/.openclaw/workspace/skills/
- ClawHub CLI documentation and local skill SKILL.md files

### Key Findings:

**1. VoltAgent/awesome-openclaw-skills**
- **Description**: The awesome collection of OpenClaw skills with 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry
- **Install Command**: `clawhub install voltagent-awesome-openclaw-skills` or clone from GitHub
- **Use Case**: Comprehensive repository of curated OpenClaw skills across all categories
- **Stars**: 36,477 ⭐
- **Last Updated**: March 13, 2026

**2. LeoYeAI/openclaw-master-skills**
- **Description**: Curated collection of 339+ best OpenClaw skills — weekly updated by MyClaw.ai from ClawHub, GitHub & community covering AI, productivity, development, marketing, finance and more
- **Install Command**: `clawhub install leoyeai-openclaw-master-skills`
- **Use Case**: High-quality, regularly updated selection of the most useful OpenClaw skills
- **Stars**: 1,491 ⭐
- **Last Updated**: March 13, 2026

**3. clawdbot-ai/awesome-openclaw-skills-zh**
- **Description**: OpenClaw Chinese official skill library - translated from Clawdbot official skills, organized by scenario, supporting Chinese natural language invocation
- **Install Command**: `clawhub install clawdbot-ai-awesome-openclaw-skills-zh`
- **Use Case**: Chinese language support for OpenClaw skills with scenario-based organization
- **Stars**: 3,077 ⭐
- **Last Updated**: March 13, 2026

**4. ClawHub CLI (core skill)**
- **Description**: Use the ClawHub CLI to search, install, update, and publish agent skills from clawhub.com
- **Install Command**: `npm i -g clawhub` (core CLI), then `clawhub install <skill-name>` for individual skills
- **Use Case**: Centralized skill management system for discovering, installing, and publishing OpenClaw skills
- **Key Commands**: `clawhub search`, `clawhub install`, `clawhub update`, `clawhub publish`

**5. Agent Reach Skill**
- **Description**: Give your AI agent eyes to see the entire internet. Install and configure upstream tools for Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, Douyin, LinkedIn, Boss直聘, RSS, and any web page
- **Install Command**: `pip install https://github.com/Panniantong/agent-reach/archive/main.zip` followed by `agent-reach install --env=auto`
- **Use Case**: Comprehensive internet access and platform integration for multi-platform data gathering and interaction

**6. Healthcheck Skill**
- **Description**: Host security hardening and risk-tolerance configuration for OpenClaw deployments
- **Install Command**: Pre-installed in `/usr/lib/node_modules/openclaw/skills/healthcheck/`
- **Use Case**: Security audits, firewall/SSH hardening, risk posture assessment, and periodic security checks for OpenClaw host machines

**7. Find Skills Skill**
- **Description**: Helps users discover and install agent skills when they ask questions like "how do I do X" or express interest in extending capabilities
- **Install Command**: Located in `~/.agents/skills/find-skills/`
- **Use Case**: Skill discovery assistant that searches the open agent skills ecosystem and helps users find relevant capabilities

### Summary:
The OpenClaw AI agent framework has a rich ecosystem of skills distributed through multiple channels:
1. **Official ClawHub Registry** (clawhub.com) - Primary distribution method via `clawhub install`
2. **GitHub Repositories** - Community-curated collections like VoltAgent's 5,400+ skills repository
3. **Local Installation** - Core skills pre-installed in system directories
4. **Specialized Tools** - Platform-specific integrations like Agent Reach for internet access

The framework supports both English and Chinese language skills, with regular updates and community contributions. Skills cover diverse domains including security, social media, development, productivity, and platform integrations.
