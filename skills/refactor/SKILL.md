---
name: refactor
description: Refactoring and optimization workflow. Measure first, then
             plan -> TDD -> review -> harden -> ship. Use when user says
             "optimize", "refactor", "improve", "speed up", "clean up",
             "优化", "重构", "整理", "加速", "性能".
alwaysApply: false
trigger: refactor, /refactor, optimize, optimization, improve, speed up,
         clean up, 优化, 重构, 整理, 加速, 性能, 改进, perf, performance,
         code quality
model_hint: opus
---

# Refactor: Optimization & Refactoring Workflow

改之前先量，改之后验证改善。

**⚠️ 每个 phase 开头先调 MCP，返回的步骤列表是权威指令：**
```python
steps = mcp__claude-mcp__workflow_step("<slug>", workflow="refactor", phase="<phase>", context={"task": "<描述>"})
# 返回 {"steps": [...], "total": N}。逐项执行。
# MCP 失败或 10 秒超时 → 读本文件文本描述退化为手动模式。
```

## Phase 0: Resume Check

调用 `mcp__claude-mcp__session_read("<slug>")`。

**session 存在且 `phase` 不是 `init`**：
展示当前进度（含 baseline 指标），问用户"继续还是重头来？"

| session.phase | 跳转到 |
|---------------|--------|
| measure | Phase 1（但跳过再次测量，直接用已有 baseline）|
| plan | Phase 2 |
| build | Phase 3 |
| verify | Phase 4 |
| review | Phase 5 |
| ship | Phase 6 |

用户选重头走 → 正常进 Phase 1。
**session 不存在** → 先初始化：`mcp__claude-mcp__session_write("<slug>", workflow="refactor", phase="init")`，再进 Phase 1。
**phase=init** → 正常进 Phase 1。

---

## Phase 1: Measure & Assess

**先跑 ponytail 审计**：`/ponytail-audit` — 全仓库扫描过度工程，输出一份按优先级排序的"该删什么/该简化什么"清单。这份清单直接作为 refactor 目标的输入。

**同时用代码图谱快速理解目标区域**：

   **📊 先检查离线图谱**：`ls <project_path>/graphify-out/`，存在则优先读 `GRAPH_REPORT.md` + `/graphify query <问题>`。graphify 全项目覆盖，不入 token 预算。

   **🔍 在线图谱回退链**（无 graphify-out 时，依次尝试）：
   ① `tokensave_context` → ② `tokensave_search` → ③ `tokensave_dependencies` → ④ `tokensave_similar` → ⑤ `Agent(Explore)` 兜底。**禁止跳回手动 Read + Grep。**

**然后按需补量**，别全跑：

| 场景 | 用这个 |
|------|--------|
| 过度工程/冗余（ponytail 已覆盖） | `/ponytail-audit` 结果直接跳 Phase 2 规划拆除 |
| 性能/卡顿 | `Skill("pensive:performance-review")` |
| 代码腐化/重复 | `Skill("pensive:code-refinement")` |
| 死代码太多 | `Skill("conserve:unbloat")` |
| 可读性/重命名/提取函数 | 直接量：读代码确认无副作用即可 |
| 架构调整 | `Skill("pensive:architecture-reviewer")` |

明确输出：**改前指标是什么？目标是什么？**

## Phase 2: Plan

- 范围大（>3 文件、架构级）→ `EnterPlanMode`，方案审批通过后**必须**调用 `Skill("grill-me")` 拷问设计
- 范围小（单文件/单函数）→ 一句话说改法，用户确认即动手
- 方案拿不准、架构取舍多 → `Skill("grill-me")` 拷问到确定为止

## Phase 3: Build

**有测试的项目**：保持现有测试绿 → 改代码 → 再次确认测试绿。

**无测试基础设施的项目**（HITA、QQ Bot 等）：
1. 改动前记下验证方法（例如："打开课表页，确认学期切换正常"）
2. 改代码
3. 改动后手动验证
4. Commit message 写清：验证步骤 + 验证结果

## Phase 4: Verify

**有测试的项目**：跑现有测试，确认全绿后再进 Review。

```
./gradlew assembleDebug && ./gradlew test   # Android
python -m pytest                              # Python
```

**无测试的项目**：
1. 编译确认
2. 调用 `mcp__claude-mcp__checklist_read("<slug>")`，跑相关模块的已有验证步骤
3. 按 Phase 3 记下的验证方法手动测试
4. 确认改后行为正确、无副作用

编译不过的优化等于没做。

## Phase 5: Review

**回归检查**：对比 Phase 1 baseline，确认：
- 功能行为无退化（手动验证 / 现有测试绿）
- 指标有改善（对比改前数据）

- 影响面分析 → `Skill("pensive:blast-radius")`

- 代码审查 → `Skill("simplify")`
- 过度工程回访 → `/ponytail-review`（确认这次改完后没有留下新的过度工程）
- **涉及 UI 组件改动** → 跑 `ui-ux-pro-max` 的 UX 指南对照，确认没有引入视觉退化或交互不一致
- 大范围重构 → `Skill("pensive:unified-review")`（多维度全面审查）
- **验证改后指标** — 对比 Phase 1，有没有改善？

## Phase 6: Ship

`Skill("commit-commands:commit")`

```
perf: <改了什么>（<指标>：改前 X → 改后 Y）
refactor: <提取了什么>（-N 行重复代码）
```

Ship 完成后提示用户 `Skill("wrap")` 收尾沉淀经验。

## Session 追踪

每个 phase 结束时调用 MCP：

```python
mcp__claude-mcp__session_write("<slug>", workflow="refactor", phase="<current>", checks={...})
```

- Phase 1 测量完成：`mcp__claude-mcp__session_write("<slug>", workflow="refactor", phase="measure", baseline={...})`
- Phase 2 方案确定：`mcp__claude-mcp__session_write("<slug>", phase="plan", checks={"grill_me_done": True}  # 范围大时)`
- Phase 3 进入构建：`mcp__claude-mcp__session_write("<slug>", phase="build")`
- Phase 4 编译通过：`mcp__claude-mcp__session_write("<slug>", phase="verify", checks={"build_passed": True})`
- Phase 5 Review 完成：`mcp__claude-mcp__session_write("<slug>", phase="review", checks={...})`
- Phase 6 Ship 后 → `mcp__claude-mcp__session_cleanup("<slug>")`

## 失败回环

- Phase 4 编译不过 → 回 Phase 3 修
- Phase 5 指标没改善（甚至变差）→ 回 Phase 2 重新设计方案
- Phase 5 多指标冲突（A 改善 B 变差）→ 展示数据给用户判断，不自己做取舍
- Phase 5 Review 扫出新问题 → 回 Phase 3 修
- **同一环节回退 2 次还不行** → `Skill("ask-teacher")` 整理问题问老师，或 `Skill("handoff")` 写交接

## Exit Criteria

- [ ] Phase 1 指标已记录（改前基准）
- [ ] 编译通过
- [ ] Phase 5 Review 已完成（blast-radius + simplify）
- [ ] Phase 5 验证改后指标有改善
- [ ] Commit message 包含数据对比
