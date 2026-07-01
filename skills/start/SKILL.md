---
name: start
description: Session initialization. Detect tech stack, check git, ask what to work on.
alwaysApply: false
trigger: start, /start, 开始, 开始做, work on, 开工
model_hint: standard
**第一步 — 调用 MCP（参数名必须精确，不要发明参数）：**

```
mcp__claude-mcp__workflow_step(
    slug="personalwebsite",       # ← 必须叫 slug，不是 project
    workflow="start",
    phase="init"
)
```

---

# Start: Session Initialization
