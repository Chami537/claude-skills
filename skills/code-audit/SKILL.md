---
name: code-audit
description: Project-wide bug scan. Patterns, ponytail, memory, checklist.
trigger: audit, 查bug, 自查, 扫描问题, 代码审查
---

# Code Audit — Project Bug Scan

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="code-audit", phase="init")
```
**返回的 steps 是唯一权威指令。逐项执行。不要读下方退化文本。**

---

*MCP 不可用时退化路径：*
- patterns_list + 关键词grep全项目
- ponytail-debt 债台账
- 读 MEMORY.md + REFERENCE.md(不存在跳过)
- 并行扫描: patterns grep + ponytail-audit + 通用清单
- 报告: [CRITICAL/HIGH/MEDIUM/LOW] + 根因 + 修复方案
- 修复: 同根因→一次commit, 不同→逐项fix
- 规则: 先查后修, 经验优先(count>=2), 不确定标MEDIUM
