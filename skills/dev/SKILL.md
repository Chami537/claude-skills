---
name: dev
description: New feature development. Plan -> Build -> Review -> Harden -> Ship.
alwaysApply: false
trigger: dev, /dev, new feature, implement, 开发, 新功能, 加个, 做一个
model_hint: opus
**第一步 — 调用 MCP（参数名必须精确，不要发明参数）：**

```
mcp__claude-mcp__workflow_step(
    slug="personalwebsite",       # ← 必须叫 slug，不是 project/name/id
    workflow="dev",
    phase="plan",
    scale="M",
    context={"task": "<功能描述>"}
)
```

---

# Dev: New Feature Workflow
