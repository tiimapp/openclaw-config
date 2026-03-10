---
name: tavily-search
description: Web search using Tavily AI API - optimized for AI agents with clean, relevant results. Use for research, fact-checking, and finding current information.
metadata:
  {
    "openclaw":
      {
        "emoji": "🔍",
        "requires": { "env": ["TAVILY_API_KEY"] },
        "install":
          [
            {
              "id": "pip",
              "kind": "pip",
              "package": "tavily-python",
              "label": "Install Tavily Python SDK",
            },
          ],
      },
  }
---

# Tavily Search Skill

Web search powered by Tavily AI - designed specifically for AI agents with clean, relevant results and no ads.

## Quick Start

### 1. Get API Key

Sign up at https://tavily.com and get your API key from the dashboard.

### 2. Set Environment Variable

```bash
export TAVILY_API_KEY='your-api-key-here'
```

Or add to `~/.openclaw/.env`:
```
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxx
```

### 3. Install SDK

```bash
pip install tavily-python
```

---

## Usage

### Basic Search

```bash
python3 -c "
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])
response = client.search('your query here')
print(response)
"
```

### Advanced Search Options

```python
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])

response = client.search(
    query="AI agent frameworks 2026",
    search_depth="advanced",  # or "basic"
    max_results=5,
    include_answer=True,
    include_raw_content=False,
    include_images=False,
    topic="general",  # or "news", "finance"
    days=7  # only results from last 7 days
)

print(response['answer'])  # AI-generated answer
print(response['results'])  # Search results
```

---

## Search Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | — | **Required.** Search query |
| `search_depth` | string | "basic" | "basic" or "advanced" |
| `max_results` | int | 5 | Number of results (1-10) |
| `include_answer` | bool | false | Include AI-generated answer |
| `include_raw_content` | bool | false | Include full page content |
| `include_images` | bool | false | Include relevant images |
| `topic` | string | "general" | "general", "news", or "finance" |
| `days` | int | — | Limit to last N days |

---

## Example Commands

### Quick Fact Check
```bash
python3 -c "
from tavily import TavilyClient
import os
client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])
r = client.search('current population of Tokyo 2026', max_results=3)
print(r['answer'])
"
```

### News Search (Last 7 Days)
```bash
python3 -c "
from tavily import TavilyClient
import os
client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])
r = client.search('AI regulation Europe', topic='news', days=7)
for result in r['results']:
    print(f\"- {result['title']}: {result['url']}\")
"
```

### Finance/Stock Search
```bash
python3 -c "
from tavily import TavilyClient
import os
client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])
r = client.search('NVIDIA earnings Q1 2026', topic='finance')
print(r['answer'])
"
```

---

## Response Format

```json
{
  "query": "your search query",
  "answer": "AI-generated direct answer",
  "results": [
    {
      "title": "Page Title",
      "url": "https://example.com/page",
      "content": "Relevant excerpt from page",
      "score": 0.95,
      "published_date": "2026-03-10"
    }
  ],
  "images": [],
  "follow_up_questions": ["Related question 1?"]
}
```

---

## Pricing (as of 2026)

| Plan | Price | Searches/Month |
|------|-------|----------------|
| Free | $0 | 1,000 |
| Starter | $29 | 10,000 |
| Pro | $99 | 50,000 |
| Enterprise | Custom | Unlimited |

Check https://tavily.com/pricing for current rates.

---

## Comparison with Other Search APIs

| Feature | Tavily | Exa MCP | web_search |
|---------|--------|---------|------------|
| AI-generated answer | ✅ | ✅ | ❌ |
| Clean results (no ads) | ✅ | ✅ | Varies |
| Topic filtering | ✅ | Limited | ❌ |
| Time filtering | ✅ | Limited | ❌ |
| Raw content extraction | ✅ | ✅ | ❌ |
| Free tier | 1,000/mo | Limited | Varies |

---

## Troubleshooting

### API Key Error
```
Error: Invalid API key
```
→ Check `TAVILY_API_KEY` is set correctly in environment

### Rate Limit
```
Error: Rate limit exceeded
```
→ Wait or upgrade plan. Free tier: 1,000 searches/month

### No Results
→ Try broader query or check `search_depth="advanced"`

---

## Integration Notes

- **OpenClaw:** Add `TAVILY_API_KEY` to `~/.openclaw/.env`
- **LangChain:** `pip install langchain-community` + use `TavilySearchResults`
- **LlamaIndex:** `pip install llama-index-tools-tavily`

---

*Skill created: 2026-03-10*
