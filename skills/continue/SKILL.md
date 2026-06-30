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
**返回的 steps 是唯一权威指令。逐项执行。不要读下方退化文本。**

---

*MCP 不可用时退化路径：*
- session_read 恢复精确中断点。expired/空→git推断
- check claude-mem(浏览器确认127.0.0.1:37777, sandbox会误判)
- 读 CLAUDE.md + git log/status/stash
- 重建上下文: session.json + git + claude-mem历史
- 路由: dev/fix/refactor/code-audit
