# Code Audit — Examples

## Example: Pre-commit self-audit

User: `/code-audit 只看最近改过的文件`

1. **Agent 调 MCP** → `workflow_step("code-audit", phase="init")`
2. **MCP 返回 steps**: patterns_list → ponytail-debt → 并行扫描 → 报告
3. **输出**: [严重级别] 文件:行号 — 问题 — 根因 — 修复方案 — 来源
4. **修复**: 同根因一次commit, 不同逐项fix

全程 MCP 编排，先查后修，经验优先(count>=2)。
