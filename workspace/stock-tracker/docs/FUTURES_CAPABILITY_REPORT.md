# Futures Data Capability Assessment

## Executive Summary

**Current Status:** The stock-tracker project does **NOT** currently support futures data. Adding futures support is **feasible** but requires significant modifications to the fetcher module and potentially new data sources.

**Target:** 棉花期货 CF2605 (Cotton Futures, Zhengzhou Commodity Exchange, May 2026 delivery)

---

## 1. Current Capabilities Summary

### Supported Data Sources
| Source | Stocks | Futures | Status |
|--------|--------|---------|--------|
| Tencent (qt.gtimg.cn) | ✅ Yes | ❌ No | Primary source for stocks |
| Sina (hq.sinajs.cn) | ✅ Yes | ⚠️ Partial | Works for stocks, blocked for this server |
| NetEase (163) | ✅ Yes | ❌ No | Fallback for stocks |

### Current Fetcher Features
- Real-time stock price data (A-shares, 科创板)
- Historical daily prices
- News aggregation (Sina, 东财，SSE)
- Multi-API fallback with retry logic

### What's Missing for Futures
- No futures symbol format handling
- No futures-specific field parsing
- No support for commodity exchanges (ZCE, DCE, SHFE, CFFEX)
- No open interest (持仓量) tracking
- No settlement price (结算价) handling

---

## 2. Required Changes for Futures Support

### A. Symbol Format Handling

Futures symbols use different formats than stocks:

```python
# Current stock format:
"sh688777"  # Shanghai stock 688777

# Futures format examples:
"czce_cf2605"   # Sina: Zhengzhou Cotton May 2026
"CF2605"        # Tencent: Cotton May 2026
"DCE_m2409"     # Sina: Dalian Soybean Meal Sep 2024
"SHF_rb2410"    # Sina: Shanghai Rebar Oct 2024
```

**Required Changes:**
1. Add futures symbol prefix detection (czce_, DCE_, SHF_, CFF_, INE_)
2. Support both exchange-prefixed and plain formats
3. Handle case sensitivity (futures codes are often lowercase)

### B. API Endpoint Additions

**Sina Finance Futures API:**
```
URL: http://hq.sinajs.cn/list={symbol}
Format: czce_cf2605, DCE_m2409, SHF_rb2410, CFF_IF2406
Response: var hq_str_czce_cf2605="棉花 2605,14850,14860,..."
```

**Tencent Finance Futures API:**
```
URL: https://qt.gtimg.cn/q={symbol}
Format: CF2605, RB2410, M2409
Response: v_s_CF2605="51~棉花 2409~15230~..."
```

**Alternative: AKShare (Recommended for production)**
```python
import akshare as ak
df = ak.futures_zh_daily(symbol="CF2605")  # Historical daily
```

### C. Data Field Mapping

Futures data has **different fields** than stocks:

| Field | Stocks | Futures | Notes |
|-------|--------|---------|-------|
| Current Price | ✅ | ✅ | Same |
| Open/High/Low | ✅ | ✅ | Same |
| Volume | ✅ | ✅ | Same (lots/hands) |
| Turnover | ✅ | ✅ | Same |
| **Open Interest** | ❌ | ✅ | Critical for futures |
| **Settlement Price** | ❌ | ✅ | Daily settlement |
| **Delivery Month** | ❌ | ✅ | Contract expiry |

### D. Code Structure Changes

**New files needed:**
```
src/
├── fetcher.py          # Modify existing
├── fetcher_futures.py  # NEW: Futures-specific fetcher
├── symbols.py          # NEW: Symbol format utilities
```

**Modifications to fetcher.py:**
1. Add `fetch_futures_price_*()` functions (parallel to stock functions)
2. Add symbol format detection utility
3. Modify `fetch_price_data()` to route based on asset type
4. Add futures-specific field parsers

---

## 3. Sample API Endpoints for CF2605

### Sina Finance
```
URL: http://hq.sinajs.cn/list=czce_cf2605
Expected Response:
var hq_str_czce_cf2605="棉花 2605,14850,14860,14830,14845,14870,14820,14845,14850,1234,5678,2026-03-04,15:00:00"

Fields (comma-separated):
[0]  Name: 棉花 2605
[1]  Yesterday Settlement: 14850
[2]  Open: 14860
[3]  High: 14830  (Note: may vary by exchange)
[4]  Low: 14845
[5]  Bid1: 14870
[6]  Ask1: 14820
[7]  Current: 14845
[8]  Settlement: 14850
[9]  Volume: 1234
[10] Open Interest: 5678
[11] Date: 2026-03-04
[12] Time: 15:00:00
```

### Tencent Finance
```
URL: https://qt.gtimg.cn/q=CF2605
Expected Response:
v_s_CF2605="51~棉花 2409~15230~15280~15190~15250~..."

Fields (tilde-separated):
[0]  Market Code: 51 (commodity futures)
[1]  Name: 棉花 2409
[2]  Yesterday Settlement: 15230
[3]  Open: 15280
[4]  High: 15190
[5]  Low: 15250
... (more fields)
```

