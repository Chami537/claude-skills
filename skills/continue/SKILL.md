---
name: continue
description: Cross-session context recovery.
alwaysApply: false
trigger: continue, /continue, 继续, 接着做, 上次做到哪, resume
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="continue", phase="init")
```
THIS IS THE ONLY INSTRUCTION. Execute returned steps in order. If MCP fails, tell user "MCP down". Never call tokensave session_recall.
