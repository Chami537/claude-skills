# Chami's Claude Code Workflows

自用 Claude Code 工作流技能集 + 配套 MCP Server。**已集成 ponytail / superpowers / ui-ux-pro-max / deep-research / claude-mem / graphify / agent-reach / tokensave / headroom 等生态插件。**

## Quick Links

| Tool | GitHub | Install |
|------|--------|---------|
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

## One-Click Install

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

## Usage Flow

```
/start          -> init session, detect project
                    ├── check claude-mem cross-session memory
                    └── check graphify knowledge graph
/dev            -> new feature (Plan -> Build -> Review -> Harden -> Ship)
    ├── Plan   -> ponytail-audit -> research-deep + agent-reach
    │           -> tokensave_context -> EnterPlanMode
    ├── Build  -> ui-ux-pro-max + parallel-agents + ponytail 6-step
    ├── Review -> ponytail-review + tokensave_impact + blast-radius + code-audit
    └── stuck? -> /ask-teacher
/fix            -> bug fix (Triage -> Diagnose -> Plan -> Fix -> Review -> Ship)
    ├── Diagnose -> systematic-debugging + grill-me
    └── Review  -> ponytail-review + tokensave_impact + blast-radius
/refactor       -> refactor (Measure -> Plan -> TDD -> Review -> Ship)
    ├── Measure -> ponytail-audit + tokensave_context
    └── Review  -> ponytail-review + ui-ux-pro-max UX
/code-audit     -> project bug scan
    ├── Intel  -> patterns.json + ponytail-debt + memory
    └── Scan   -> ponytail-audit + general checklist
/wrap           -> retro
    ├── ponytail-gain (savings scoreboard)
    └── headroom_compress (context compression)
/continue       -> resume from last session
    ├── session.json -> phase recovery
    └── claude-mem -> operation history
```

## Embed Matrix

| Skill | ponytail | superpowers | ui-ux-pro | deep-research | claude-mem | graphify | agent-reach | tokensave | headroom |
|-------|----------|-------------|-----------|---------------|------------|----------|-------------|-----------|----------|
| **dev** | audit+review+6step | parallel-agents | UI inject | tech research | - | - | ext search | context+impact | - |
| **fix** | review | systematic-debugging | - | - | - | - | - | impact | - |
| **refactor** | audit+review | - | UX check | - | - | - | - | context | - |
| **code-audit** | debt+audit | - | - | - | - | - | - | - | - |
| **start** | - | - | - | - | status | graph report | - | - | - |
| **continue** | - | - | - | - | history | - | - | - | - |
| **wrap** | gain | - | - | - | - | - | - | - | compress |

## Skill List

| Skill | Purpose | Integrated |
|-------|---------|------------|
| `start` | Init session, detect tech stack | claude-mem + graphify |
| `dev` | New feature: Plan->Build->Review->Harden->Ship | ponytail + research-deep + agent-reach + tokensave + ui-ux-pro-max + parallel-agents |
| `fix` | Bug fix: Triage->Diagnose->Plan->Fix->Review->Ship | systematic-debugging + ponytail-review + tokensave_impact |
| `refactor` | Refactor: Measure->Plan->TDD->Review->Ship | ponytail-audit + tokensave_context + ponytail-review + ui-ux-pro-max UX |
| `wrap` | Retro: summary, lessons, progress | ponytail-gain + headroom_compress |
| `code-audit` | Project bug scan, root cause analysis | ponytail-debt + ponytail-audit |
| `ask-teacher` | Format stuck problems for external help | - |
| `continue` | Recover context from previous session | claude-mem history |

## MCP Tracking

- `session_read/write/cleanup` -- Session state (24h recovery)
- `checklist_read/append` -- Verification checklist
- `patterns_list/match/append` -- Bug pattern matching
- `tokensave_context` -- Code graph context
- `tokensave_impact` -- Graph-aware blast radius
- `headroom_compress` -- Context compression
- `claude-mem` -- Cross-session memory

## FAQ

**Q: All plugins required?** No. Failures are gracefully skipped. But without ponytail you lose over-engineering detection, without claude-mem cross-session memory fails, without MCP Server session/checklist/patterns tracking disabled.

**Q: How to contribute?** Edit `<repo>/skills/<name>/SKILL.md`, PR or fork. All Markdown, no compilation.
