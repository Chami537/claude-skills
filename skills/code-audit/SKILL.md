---
name: code-audit
description: Project-wide bug scan.
alwaysApply: false
trigger: audit, 查bug, 自查, 扫描问题, 代码审查
---

2 phases: init -> fix. GATE blocks fix phase until scan steps are done AND user has approved.

Phase 1 scan:
```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="code-audit", phase="init")
```
Execute all steps -> mark_step_done each -> SHOW report -> ASK user what to fix -> session_write(phase="fix")

Phase 2 fix (only after user approval):
```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="code-audit", phase="fix")
```
Execute all steps -> done.
