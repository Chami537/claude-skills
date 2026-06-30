# Refactor Examples

## Example: Extract duplicate code

User: `/refactor 两个Card组件有很多重复布局，提取公共组件`

1. **Agent 调 MCP** → `workflow_step("refactor", phase="measure")`
2. **MCP 返回 steps**: ponytail-audit → code_graph → choose_metric → record_baseline
3. **Agent 按 steps 执行**: 测量 → Plan → Build → Verify → Review(含数据对比) → Ship
4. **Ship**: commit(含改前/改后数据) + 自动更新 CLAUDE.md

全程 MCP 编排，Review 自动对比 Phase 1 baseline。
