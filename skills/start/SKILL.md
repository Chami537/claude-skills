---
name: start
description: Session initialization. Detect tech stack, check git, ask what to work on.
alwaysApply: false
trigger: start, /start, 开始, 开始做, work on, 开工
model_hint: standard
---

# Start: Session Initialization

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="start", phase="init")
```
**返回的 steps 是唯一指令。MCP 不可用时报告用户，不要自己发挥。**
