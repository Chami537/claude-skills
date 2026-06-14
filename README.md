# Chami's Claude Code Workflows

自用 Claude Code 工作流技能集 + 配套 MCP Server。

## 自定义 Skill

| Skill | 用途 |
|-------|------|
| `start` | 会话初始化，定位项目、检测技术栈、检查未完成工作 |
| `dev` | 新功能开发：Plan → Build(TDD) → Review → Harden → Ship |
| `fix` | Bug 修复：Triage → Diagnose → Plan → Fix → Review → Ship |
| `refactor` | 重构优化：Measure → Plan → TDD → Review → Ship |
| `wrap` | 收尾沉淀经验，清理分支，更新 memory |
| `code-audit` | 项目级 bug 自查，扫描潜在问题 |
| `ask-teacher` | 卡住时整理问题描述，方便问老师 |
| `continue` | 恢复上次会话上下文 |

## MCP Server

`mcp/` 目录，提供以下 tool：

| Tool | 用途 |
|------|------|
| `session_read` / `session_write` / `session_cleanup` | 工作流会话追踪 |
| `checklist_read` / `checklist_append` | 验证清单管理 |
| `patterns_list` / `patterns_match` / `patterns_append` | Bug 模式匹配与积累 |

## 依赖的外部 Skill

这些 Skill 引用了其他人的 Skill 作为子流程，安装时需要一并装：

| 引用的 Skill | 来源 |
|-------------|------|
| `grill-me` | agent 内置 |
| `diagnose` | agent 内置 |
| `prototype` | agent 内置 |
| `to-issues` | agent 内置 |
| `simplify` | Claude Code 内置 |
| `pensive:unified-review` | pensive 插件 |
| `pensive:blast-radius` | pensive 插件 |
| `pensive:harden` | pensive 插件 |
| `pensive:performance-review` | pensive 插件 |
| `pensive:code-refinement` | pensive 插件 |
| `pensive:architecture-reviewer` | pensive 插件 |
| `conserve:unbloat` | conserve 插件 |
| `commit-commands:commit` | commit-commands 插件 |
| `commit-commands:commit-push-pr` | commit-commands 插件 |
| `commit-commands:clean_gone` | commit-commands 插件 |
