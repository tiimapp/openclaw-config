# AKShare Migration Checklist - Stock Tracker

**Goal:** Migrate all price data APIs to AKShare (cost-free solution)
**Acceptance:** 15-20min data delays are acceptable

---

## Phase 1: Audit & Planning

- [x] **1.1** Clone repo and analyze current codebase (IN PROGRESS - Code_G working on it)
- [ ] **1.2** Document all current API calls (endpoints, functions, symbols)
- [ ] **1.3** Map current APIs → AKShare equivalents
- [ ] **1.4** Create migration plan with file-by-file changes

---

## Phase 2: Core Migration

- [ ] **2.1** Add AKShare dependency to requirements.txt
- [ ] **2.2** Create new `akshare_client.py` module (wrapper with fallback logic)
- [ ] **2.3** Migrate A-share price fetching to AKShare
- [ ] **2.4** Migrate commodity futures fetching to AKShare
- [ ] **2.5** Add data freshness indicators (timestamp, delay warnings)

---

## Phase 3: Testing

- [ ] **3.1** Test A-share symbols (e.g., 中控技术 688777)
- [ ] **3.2** Test commodity futures (玉米期货 C2605)
- [ ] **3.3** Verify fallback logic works
- [ ] **3.4** Run existing test suite (if any)

---

## Phase 4: Documentation & Cleanup

- [ ] **4.1** Update README with AKShare info and delay notices
- [ ] **4.2** Add inline comments explaining data limitations
- [ ] **4.3** Remove old API dependencies (if fully replaced)
- [ ] **4.4** Commit and push to GitHub

---

## Phase 5: Post-Migration

- [ ] **5.1** Verify cron jobs still work with new APIs
- [ ] **5.2** Monitor for 24h to catch any edge cases
- [ ] **5.3** Update MEMORY.md with completion status

---

**Started:** 2026-03-05 ~15:00
**Status:** In Progress (previous attempts timed out - switching to incremental approach)
