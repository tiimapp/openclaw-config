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
