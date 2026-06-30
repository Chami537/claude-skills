---
name: refactor
description: Refactoring & optimization. Measure -> Plan -> TDD -> Review -> Ship.
alwaysApply: false
trigger: refactor, /refactor, optimize, improve, 优化, 重构, 加速, 性能
model_hint: opus
---

# Refactor: Optimization & Refactoring Workflow

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="refactor", phase="<phase>", context={"task": "<描述>"})
```
**返回的 steps 是唯一指令。MCP 不可用时报告用户，不要自己发挥。**
