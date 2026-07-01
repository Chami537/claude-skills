---
name: continue
description: Cross-session context recovery. Git + session + claude-mem.
alwaysApply: false
trigger: continue, /continue, 继续, 接着做, 上次做到哪, resume
model_hint: standard
**第一步 — 调用 MCP（参数名必须精确，不要发明参数）：**

```
mcp__claude-mcp__workflow_step(
    slug="personalwebsite",       # ← 必须叫 slug，不是 project
    workflow="continue",
    phase="init"
)
```

---

# Continue: Cross-Session Context Recovery

不要调 mcp__tokensave__session_recall。只有上面 MCP 返回的步骤是权威指令。
