---
name: refactor
description: Refactoring & optimization.
alwaysApply: false
trigger: refactor, /refactor, optimize, improve, 优化, 重构, 加速, 性能
model_hint: opus
---

Phases: measure -> plan -> build -> verify -> review -> ship. GATE blocks advance until current phase steps are done.

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="refactor", phase="measure", context={"task": "<desc>"})
# Then: phase="plan", phase="build", phase="verify", phase="review", phase="ship"
```
Execute all steps -> mark_step_done each -> session_write(next_phase). MCP down = tell user.
