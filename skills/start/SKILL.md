---
name: start
description: Initialize a development session on a project. Reads CLAUDE.md,
             checks git status, identifies pending work, and asks what to work
             on. Use when user wants to start working, says "start X project",
             "开始", "开始做", "work on", or opens Claude Code to begin a new
             session.
alwaysApply: false
trigger: start, /start, 开始, 开始做, 开工, work on, 开始开发, let's start,
         start working, 干活, 开干, new session
model_hint: standard
---

# Start: Session Initialization

**⚠️ 先调 MCP 再读文本：**
```python
steps = mcp__claude-mcp__workflow_step("<slug>", "start", "init")
# MCP 失败或 10s 超时 → 读本文件文本退化为手动模式。
```

开始一次开发会话。确定在哪个项目、做什么。

**全流程**: `start → {dev|fix|refactor} → wrap`（中间可能走 grill-me / diagnose / code-audit）

## Step 1: Locate Project

用户说了项目名（如 "start hita"），匹配：

| 关键词 | slug | 路径 |
|--------|------|------|
| datememory, dm, 倒计时 | datememory | E:\DateMemory |
| hita, hit, 课表 | hita | E:\HITA_Agent |
| qqbot, bot, qq | qqbot | E:\qqbot |
| flightcompare, fc, 机票 | flightcompare | E:\flightcompare |
| sts2, sts, 尖塔, mod | sts2 | 待补充，问用户 |

**用户没说项目** → 列出上表所有项目让用户选。
**项目不在表中** → 问用户路径，slug 按项目名小写下划线。

## Step 2: Detect Tech Stack

用 **Glob / Read** 扫项目根目录，按文件自动判断：

| 检测到文件 | 平台 | 编译命令 | 测试命令 |
|---|---|---|---|
| `build.gradle.kts` + `app/` | Android Kotlin | `./gradlew assembleDebug` | `./gradlew test` |
| `build.gradle` (无 .kts) | Android Groovy | `./gradlew assembleDebug` | `./gradlew test` |
| `requirements.txt` / `pyproject.toml` | Python | `python -m compileall .` | `python -m pytest` |
| `package.json` | Node/TS | 读 scripts.build | 读 scripts.test |
| 以上都不匹配 | 未知 | 问用户 | 问用户 |

**检查是否有测试**：找 `src/test/`、`tests/`、`__tests__/`、pytest/phpunit 配置等 → 有则 `has_tests: true`，无则 `has_tests: false`。

**推导 commit 前缀**（用于 commit message 自动选前缀）：
- Android → `feat:` / `fix:` / `perf:` / `refactor:`
- Python → 同上
- 通用的从 CLAUDE.md 找约定

**缓存 tech 结论**：写 `.claude/projects/<slug>/tech.json`：

```json
{ "platform": "Android Kotlin", "build_cmd": "./gradlew assembleDebug", "test_cmd": "./gradlew test", "has_tests": false, "detected": "<ISO timestamp>" }
```

下次 start 先读这个文件，存在且项目文件未变就跳过检测。

**检查 claude-mem**：如果 claude-mem worker 在运行（`curl -s http://localhost:37777` 可达），说明跨会话记忆已激活。当前项目的历史上下文将在后续 step 中自动注入。

## Step 3: Check Session State

调用 MCP 工具：

```
session_read("<slug>")
```

**返回数据存在且 `updated` 在 24h 内**：

```
⚠️ 发现未完成的工作流:
  工作流: fix
  所处阶段: Phase 4 (Review)
  已通过: 编译 ✓  simplify ✓
  未完成: blast-radius ✗
  开始时间: 2026-05-31 15:30
```

→ 提示用 `Skill("continue")` 精确恢复。

**超过 24h** → 忽略，算过期会话。
**文件不存在** → 新会话，跳到 Step 4。

## Step 4: Present Status

**先看有没有知识图谱**：检查 `<project_path>/graphify-out/GRAPH_REPORT.md` 是否存在。如果之前跑过 `/graphify .`，直接读这份报告——它用自然语言描述了项目架构、模块关系、关键依赖，比从头扫代码快 10 倍。

**没有图谱？** 如果是你第一次进这个项目（或项目结构大改过），在 Step 4 末尾问用户：

```
这个项目还没生成知识图谱，要不要跑 `/graphify .` 分析一下？
以后每次 start 都能秒读项目结构，token 消耗降 71 倍。（2-5 分钟）
```

用户说好 → 跑 `graphify .`，等生成完再继续展示状态。用户说跳过 → 继续。

用 **Read 工具**读 `<project_path>/CLAUDE.md` + 图谱报告（如有）。

用 `git -C "<project_path>"` 读 git 状态：

```bash
git -C "<project_path>" log --oneline -5
git -C "<project_path>" status
```

**有待提交的变更？有 stash？** → 输出警告：

```
⚠️ 发现未完成的工作:
- N 个文件已修改
- 分支 feat/xxx 比 main 多 N 个 commit
```

汇总：

```
## <项目名> — 当前状态

**平台**: Android Kotlin（has_tests: false）
**分支**: main (clean)
**最后提交**: fix: xxx (2 小时前)

**可选任务**:
1. [ ] <来自 CLAUDE.md / memory 的待办>
2. [ ] <自己的新想法>

**最近开发活动**:
- <最近 commit 摘要>
```

## Step 5: Route

问用户："做什么？"

确认后路由：

- 新功能 → `Skill("dev")`
- 修 Bug → `Skill("fix")`
- 优化/重构 → `Skill("refactor")`
- 扫描已有 Bug → `Skill("code-audit")`
- 拆成 Issue 分步做 → `Skill("to-issues")`

路由前，初始化 session：

```
session_write("<slug>",
  workflow="fix",       # 先设一个，后续 workflow skill 会覆盖
  phase="init",
  project_path="<path>",
  platform="<detected>",
  has_tests=false,
  branch="<branch>"
)
```

## Exit Criteria

- [ ] 项目已定位，tech stack 已检测
- [ ] Session 状态已检查
- [ ] CLAUDE.md 已读，Git 状态已知
- [ ] 未完成工作已提示（如果有）
- [ ] 用户已选定目标
- [ ] session.json 已初始化
- [ ] 对应 skill 已触发
