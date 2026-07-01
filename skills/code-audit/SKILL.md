---
name: code-audit
description: Project-wide bug scan. Patterns, ponytail, memory, checklist.
trigger: audit, 查bug, 自查, 扫描问题, 代码审查
**第一步 — 调用 MCP（参数名必须精确，不要发明参数）：**

```
mcp__claude-mcp__workflow_step(
    slug="personalwebsite",       # ← 必须叫 slug，不是 project
    workflow="code-audit",
    phase="init"
)
```

---

# Code Audit — Project Bug Scan
