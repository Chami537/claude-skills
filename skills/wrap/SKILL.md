---
name: wrap
description: Post-development retro. Summarize, capture lessons, update progress.
alwaysApply: false
trigger: wrap, /wrap, 总结, 回顾, 复盘, retro, 收尾, done
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(
    slug="<项目slug>",            # 必须叫 slug，不是 project
    workflow="wrap",
    phase="init"
)
```

MCP 自动写 CLAUDE.md (claude_md_append) + 自动存 memory (memory_save)。

---

# Wrap: Post-Development Retro
