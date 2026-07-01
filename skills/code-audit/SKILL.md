---
name: code-audit
description: Project-wide bug scan. Patterns, ponytail, memory, checklist.
alwaysApply: false
trigger: audit, 查bug, 自查, 扫描问题, 代码审查
---

```python
mcp__claude-mcp__workflow_step(
    slug="<项目slug>",            # 必须叫 slug，不是 project
    workflow="code-audit",
    phase="init"
)
```

扫描链: patterns_list -> ponytail-debt -> ponytail-audit -> 通用清单。先查后修。

---

# Code Audit — Project Bug Scan
