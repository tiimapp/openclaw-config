# 每日交易日验证系统

## 功能概述

在每日第一次心跳时自动验证今天是否为交易日，并根据验证结果决定是否发送 A 股和期货市场的分析报告。

## 工作流程

```
┌─────────────────────────────────────────────────────────────┐
│                    每日第一次心跳 (before 10:00)              │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              读取 memory/heartbeat-state.json                │
│              检查 trading_day_verify 是否等于今天            │
└─────────────────────────────────────────────────────────────┘
                              ↓
                    ┌───────┴───────┐
                    │               │
              已验证 ✓          未验证 ✗
                    │               │
                    │               ↓
                    │    ┌──────────────────────┐
                    │    │ 运行交易日验证脚本    │
                    │    │ heartbeat_trading_   │
                    │    │ check.py             │
                    │    └──────────────────────┘
                    │               ↓
                    │    ┌──────────────────────┐
                    │    │ 调用 trading_time_   │
                    │    │ checker.py           │
                    │    └──────────────────────┘
                    │               ↓
                    │    ┌──────────────────────┐
                    │    │ 更新 state 文件       │
                    │    │ - trading_day_verify │
                    │    │ - is_trading_day     │
                    │    │ - reportSchedule     │
                    │    └──────────────────────┘
                    │               ↓
                    └───────┬───────┘
                            ↓
              ┌─────────────────────────┐
              │   后续心跳不再重复验证   │
              └─────────────────────────┘
```

## 文件结构

```
/home/admin/.openclaw/workspace/
├── HEARTBEAT.md                      # 心跳检查规范 (已更新)
├── heartbeat_trading_check.py        # 交易日验证脚本 (新建)
└── memory/
    └── heartbeat-state.json          # 状态跟踪文件 (已更新)
```

## 状态文件结构

```json
{
  "lastChecks": {
    "trading_day_verify": "2026-03-06",  // 最后验证日期
    "is_trading_day": true               // 是否为交易日
  },
  "reportSchedule": {
    "ashare_daily": "15:30",             // A 股日报时间
    "c2605_hourly": "09:00,10:00,...",   // C2605 小时报时间
    "c2605_daily": "15:30"               // C2605 日报时间
  }
}
```

## 决策逻辑

| 验证结果 | A-Share 日报 | C2605 小时报 | C2605 日报 |
|----------|-------------|-------------|-----------|
| 交易日 ✓  | ✅ 15:30    | ✅ 交易时段  | ✅ 15:30  |
| 非交易日 ✗ | ❌ 跳过     | ❌ 跳过     | ❌ 跳过   |

## 使用命令

### 正常检查 (自动跳过已验证日期)
```bash
cd /home/admin/.openclaw/workspace && python3 heartbeat_trading_check.py
```

### 强制重新验证
```bash
python3 heartbeat_trading_check.py --force
```

### JSON 输出 (用于自动化)
```bash
python3 heartbeat_trading_check.py --json
```

## 输出示例

### 首次验证
```
🔍 Running trading day verification...
✅ Verification complete (2026-03-06)
   Trading day: True
   📈 A-Share daily report: 15:30
   🌽 C2605 hourly reports: 09:00, 10:00, 11:00, 14:00, 15:00
   🌽 C2605 daily summary: 15:30
```

### 已验证后再次检查
```
✅ Already verified today (2026-03-06)
   Trading day: True
   Reports enabled: A-Share daily, C2605 hourly+daily
```

## 集成到心跳流程

在 HEARTBEAT.md 中已规定：
1. **第一次心跳** (每天 before 10:00): 运行 `heartbeat_trading_check.py`
2. **后续心跳**: 读取 state 文件，不重复验证
3. **报告调度**: 根据 `reportSchedule` 决定是否发送报告

## 测试记录

```bash
# Test 1: 首次验证
$ python3 heartbeat_trading_check.py
✅ Verification complete (2026-03-06)
   Trading day: True

# Test 2: 再次运行 (应跳过)
$ python3 heartbeat_trading_check.py
✅ Already verified today (2026-03-06)

# Test 3: 强制重新验证
$ python3 heartbeat_trading_check.py --force
✅ Verification complete (2026-03-06)
```

---
*Created: 2026-03-06 22:00*
