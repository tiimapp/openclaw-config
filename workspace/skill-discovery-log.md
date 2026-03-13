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

