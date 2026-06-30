---
name: start
description: Session initialization. Detect tech stack, check git, ask what to work on.
alwaysApply: false
trigger: start, /start, 开始, 开始做, work on, 开工
model_hint: standard
---

# Start: Session Initialization

```python
mcp__claude-mcp__workflow_step("<slug>", workflow="start", phase="init")
```
**返回的 steps 是唯一权威指令。逐项执行。不要读下方退化文本。**

---

*MCP 不可用时退化路径：*
- 定位项目(hita→E:/HITA_Agent, qqbot→E:/qqbot, ...)
- 检测技术栈(Gradle→Android, requirements.txt→Python)
- 检查 claude-mem(浏览器确认), graphify(建议生成)
- session_read 查未完成工作流
- 读 CLAUDE.md + git log/status
- 路由: dev/fix/refactor/code-audit
