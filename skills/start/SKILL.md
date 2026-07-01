---
name: start
description: Session initialization. Detect tech stack, check git, ask what to work on.
alwaysApply: false
trigger: start, /start, 开始, 开始做, work on, 开工
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(
    slug="<项目slug>",            # 必须叫 slug，不是 project
    workflow="start",
    phase="init"
)
```

项目映射: hita->E:/HITA_Agent, qqbot->E:/qqbot, personalwebsite->C:/Users/Rinat/Desktop/个人网站。

---

# Start: Session Initialization
