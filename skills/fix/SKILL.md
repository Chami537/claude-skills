---
name: fix
description: Fast bug-fixing.
alwaysApply: false
trigger: fix, /fix, bug, debug, broken, crash, error, 修, 修bug, 报错, 崩了
model_hint: standard
---

Phases: diagnose -> plan -> baseline -> fixing -> review -> ship. GATE blocks advance until current phase steps are done.

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="fix", phase="diagnose", context={"symptoms": [...], "files": [...]})
# Then: phase="plan", phase="baseline", phase="fixing", phase="review", phase="ship"
```
Execute all steps -> mark_step_done each -> session_write(next_phase). MCP down = tell user.
