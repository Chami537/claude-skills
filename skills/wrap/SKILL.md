---
name: wrap
description: Post-development retro.
alwaysApply: false
trigger: wrap, /wrap, 总结, 回顾, 复盘, retro, 收尾, done
model_hint: standard
---

Wrap has 3 phases: init -> save -> clean. You MUST complete all 3. GATE blocks advance until all steps in current phase are done.

Phase 1 init:
```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="wrap", phase="init")
```
Execute all steps -> mark_step_done for each -> session_write(phase="save")

Phase 2 save:
```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="wrap", phase="save")
```
Execute all steps -> mark_step_done for each -> session_write(phase="clean")

Phase 3 clean:
```python
mcp__claude-mcp__workflow_step(slug="<slug>", workflow="wrap", phase="clean")
```
Execute all steps -> done.
