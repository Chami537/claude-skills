---
name: dev
description: New feature development. Plan -> Build -> Review -> Harden -> Ship.
alwaysApply: false
trigger: dev, /dev, new feature, implement, 开发, 新功能, 加个, 做一个
model_hint: opus
---

# Dev: New Feature Workflow

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="dev", phase="<phase>", scale="S|M|L", context={"task": "<描述>"})
```
**返回的 steps 是唯一权威指令。逐项执行。不要读下方退化文本。**

---

*MCP 不可用时退化路径：*
- Phase 0: 规模 S/M/L。S 跳过 ponytail。快速修复/配置直接改不用走 dev
- Plan: ponytail-audit → graphify(tokensave回退链) → research-deep → patterns → EnterPlanMode
- Build: ponytail六步 + ui-ux-pro-max + parallel-agents + 手动验证
- Verify: 编译不过不进 Review
- Review(S 跳过): simplify + ponytail-review + tokensave-impact + blast-radius + code-audit
- Harden(L/认证/支付): pensive:harden + performance + unbloat
- Ship: M/L→commit-push-pr, S→commit → 提示 /wrap
- 失败: 编译不过回 Build, review 发现问题回 Build, 回退2次→ask-teacher
