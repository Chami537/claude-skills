---
name: fix
description: Fast bug-fixing. Triage -> Diagnose -> Plan -> Fix -> Review -> Ship.
alwaysApply: false
trigger: fix, /fix, bug, debug, broken, crash, error, 修, 修bug, 报错, 崩了
model_hint: standard
**第一步 — 调用 MCP（参数名必须精确，不要发明参数）：**

```
mcp__claude-mcp__workflow_step(
    slug="personalwebsite",       # ← 必须叫 slug，不是 project
    workflow="fix",
    phase="diagnose",
    context={"symptoms": [...], "files": [...]}
)
```

---

# Fix: Bug Fixing Workflow
