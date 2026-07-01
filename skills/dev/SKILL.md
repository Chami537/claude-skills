---
name: dev
description: New feature development. Plan -> Build -> Review -> Harden -> Ship.
alwaysApply: false
trigger: dev, /dev, new feature, implement, 开发, 新功能, 加个, 做一个
model_hint: opus
---

```python
mcp__claude-mcp__workflow_step(
    slug="<项目slug>",            # 必须叫 slug，不是 project/name/id
    workflow="dev",
    phase="<phase>",              # plan/build/verify/review/harden/ship
    scale="S|M|L",                # S:单文件<50行, M:多文件, L:新模块
    context={"task": "<功能描述>"}
)
```

scale 取值: S(单文件<50行 跳过Ponytail) M(多文件) L(新模块/架构变更)。

---

# Dev: New Feature Workflow
