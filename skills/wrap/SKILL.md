---
name: wrap
description: Post-development retro. Summarize, capture lessons, update progress.
alwaysApply: false
trigger: wrap, /wrap, 总结, 回顾, 复盘, retro, 收尾, done
model_hint: standard
**第一步 — 调用 MCP（参数名必须精确，不要发明参数）：**

```
mcp__claude-mcp__workflow_step(
    slug="personalwebsite",       # ← 必须叫 slug，不是 project
    workflow="wrap",
    phase="init"
)
```

---

# Wrap: Post-Development Retro
