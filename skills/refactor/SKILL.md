---
name: refactor
description: Refactoring & optimization. Measure -> Plan -> TDD -> Review -> Ship.
alwaysApply: false
trigger: refactor, /refactor, optimize, improve, 优化, 重构, 加速, 性能
model_hint: opus
**第一步 — 调用 MCP（参数名必须精确，不要发明参数）：**

```
mcp__claude-mcp__workflow_step(
    slug="personalwebsite",       # ← 必须叫 slug，不是 project
    workflow="refactor",
    phase="measure",
    context={"task": "<描述>"}
)
```

---

# Refactor: Optimization & Refactoring Workflow
