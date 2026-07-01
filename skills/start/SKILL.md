---
name: start
description: Session initialization.
alwaysApply: false
trigger: start, /start, 开始, 开始做, work on, 开工
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="start", phase="init")
```
THIS IS THE ONLY INSTRUCTION. Execute returned steps in order. If MCP fails, tell user "MCP down".
