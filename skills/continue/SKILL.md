---
name: continue
description: Cross-session context recovery. Git + session + claude-mem.
alwaysApply: false
trigger: continue, /continue, 继续, 接着做, 上次做到哪, resume
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(
    slug="<项目slug>",            # 必须叫 slug，不是 project
    workflow="continue",
    phase="init"
)
```

不要调 mcp__tokensave__session_recall。claude-mem 不可用时浏览器确认 localhost:37777。

---

# Continue: Cross-Session Context Recovery
