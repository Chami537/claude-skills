---
name: continue
description: Recover development context from last session. Reads git log +
             project memory + CLAUDE.md to rebuild context in seconds. Use
             when starting a new session on an existing project, user says
             "continue", "继续", "接着做", "上次做到哪", "go on", or opens
             a project after a break.
alwaysApply: false
trigger: continue, /continue, 继续, 接着, 接着做, 上次, 上次做到哪, 继续开发,
         接着开发, go on, resume, pick up, where were we, 上次的, 进度,
         what's the status
model_hint: standard
---

# Continue: Cross-Session Context Recovery

新会话打开项目时，秒级重建上下文。不靠记忆，靠 git 和 CLAUDE.md。

## Step 1: Locate Project

1. 从 conversation context 读取上次 git -C 的目标路径
2. 读 `.claude/projects/` 下所有 `*/session.json`，取最近更新的 `project_path`
3. 以上都没有 → 列出已配置项目表（同 start）让用户选

## Step 2: Read Session State

调用 MCP：

```
session_read("<slug>")
```

返回精确的工作流状态。用 `workflow` + `phase` + `checks` 定位中断点。
**返回 `_expired: true` 或空 `{}`** → 退化为纯 git 恢复，跳到 Step 4。

## Step 3: Read Project Config

先读项目根目录的 `CLAUDE.md`。

如果没有，提示用户创建（直接建一个 `CLAUDE.md` 文件，写项目名和技术栈即可）。

## Step 3b: Read Tech Config

读 `.claude/projects/<slug>/tech.json`（start 的缓存产物）。存在则直接用，跳过平台检测。
不存在则用 start 的 Step 2 逻辑检测。

## Step 4: Read Git History

项目路径优先从上下文推断（最近 git 操作的目标目录），推断不出就问用户。

```bash
git -C "<project_path>" log --oneline -5
git -C "<project_path>" log -1 --format="%H %s %ai"
git -C "<project_path>" status
git -C "<project_path>" stash list
```

## Step 5: Rebuild Context

**从 session.json 取精确状态**（如有）：

```
workflow: fix
phase: review
checks: { build_passed: true, simplify_done: true, blast_radius_done: false }
```

**从 git 推断开发主题**（如无 session）：

1. 读最近 3 条 commit subject，提取共同主题（例如连续 3 条 `feat: 暗黑模式` → 在做暗黑模式）
2. 看分支名（`feat/dark-theme` → 在做暗黑模式）
3. 看 dirty files 路径（`src/theme/` 下改了 3 个文件 → 在做主题相关）
4. 有 stash → 说明中断时有做了一半的改动，列出 stash message

两者合并，填入模板：

```
## 上下文恢复: <项目名>

<有 session 时>
**工作流**: fix — Phase 4 (Review)
**已完成**: 编译 ✓ | simplify ✓
**待完成**: blast-radius ✗ | ship ✗

**当前分支**: <branch>
**上次提交**: <hash> — <message> (<date>)
**工作区**: clean / N files modified / stash 中有 M 项

**上次在做**:
<有 session: 从 phase 精确描述>
<无 session: 从 git 4 信号推断>

**验证清单**:
<如果 has_tests=false: 读 .claude/projects/<slug>/checklist.md，列出相关验证步骤>

**下一步建议**:
<有 session: 继续未完成的 phase>
<无 session: 基于 git 推断>
```

## Step 6: Confirm & Route

问用户："是这个状态吗？接下来做什么？"

不要假设用户的意图。上下文恢复的目的是对齐，不是替用户决定。

确认后路由到对应 skill：
- 新功能 → `Skill("dev")`
- 修 Bug → `Skill("fix")`
- 优化/重构 → `Skill("refactor")`
- 扫描已有 Bug → `Skill("code-audit")`
- 拆成 Issue 分步做 → `Skill("to-issues")`

## Exit Criteria

- [ ] session.json 已读（如有）
- [ ] CLAUDE.md 已读（或已提示创建）
- [ ] Git 状态已读取
- [ ] 上下文摘要已输出（含 session 状态 + git 推断）
- [ ] 用户确认了下一步
- [ ] 对应 skill 已触发（由 workflow skill 自身的 Resume Check 跳转 phase）
