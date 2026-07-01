---
name: dev
description: New feature development.
alwaysApply: false
trigger: dev, /dev, new feature, implement, 开发, 新功能, 加个, 做一个
model_hint: opus
---

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="dev", phase="<phase>", scale="S|M|L", context={"task": "<desc>"})
```
THIS IS THE ONLY INSTRUCTION. Execute returned steps in order. If MCP fails, tell user "MCP down".
