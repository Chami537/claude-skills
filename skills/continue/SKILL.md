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

第一步必须是：

不要传 args 数组，不要传 from_plugin。slug 用项目目录的小写英文名（如 personal_website、hita）。
不要调 mcp__tokensave__session_recall。

返回的 steps 是唯一指令。MCP 失败时报用户，不要自己发挥。
