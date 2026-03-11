# C2605 玉米期货夜盘交易时间 - 调查报告

## 📋 执行摘要

**调查时间:** 2026-03-10
**调查方法:** 多源网络搜索 + 官方数据源验证
**结论:** 玉米期货夜盘交易状态**存在争议**，建议**继续监控**

---

## 🔍 搜索结果汇总

### 搜索 1: 大连商品交易所 玉米期货 夜盘交易时间 2026 年最新
**来源:** Perplexity Web Search
**结果:** ⚠️ **不确定**

> "截至我知识截止时间（2024 年 6 月），大连商品交易所（DCE）尚未公布 2026 年玉米期货夜盘交易时间的官方调整安排。"
> 
> "**当前**（2024 年）: **21:00 至 23:00**"

---

### 搜索 2: 大商所 玉米 夜盘 21:00-23:00 官方公告 2025 2026
**来源:** Perplexity Web Search
**结果:** ❌ **无夜盘**

> "截至目前（2024 年 6 月），大连商品交易所（大商所）尚未发布关于**2025 年或 2026 年玉米期货夜盘交易时间调整为 21:00–23:00**的官方公告。"
>
> "**玉米期货**（代码：C）"
>
> "大商所的夜盘交易品种主要包括：棕榈油、豆油、豆粕、铁矿石、焦煤、焦炭、乙二醇、苯乙烯、液化石油气（LPG）等，但**玉米和玉米淀粉暂未纳入夜盘交易品种**。"

---

### 搜索 3: 玉米期货 C2605 夜盘 有吗 2026 年 3 月 最新交易时间
**来源:** Perplexity Web Search
**结果:** ✅ **有夜盘**

> "**是的**，大连商品交易所的玉米期货（代码：C）**有夜盘交易**。"
>
> "**夜盘交易时间**（北京时间）: **21:00 – 23:00**"
>
> "C2605 是远期合约，在 2026 年 3 月仍处于活跃交易期，因此**2026 年 3 月应正常交易，包括夜盘**。"

---

### 搜索 4: 大连商品交易所 夜盘交易品种列表 玉米 豆粕 2026
**来源:** Perplexity Web Search
**结果:** ❌ **无夜盘**

> "截至 2024 年，大连商品交易所（DCE）的夜盘交易品种中**不包括玉米**（Corn）"
>
> "**玉米**（C）"

---

### 搜索 5: 大连商品交易所官网
**来源:** web_fetch
**结果:** ❌ **访问失败**

> URL: `https://www.dce.com.cn/dalianshangpin/jyyl/jysj/index.html`
> 
> 错误：`fetch failed` (海外 IP 被封锁)

---

## 📊 结论分析

### 信息冲突

| 来源 | 结论 | 可信度 | 知识截止时间 |
|------|------|--------|-------------|
| 搜索 1 | 有夜盘 (21:00-23:00) | ⚠️ 中 | 2024-06 |
| 搜索 2 | **无夜盘** | ⚠️ 中 | 2024-06 |
| 搜索 3 | **有夜盘** (21:00-23:00) | ⚠️ 中 | 2024-06 |
| 搜索 4 | **无夜盘** | ⚠️ 中 | 2024-06 |
| DCE 官网 | 无法访问 | ❌ - | - |

### 共识评估
- **支持有夜盘**: 2 票
- **支持无夜盘**: 2 票
- **无法确认**: 1 票 (DCE 官网)

**最终判定:** ⚠️ **不确定 **(uncertain)

---

## 💡 建议方案

### 当前策略：继续监控 (Continue Monitoring)

由于信息来源冲突且无法访问官方数据源，建议：

1. **保持夜盘监控** - 继续发送 21:00/22:00/23:00 报告
2. **明确标注数据状态** - 在报告中注明"夜盘交易状态待确认"
3. **每日验证** - 使用自动化工具每日查询最新信息
4. **等待官方确认** - 关注 DCE 官网公告

---

## 🛠️ 自动化验证工具

### 脚本位置
```
/home/admin/.openclaw/workspace/stock-tracker/dce_trading_verifier.py
```

### 使用方法

```bash
# 正常验证 (如果今日已验证则跳过)
python3 dce_trading_verifier.py

# 强制重新验证
python3 dce_trading_verifier.py --force

# JSON 输出 (用于自动化)
python3 dce_trading_verifier.py --json
```

### 输出示例

```
🔍 正在验证夜盘交易状态...
✅ 验证完成 (2026-03-10)
   交易日：True
   夜盘状态：None (不确定)
   共识：uncertain
   建议：continue_monitoring
```

---

## 📅 每日验证流程

### 第一步：检查是否交易日
```python
from dce_trading_verifier import is_trading_day
print(is_trading_day())  # True/False
```

### 第二步：运行验证脚本
```bash
python3 dce_trading_verifier.py --json > /tmp/dce_verify.json
```

### 第三步：解析结果
```json
{
  "status": "verified",
  "date": "2026-03-10",
  "night_session_enabled": null,
  "consensus": "uncertain",
  "recommendation": "continue_monitoring"
}
```

### 第四步：更新监控配置
- 如果 `night_session_enabled: true` → 启用夜盘报告
- 如果 `night_session_enabled: false` → 禁用夜盘报告
- 如果 `night_session_enabled: null` → 继续监控

---

## 🔍 Tavily Search 验证方法 (新增)

### 安装与配置

