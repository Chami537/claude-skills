---
name: dev
description: New feature development. Plan -> Build -> Review -> Harden -> Ship.
alwaysApply: false
trigger: dev, /dev, new feature, implement, 开发, 新功能, 加个, 做一个
model_hint: opus
---

# Dev: New Feature Workflow

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="dev", phase="<phase>", scale="S|M|L", context={"task": "<描述>"})
```
**返回的 steps 是唯一指令。MCP 不可用时报告用户，不要自己发挥。**
