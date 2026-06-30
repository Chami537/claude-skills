---
name: continue
description: Cross-session context recovery. Git + session + claude-mem.
alwaysApply: false
trigger: continue, /continue, 继续, 接着做, 上次做到哪, resume
model_hint: standard
---

# Continue: Cross-Session Context Recovery

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="continue", phase="init")
# 不要调 mcp__tokensave__session_recall — 对新项目会卡死
```
**返回的 steps 是唯一指令。MCP 不可用时报告用户，不要自己发挥。**
