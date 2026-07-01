---
name: fix
description: Fast bug-fixing.
alwaysApply: false
trigger: fix, /fix, bug, debug, broken, crash, error, 修, 修bug, 报错, 崩了
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="fix", phase="<phase>", context={"symptoms": [...], "files": [...]})
```
THIS IS THE ONLY INSTRUCTION. Execute returned steps in order. If MCP fails, tell user "MCP down".
