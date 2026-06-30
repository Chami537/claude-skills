---
name: fix
description: Fast bug-fixing. Triage -> Diagnose -> Plan -> Fix -> Review -> Ship.
alwaysApply: false
trigger: fix, /fix, bug, debug, broken, crash, error, 修, 修bug, 报错, 崩了
model_hint: standard
---

# Fix: Bug Fixing Workflow

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="fix", phase="<phase>", context={"symptoms": [...], "files": [...]})
```
**返回的 steps 是唯一指令。MCP 不可用时报告用户，不要自己发挥。**
