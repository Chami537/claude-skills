---
name: fix
description: Fast bug-fixing. Triage -> Diagnose -> Plan -> Fix -> Review -> Ship.
alwaysApply: false
trigger: fix, /fix, bug, debug, broken, crash, error, 修, 修bug, 报错, 崩了
model_hint: standard
---

```python
mcp__claude-mcp__workflow_step(
    slug="<项目slug>",            # 必须叫 slug，不是 project
    workflow="fix",
    phase="<phase>",              # diagnose/plan/baseline/fixing/review/ship
    context={"symptoms": [...], "files": [...]}
)
```

symptoms: 报错关键词+堆栈函数名。files: 出问题的文件路径。


执行每个 step 后必须调 mark_step_done(slug, step_index)。全部做完才能 session_write 进下一个 phase。
session_write 返回 GATE 错误 = 有步骤漏了，回去补完。

---

# Fix: Bug Fixing Workflow
