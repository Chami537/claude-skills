# Chami's Claude Code Workflows

自用 Claude Code 工作流技能集 + 配套 MCP Server。

## 目录结构

```
claude-skills/
├── skills/              # 自定义 Skill
│   ├── start/           # 会话初始化
│   ├── dev/             # 新功能开发
│   ├── fix/             # Bug 修复
│   ├── refactor/        # 重构优化
│   ├── wrap/            # 收尾沉淀
│   ├── code-audit/      # Bug 自查
│   ├── ask-teacher/     # 卡住求助
│   └── continue/        # 恢复会话
├── mcp/                 # MCP Server（session/checklist/patterns）
│   ├── server.py
│   └── tools/
└── README.md
```

## 前置依赖

### 1. 安装插件（Claude Code Marketplace）

这些 Skill 会调用其他插件提供的 Skill：

| 依赖的 Skill | 来源插件 | 安装方式 |
|-------------|---------|---------|
| `pensive:unified-review`、`pensive:blast-radius`、`pensive:harden`、`pensive:performance-review`、`pensive:code-refinement`、`pensive:architecture-reviewer` | [pensive](https://github.com/athola/claude-night-market) | `/plugin install pensive@claude-night-market` |
| `conserve:unbloat` | [conserve](https://github.com/athola/claude-night-market) | `/plugin install conserve@claude-night-market` |
| `commit-commands:commit`、`commit-commands:commit-push-pr`、`commit-commands:clean_gone` | [commit-commands](https://github.com/anthropics/claude-plugins-official) | `/plugin install commit-commands@claude-plugins-official` |
| `grill-me`、`diagnose`、`prototype`、`to-issues` | Claude Code 内置 / agent skills | 无需安装（如缺失请装 [agent-sdk](https://github.com/anthropics/claude-agent-sdk)） |
| `simplify` | Claude Code 内置 | 无需安装 |

```bash
# 一键安装所有插件依赖
/plugin install pensive@claude-night-market
/plugin install conserve@claude-night-market
/plugin install commit-commands@claude-plugins-official
```

### 2. 配置 MCP Server

在 Claude Code 的 `settings.json` 中添加：

```json
{
  "mcpServers": {
    "claude-mcp": {
      "command": "python",
      "args": ["<path-to-repo>/mcp/server.py"]
    }
  }
}
```

## 安装

```bash
# 1. 克隆仓库
git clone https://github.com/Chami537/claude-skills.git

# 2. 复制 skill 到 Claude Code 技能目录
#    所有平台通用：将 skills/ 下的每个子目录复制到 ~/.claude/skills/
cp -r skills/* ~/.claude/skills/

# 3. 配置 MCP Server（见上一节）

# 4. 重启 Claude Code
```

## 使用流程

### 完整开发周期

```
/start          → 初始化会话，选定项目
/dev            → 开发新功能（Plan → Build → Review → Harden → Ship）
    └── 卡住了？ → /ask-teacher  整理问题问老师
/fix            → 修 Bug（Triage → Diagnose → Plan → Fix → Review → Ship）
/refactor       → 重构优化（Measure → Plan → TDD → Review → Ship）
    └── 改之前  → /code-audit    扫描已有 Bug
/wrap           → 收尾总结，沉淀经验
/continue       → 下次会话恢复上下文
```

### 工作流 Skill 详解

| 阶段 | dev（开发） | fix（修复） | refactor（重构） |
|------|-----------|------------|-----------------|
| 0 | 规模评估 S/M/L | 扫 patterns 匹配已知 Bug | 读取上次 session |
| 1 | Plan 方案设计 | Diagnose 诊断定位 | Measure 测量基线 |
| 2 | Build 编码实现 | Plan 修复方案 | Plan 重构方案 |
| 3 | Verify 编译验证 | Baseline 基线确认 | Build 执行重构 |
| 4 | Review 代码审查 | Fix 最小修复 | Verify 编译验证 |
| 5 | Harden 安全加固 | Review 回归检查 | Review 回归检查 |
| 6 | Ship 提交发布 | Ship 提交发布 | Ship 提交发布 |

### MCP 追踪

工作流自动通过 MCP Server 追踪进度：

- `session_read/write/cleanup` — 会话状态持久化，24h 内可恢复
- `checklist_read/append` — 验证清单管理
- `patterns_list/match/append` — Bug 模式积累与自动匹配

## Skill 清单

| Skill | 用途 |
|-------|------|
| `start` | 会话初始化：定位项目、检测技术栈、检查未完成工作 |
| `dev` | 新功能开发全流程（Plan→Build→Review→Harden→Ship） |
| `fix` | Bug 修复全流程（Triage→Diagnose→Plan→Fix→Review→Ship） |
| `refactor` | 重构优化全流程（Measure→Plan→TDD→Review→Ship） |
| `wrap` | 收尾沉淀：总结改动、更新 memory、清理分支 |
| `code-audit` | 项目级 bug 自查，扫描潜在问题，给出修复方案 |
| `ask-teacher` | 卡住时整理问题描述，方便问老师 |
| `continue` | 从上次 session 恢复开发上下文 |

## 常见问题

**Q: 为什么不直接用 Claude Code 内置工作流？**

内置工作流是通用的，这套针对个人项目（Android/Python/HTML）做了定制：自动检测技术栈、记住编译命令、按 slug 追踪 session、积累 Bug 模式。

**Q: MCP Server 必须装吗？**

非必须。Skill 调用 MCP tool 失败时会跳过 session/checklist/patterns 追踪，不影响核心工作流。但建议装，否则：
- 不会有跨会话的进度恢复（`/continue` 失效）
- Bug 模式不会积累（每次 `fix` 都是全新诊断）
- 验证清单不会持久化

**Q: 怎么贡献/修改？**

直接改 `<repo>/skills/<name>/SKILL.md`，PR 或自己 fork。Skill 文件都是纯 Markdown，不需要编译。
