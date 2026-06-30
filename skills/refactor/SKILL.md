---
name: refactor
description: Refactoring & optimization. Measure -> Plan -> TDD -> Review -> Ship.
alwaysApply: false
trigger: refactor, /refactor, optimize, improve, 优化, 重构, 加速, 性能
model_hint: opus
---

# Refactor: Optimization & Refactoring Workflow

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="refactor", phase="<phase>", context={"task": "<描述>"})
```
**返回的 steps 是唯一权威指令。逐项执行。不要读下方退化文本。**

---

*MCP 不可用时退化路径：*
- Measure: ponytail-audit + graphify(tokensave回退链) + 按需选指标 → 记录基线
- Plan: 简单→一句话, 复杂→EnterPlanMode+grill-me
- Build: 保持测试绿 → 改 → 确认
- Verify: 编译不过=没做
- Review: 回归检查 + blast-radius + simplify + ponytail-review + UX一致性 + unified-review → 对比baseline
- Ship: commit(含数据对比) → 提示 /wrap
- 失败: 编译不过回Build, 指标变差回Plan, 2次回退→ask-teacher
