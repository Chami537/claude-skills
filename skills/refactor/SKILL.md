---
name: refactor
description: Refactoring & optimization. Measure -> Plan -> TDD -> Review -> Ship.
alwaysApply: false
trigger: refactor, /refactor, optimize, improve, 优化, 重构, 加速, 性能
model_hint: opus
---

```python
mcp__claude-mcp__workflow_step(
    slug="<项目slug>",            # 必须叫 slug，不是 project
    workflow="refactor",
    phase="<phase>",              # measure/plan/build/verify/review/ship
    context={"task": "<描述>"}
)
```

Phase 1 Measure 先跑 Ponytail-audit。Phase 5 Review 对比 baseline。


执行每个 step 后必须调 mark_step_done(slug, step_index)。全部做完才能 session_write 进下一个 phase。
session_write 返回 GATE 错误 = 有步骤漏了，回去补完。

---

# Refactor: Optimization & Refactoring Workflow
