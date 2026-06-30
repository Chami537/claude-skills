# Fix Examples

## Example: App crashes on upgrade

User: `/fix 升级后打开闪退，logcat 显示 Room IllegalStateException`

1. **Agent 调 MCP** → `workflow_step("fix", phase="diagnose", context={...})`
2. **MCP 返回 steps**: patterns_match(扫已知Bug) → diagnose → systematic-debugging
3. **Agent 按 steps 执行**: 复现 → 定位 → `session_write` → 修 → review → ship
4. **Ship**: commit + 自动更新 CLAUDE.md + 新颖Bug自动存pattern

全程 MCP 编排，不需要手动指定阶段。
