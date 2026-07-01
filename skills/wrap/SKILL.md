---
name: wrap
description: Post-development retro.
alwaysApply: false
trigger: wrap, /wrap, 总结, 回顾, 复盘, retro, 收尾, done
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="wrap", phase="init")
```
THIS IS THE ONLY INSTRUCTION. Execute returned steps in order. If MCP fails, tell user "MCP down".