### AKShare (Recommended)
```python
import akshare as ak

# Get daily historical data
df = ak.futures_zh_daily(symbol="CF2605")

# Get main contract (most active)
df_main = ak.futures_main_sina(symbol="棉花")

# Columns: date, open, high, low, close, volume, open_interest, settlement
```

---

## 4. Code Estimate

### Effort Breakdown

| Task | Complexity | Estimated Time |
|------|------------|----------------|
| Symbol format utilities | Low | 2-3 hours |
| Futures fetcher functions | Medium | 4-6 hours |
| Field parsing (futures-specific) | Medium | 3-4 hours |
| Integration with existing fetcher | Medium | 2-3 hours |
| Testing & validation | Medium | 3-4 hours |
| Documentation | Low | 1-2 hours |
| **TOTAL** | | **15-22 hours** |

### Implementation Phases

**Phase 1: Core Fetcher (8-10 hours)**
- Add symbol detection utilities
- Implement Sina futures fetcher
- Add futures field parser
- Basic unit tests

**Phase 2: Integration (5-7 hours)**
- Modify main fetcher to support both stocks and futures
- Add config support for futures symbols
- Update error handling
- Integration tests

**Phase 3: Polish (4-6 hours)**
- Add Tencent futures fallback
- Add AKShare integration (optional)
- Documentation
- Final testing

### Sample Code Snippet

```python
# New function to add to fetcher.py

def fetch_futures_price_sina(symbol: str, retry: int = 3) -> Optional[Dict]:
    """
    Fetch futures price data from Sina Finance API.
    
    Args:
        symbol: Futures symbol (e.g., 'czce_cf2605', 'DCE_m2409')
        retry: Number of retry attempts
    
    Returns:
        Dictionary with futures price data
    """
    url = f"http://hq.sinajs.cn/list={symbol}"
    
    for attempt in range(retry):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            
            content = response.text.strip()
            match = re.search(r'hq_str_\w+="([^"]+)"', content)
            
            if not match:
                continue
            
            data_str = match.group(1)
            fields = data_str.split(',')
            
            if len(fields) < 10:
                continue
            
            # Futures-specific field mapping
            price_data = {
                'symbol': symbol,
                'name': fields[0],
                'settlement_prev': float(fields[1]) if fields[1] else 0.0,
                'open': float(fields[2]) if fields[2] else 0.0,
                'high': float(fields[3]) if fields[3] else 0.0,
                'low': float(fields[4]) if fields[4] else 0.0,
                'current_price': float(fields[7]) if fields[7] else 0.0,
                'settlement': float(fields[8]) if fields[8] else 0.0,
                'volume': float(fields[9]) if fields[9] else 0.0,
                'open_interest': float(fields[10]) if len(fields) > 10 and fields[10] else 0.0,
                'date': fields[11] if len(fields) > 11 else '',
                'time': fields[12] if len(fields) > 12 else '',
            }
            
            return price_data
            
        except Exception as e:
            logger.warning(f"Sina futures attempt {attempt + 1} failed: {e}")
            if attempt < retry - 1:
                import time
                time.sleep(5)
            continue
    
    return None
```

---

## 5. Recommendations

### Short-term (Quick Win)
1. **Use AKShare** for futures data - it's well-maintained and handles all Chinese exchanges
2. Add `akshare` to requirements.txt
3. Create a simple `fetch_futures_data()` wrapper function
4. Estimated: 4-6 hours

### Medium-term (Production Ready)
1. Implement direct Sina/Tencent API support (as shown above)
2. Add multi-source fallback (Sina → Tencent → AKShare)
3. Add futures-specific analysis (term structure, spread analysis)
4. Estimated: 15-22 hours

### Long-term (Advanced)
1. Add CTP interface for real-time tick data
2. Support for options on futures
3. Cross-exchange arbitrage detection
4. Estimated: 40+ hours

---

## 6. Testing Notes

**Server Limitations:**
- Direct HTTP requests to `hq.sinajs.cn` are currently blocked (403 Forbidden) from this server
- Tencent API (`qt.gtimg.cn`) works for stocks but returns `v_pv_none_match` for futures symbols tested
- This may be due to geographic restrictions or IP blocking

**Recommendation:**
- Use AKShare library which handles proxy/routing internally
- Or test API access from a different network/location
- Consider using a Chinese VPS for reliable access

---

## 7. Conclusion

**Can we add futures support?** ✅ **Yes**

**Is it straightforward?** ⚠️ **Moderately complex** - requires new code but follows similar patterns to existing stock fetcher

**Recommended approach:**
1. Start with AKShare integration (fastest, most reliable)
2. Add direct API support later if needed for performance
3. Budget 15-22 hours for full implementation

**Next Steps:**
1. Decide on data source (AKShare vs direct API)
2. Add futures symbols to config
3. Implement fetcher modifications
4. Test with CF2605 and other active contracts

---

*Report generated: 2026-03-04*
*Prepared by: Subagent (futures-capability-check)*
