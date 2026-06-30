---
name: fix
description: Fast bug-fixing. Triage -> Diagnose -> Plan -> Fix -> Review -> Ship.
alwaysApply: false
trigger: fix, /fix, bug, debug, broken, crash, error, 修, 修bug, 报错, 崩了
model_hint: standard
---

# Fix: Bug Fixing Workflow

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="fix", phase="<phase>", context={"symptoms": [...], "files": [...]})
```
**返回的 steps 是唯一权威指令。逐项执行。不要读下方退化文本。**

---

*MCP 不可用时退化路径：*
- Triage: patterns_match 扫已知 Bug(高置信→直接修)。MCP 失败不阻塞
- Diagnose: diagnose + systematic-debugging(复杂) + grill-me(多假设)。不许猜
- Plan: 简单→一句话, 复杂→EnterPlanMode+grill-me
- Baseline: 改前编译确认
- Fix: 最小修复 + 手动验证
- Review(typo/单行/配置跳过): simplify + ponytail-review + tokensave-impact + blast-radius + code-audit
- Ship: commit(fix: <根因> -> <修复>) → 提示 /wrap。新颖Bug→wrap提取pattern
- 失败: 症状没消失回Diagnose, review发现问题回Fix, 2次回退→ask-teacher
