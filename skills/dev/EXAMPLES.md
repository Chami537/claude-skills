# Dev Examples

## Example: Add dark mode toggle

User: `/dev 加个暗色模式切换`

1. **Agent 调 MCP** → `workflow_step("dev", phase="plan", scale="M")`
2. **MCP 返回 steps**: ponytail-audit → code_graph → patterns
3. **Agent 按 steps 执行** → 读代码 → EnterPlanMode → 出方案
4. **Phase 2 Build** → `workflow_step("dev", "build")` → 执行
5. **Phase 4 Review** → simplify + ponytail-review + blast-radius
6. **Phase 6 Ship** → commit + 自动更新 CLAUDE.md

全程不需要用户在中间追问步骤——MCP 编排保证一致性。
