# Chami's Claude Code Workflows

自用 Claude Code 工作流技能集 + 配套 MCP Server。**已集成 ponytail / superpowers / ui-ux-pro-max / deep-research / claude-mem / graphify / agent-reach / tokensave / headroom 等生态插件。**

## 快速链接

| 工具 | GitHub | 安装 |
|------|--------|------|
| **ponytail** | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | `npx skills add DietrichGebert/ponytail` |
| **superpowers** | [obra/superpowers](https://github.com/obra/superpowers) | `/plugin install superpowers@claude-plugins-official` |
| **ui-ux-pro-max** | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill` |
| **deep-research** | [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) | `npx skills add Weizhena/Deep-Research-skills` |
| **graphify** | [safishamsi/graphify](https://github.com/safishamsi/graphify) | `pip install graphifyy && graphify install --platform windows` |
| **agent-reach** | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | `pip install agent-reach && agent-reach install --env=auto` |
| **claude-mem** | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | `npx claude-mem install` |
| **headroom** | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | `pip install headroom-ai[all] && headroom wrap claude` |
| **pensive** | [athola/claude-night-market](https://github.com/athola/claude-night-market) | `/plugin install pensive@claude-night-market` |
| **conserve** | [athola/claude-night-market](https://github.com/athola/claude-night-market) | `/plugin install conserve@claude-night-market` |
| **commit-commands** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | `/plugin install commit-commands@claude-plugins-official` |
| **mattpocock/skills** | [mattpocock/skills](https://github.com/mattpocock/skills) | `git clone https://github.com/mattpocock/skills ~/.agents/skills` |
| **Bun** | [oven-sh/bun](https://github.com/oven-sh/bun) | `winget install Oven-sh.Bun` |
| **uv** | [astral-sh/uv](https://github.com/astral-sh/uv) | `pip install uv` |

## 一键安装

```bash
/plugin install superpowers@claude-plugins-official
/plugin install pensive@claude-night-market
/plugin install conserve@claude-night-market
/plugin install commit-commands@claude-plugins-official
npx skills add DietrichGebert/ponytail
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
npx skills add Weizhena/Deep-Research-skills
pip install graphifyy && graphify install --platform windows
pip install agent-reach && agent-reach install --env=auto
pip install headroom-ai[all] && headroom wrap claude
pip install uv && npx claude-mem install
```

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

## 安装

```bash
git clone https://github.com/Chami537/claude-skills.git
cp -r skills/* ~/.claude/skills/
# 安装插件依赖（见上面"一键安装"）
# 配置 MCP Server（见下面）
# 重启 Claude Code
```

## MCP Server 配置

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

## 使用流程

```
/start          -> 初始化会话，选定项目
                    ├── 检查 claude-mem 跨会话记忆
                    └── 检查 graphify 知识图谱
/dev            -> 开发新功能（Plan -> Build -> Review -> Harden -> Ship）
    ├── Plan   -> ponytail-audit -> research-deep + agent-reach
    │           -> tokensave_context -> EnterPlanMode
    ├── Build  -> ui-ux-pro-max + parallel-agents + ponytail 六步
    └── Review -> ponytail-review + tokensave_impact + blast-radius + code-audit
/fix            -> 修 Bug（Triage -> Diagnose -> Plan -> Fix -> Review -> Ship）
    ├── Diagnose -> systematic-debugging + grill-me
    └── Review  -> ponytail-review + tokensave_impact + blast-radius
/refactor       -> 重构优化（Measure -> Plan -> TDD -> Review -> Ship）
    ├── Measure -> ponytail-audit + tokensave_context
    └── Review  -> ponytail-review + ui-ux-pro-max UX 一致性
/code-audit     -> 项目级 bug 自查
    ├── 情报   -> patterns.json + ponytail-debt + memory
    └── 扫描   -> ponytail-audit + 通用清单
/wrap           -> 收尾总结
    ├── ponytail-gain（节省记分板）
    └── headroom_compress（上下文压缩存档）
/continue       -> 下次会话恢复上下文
    ├── session.json -> 精确恢复到中断的 phase
    └── claude-mem -> 补充历史操作上下文
```

## 嵌入矩阵

| Skill | ponytail | superpowers | ui-ux-pro | deep-research | claude-mem | graphify | agent-reach | tokensave | headroom |
|-------|----------|-------------|-----------|---------------|------------|----------|-------------|-----------|----------|
| **dev** | audit+review+六步 | parallel-agents | UI 注入 | 技术选型 | - | - | 外部调研 | context+impact | - |
| **fix** | review | systematic-debugging | - | - | - | - | - | impact | - |
| **refactor** | audit+review | - | UX 一致性 | - | - | - | - | context | - |
| **code-audit** | debt+audit | - | - | - | - | - | - | - | - |
| **start** | - | - | - | - | 状态检查 | 图谱报告 | - | - | - |
| **continue** | - | - | - | - | 历史上下文 | - | - | - | - |
| **wrap** | gain | - | - | - | - | - | - | - | compress |

## Skill 清单

| Skill | 用途 | 嵌入的新能力 |
|-------|------|-------------|
| `start` | 会话初始化：定位项目、检测技术栈、检查未完成工作 | claude-mem 状态 / graphify 图谱报告 |
| `dev` | 新功能开发全流程（Plan->Build->Review->Harden->Ship） | ponytail + research-deep + agent-reach + tokensave + ui-ux-pro-max + parallel-agents |
| `fix` | Bug 修复全流程（Triage->Diagnose->Plan->Fix->Review->Ship） | systematic-debugging + ponytail-review + tokensave_impact |
| `refactor` | 重构优化全流程（Measure->Plan->TDD->Review->Ship） | ponytail-audit + tokensave_context + ponytail-review + ui-ux-pro-max UX |
| `wrap` | 收尾沉淀：总结改动、沉淀经验、更新进度 | ponytail-gain + headroom_compress |
| `code-audit` | 项目级 bug 自查，扫描潜在问题，给出修复方案 | ponytail-debt + ponytail-audit |
| `ask-teacher` | 卡住时整理问题描述，方便问老师 | - |
| `continue` | 从上次 session 恢复开发上下文 | claude-mem 历史上下文 |

## MCP 追踪

- `session_read/write/cleanup` -- 会话状态持久化，24h 内可恢复
- `checklist_read/append` -- 验证清单管理
- `patterns_list/match/append` -- Bug 模式积累与自动匹配
- `tokensave_context` -- 代码图谱上下文，比 Agent(Explore) 快
- `tokensave_impact` -- 图谱感知的影响面分析
- `headroom_compress` -- 上下文压缩，防经验丢失
- `claude-mem` -- 跨会话记忆持久化，自动注入历史上下文

## 常见问题

**Q: 所有插件都必须装吗？** 非必须。插件调用失败时自动跳过。但：不装 **ponytail** 失去过度工程检测；不装 **claude-mem** 跨会话记忆失效；不装 **MCP Server** session/checklist/patterns 追踪失效。

**Q: 为什么不直接用 Claude Code 内置工作流？** 内置的是通用的，这套针对个人项目（Android/Python/HTML）定制：自动检测技术栈、按项目追踪 session、积累 Bug 模式、深度集成 ponytail/superpowers/claude-mem 等生态。

**Q: 怎么贡献/修改？** 直接改 `<repo>/skills/<name>/SKILL.md`，PR 或 fork。纯 Markdown，无需编译。
