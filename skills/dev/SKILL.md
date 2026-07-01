---
name: dev
description: New feature development.
alwaysApply: false
trigger: dev, /dev, new feature, implement, 开发, 新功能, 加个, 做一个
model_hint: opus
---

Phases: plan -> build -> verify -> review -> harden -> ship. GATE blocks advance until current phase steps are done.

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="dev", phase="plan", scale="S|M|L", context={"task": "<desc>"})
# Then: phase="build", phase="verify", phase="review", phase="harden", phase="ship"
```
Execute all steps -> mark_step_done each -> session_write(next_phase). MCP down = tell user.
