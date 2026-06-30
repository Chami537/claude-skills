# Wrap Examples

## Example: After refactor session

User: `/wrap`

1. **Agent 调 MCP** → `workflow_step("wrap", phase="init")`
2. **MCP 返回 11 steps** → agent 逐项执行：
   - git summary → ponytail-gain → workflow_health
   - 自动更新 CLAUDE.md + 自动保存 memory
   - checklist_append + patterns_append
   - session_cleanup

全程不问"有什么经验？""完成状态？"——自动从 git 提取，自动存。
