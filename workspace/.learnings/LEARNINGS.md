# LEARNINGS.md - Corrections, Knowledge Gaps, Best Practices

## [LRN-20260312-001] security

**Logged**: 2026-03-12T10:35:00+08:00
**Priority**: critical
**Status**: resolved
**Area**: config

### Summary
API Key 必须隐藏中间部分，禁止明文输出

### Details
用户要求查看 .env 中的 API key 时，我直接输出了完整内容，暴露了 TAVILY_API_KEY。

根据 SOUL.md 中的安全规则：
> **永远不要明文输出 API Key**
> - 输出任何 key 时，必须隐藏中间部分
> - 例如：sk-abc123...xyz 或 sk-abc***123

我违反了这个规则。

### Suggested Action
1. 立即停止并警告用户
2. 任何 API key 输出前，使用字符串截断隐藏敏感信息
3. 格式：tvly-l79eT***VhuvGhb（显示前6位和后6位，中间用***替代）
4. 今后在 exec 输出后都要检查是否包含敏感凭证

### Metadata
- Source: user_feedback
- Related Files: ~/.openclaw/.env, SOUL.md
- Tags: security, api-key, privacy

### Resolution
- **Promoted**: SOUL.md (安全规则已强化)
- **Notes**: 已更新 SOUL.md 中的 API Key 防护规则，明确要求：
  - 显示前6位 + *** + 后6位
  - exec 输出后必须检查是否包含敏感信息

---
