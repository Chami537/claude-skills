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

---

# Refactor: Optimization & Refactoring Workflow
