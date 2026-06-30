---
name: wrap
description: Post-development retro. Summarize, capture lessons, update progress.
alwaysApply: false
trigger: wrap, /wrap, 总结, 回顾, 复盘, retro, 收尾, done
model_hint: standard
---

# Wrap: Post-Development Retro

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="wrap", phase="init")
```
**返回的 steps 是唯一权威指令。逐项执行。不要读下方退化文本。**

---

*MCP 不可用时退化路径：*
- git summary(log + diff stat)
- ponytail-gain 记分板
- workflow_health 降级报告
- headroom_compress 上下文压缩
- 经验提取: git diff → feedback memory。trivial 跳过
- checklist_append + patterns_append(新颖Bug)
- session_cleanup
- 提示: 完成→clean_gone, 部分→to-issues