```bash
# 1. 安装 Tavily Python SDK
pip install tavily-python

# 2. 设置 API Key (添加到 ~/.openclaw/.env)
export TAVILY_API_KEY='tvly-xxxxxxxxxxxxxxxxxxxx'
```

### 验证脚本示例

```python
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])

# 查询夜盘交易时间
response = client.search(
    query="大连商品交易所 玉米期货 C2605 夜盘交易时间 2026",
    search_depth="advanced",
    max_results=5,
    include_answer=True,
    topic="finance",  # 财经主题过滤
    days=7  # 仅最近 7 天的信息
)

print("AI 综合答案:", response['answer'])
print("\n引用来源:")
for result in response['results']:
    print(f"- {result['title']}: {result['url']}")
```

### 预期输出

```json
{
  "query": "大连商品交易所 玉米期货 C2605 夜盘交易时间 2026",
  "answer": "根据大连商品交易所公告，玉米期货自 20XX 年 X 月 X 日起纳入夜盘交易，交易时间为 21:00-23:00...",
  "results": [
    {
      "title": "大商所关于调整玉米期货夜盘交易时间的通知",
      "url": "https://www.dce.com.cn/dalianshangpin/tzgg/xxxxxx.html",
      "content": "...",
      "score": 0.95,
      "published_date": "2026-03-05"
    }
  ]
}
```

### 优势

| 特性 | 说明 |
|------|------|
| **AI 综合答案** | 直接返回综合结论，无需人工阅读多个页面 |
| **时间过滤** | `days=7` 确保获取最新信息 |
| **主题过滤** | `topic="finance"` 过滤无关结果 |
| **引用来源** | 每个结果都有 URL 和内容摘要，可追溯 |
| **无广告** | 干净的搜索结果，适合自动化处理 |

### 集成到自动化流程

```bash
# 在 dce_trading_verifier.py 中添加 Tavily 验证
python3 -c "
from tavily import TavilyClient
import os, json

client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])
r = client.search('玉米期货 夜盘 大商所 2026', topic='finance', days=7)

# 解析结果，判断是否有夜盘
has_night = '21:00' in r['answer'] or '夜盘' in r['answer']
print(json.dumps({'has_night_session': has_night, 'answer': r['answer']}))
"
```

### 独立验证脚本

**位置:** `stock-tracker/docs/tavily-verification-example.py`

```bash
# 基本验证
python3 docs/tavily-verification-example.py

# JSON 输出 (用于自动化)
python3 docs/tavily-verification-example.py --json

# 自定义搜索时间范围
python3 docs/tavily-verification-example.py --days 14

# 自定义查询
python3 docs/tavily-verification-example.py --query "大商所 夜盘品种列表 2026"
```

---

## 🔍 可靠数据源优先级

### 官方数据源 (最可靠)
1. **大连商品交易所官网** - `https://www.dce.com.cn`
   - 业务指引 → 交易时间
   - 通知公告 → 休市安排
2. **中国证监会官网** - `http://www.csrc.gov.cn`
3. **中国期货业协会** - `http://www.cfachina.org`

### AI 搜索验证工具 ⭐ (推荐用于自动化验证)
1. **Tavily Search API** - `https://tavily.com`
   - 专为 AI Agent 设计的搜索 API
   - 支持时间过滤 (`days` 参数)
   - 支持主题过滤 (`topic: "finance"`)
   - 返回 AI 综合答案 + 引用来源
   - **优势:** 干净结果无广告，适合自动化验证

### 第三方数据源 (需交叉验证)
1. **东方财富网期货频道** - `https://futures.eastmoney.com`
2. **新浪财经期货** - `https://finance.sina.com.cn/futures`
3. **文华财经** - `https://www.wenhua.com.cn`
4. **期货公司官网** (中信、国泰君安等)

### 验证方法
1. **多源交叉验证** - 至少 3 个独立来源确认
2. **时间戳检查** - 优先采用最近 30 天的信息
3. **官方优先** - 如有冲突，以官方公告为准
4. **Tavily 快速验证** - 使用 `topic="finance"` + `days=7` 获取最新财经资讯

---

## 📝 状态文件

### 位置
```
/home/admin/.openclaw/workspace/memory/dce-trading-state.json
```

### 结构
```json
{
  "last_verification": "2026-03-10",
  "night_session_enabled": null,
  "verification_sources": [
    {
      "name": "Perplexity Search #1",
      "result": "uncertain",
      "confidence": 0.5
    }
  ],
  "notes": [
    {
      "date": "2026-03-10",
      "consensus": "uncertain",
      "action": "continue_monitoring"
    }
  ]
}
```

---

## ⏭️ 后续行动

### 短期 (本周)
- [x] 创建自动化验证脚本
- [x] 建立状态跟踪文件
- [ ] 集成到每日心跳检查
- [ ] 添加 Discord 通知

### 中期 (本月)
- [ ] 联系期货公司确认夜盘状态
- [ ] 寻找可访问的 DCE 数据源
- [ ] 建立多源自动验证系统

### 长期 (持续)
- [ ] 监控 DCE 官方公告
- [ ] 定期更新节假日日历
- [ ] 优化验证算法

---

## 📞 联系确认 (推荐)

如需 100% 确认，建议直接联系：

| 机构 | 联系方式 |
|------|----------|
| **大连商品交易所** | 0411-84808888 |
| **期货公司客服** | 咨询您的客户经理 |
| **文华财经客服** | 400-700-7979 |

---

*最后更新：2026-03-10 21:35*
*下次验证：2026-03-11 (每日自动)*
