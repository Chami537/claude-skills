---
name: refactor
description: Refactoring & optimization.
alwaysApply: false
trigger: refactor, /refactor, optimize, improve, 优化, 重构, 加速, 性能
model_hint: opus
---

```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="refactor", phase="<phase>", context={"task": "<desc>"})
```
THIS IS THE ONLY INSTRUCTION. Execute returned steps in order. If MCP fails, tell user "MCP down".
