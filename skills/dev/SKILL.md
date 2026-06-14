---
name: dev
description: New feature development with full workflow. Plan -> Build(TDD)
             -> Review -> Harden -> Ship. Use when user says "add feature",
             "implement", "new feature", "开发", "新功能", "加个", "做一个",
             or describes building something new.
alwaysApply: false
trigger: dev, /dev, new feature, add feature, implement, 开发, 新功能, 加个,
         做一个, 实现, 新增, feature request, build
model_hint: opus
---

# Dev: New Feature Workflow

先确定规模，再按对应深度走。

## Phase -1: Resume Check

调用 `session_read("<slug>")`。

**session 存在且 `phase` 不是 `init`**：
展示当前进度（phase + checks），问用户"继续从 Phase X 开始？还是重头走？"

| session.phase | 跳转到 |
|---------------|--------|
| plan | Phase 1（保留已有方案）|
| build | Phase 2 |
| verify | Phase 3 |
| review | Phase 4 |
| harden | Phase 5 |
| ship | Phase 6（问用户是否重做 Ship）|

用户选重头走 → 正常进 Phase 0。
**session 不存在或 phase=init** → 正常进 Phase 0。

---

## Phase 0: Size Triage

| 规模 | 特征 | 流程深度 |
|------|------|---------|
| **S** | 单文件 **且** <50 行 **且** 无新依赖 | Plan(口头) → Build → Verify → Ship |
| **M** | 多文件、涉及数据层/UI | Plan → Build → Review → Verify → Ship |
| **L** | 新模块、架构变更、API 设计 | 完整流程：Plan → Build → Review → Harden → Ship |

不确定就往上取。需求本身模糊、不知道怎么拆？→ `Skill("grill-me")` 先把需求拷问清楚再动手。

## Phase 1: Plan & Design

**S 规模**：一句话说改法，用户确认即动手。跳过 EnterPlanMode。
但跨 3 文件以上的改动（即使每处很小），建议走 EnterPlanMode 对齐方案，避免改完方向不一致。

**M / L 规模**：`EnterPlanMode` 出完整方案：
1. 用 `Agent (Explore)` 理解现有代码
2. 设计架构，列出要改动/新建的文件
3. `ExitPlanMode` 提交审批

架构取舍多 → `Skill("grill-me")`。需要原型 → `Skill("prototype")`。

**L 规模**：`EnterPlanMode` 方案审批通过后，**必须**调用 `Skill("grill-me")` 拷问设计，确认无遗漏再进 Build。

**检查 patterns.json**：调用 `patterns_list("<slug>")`，找出 `files` glob 匹配本次改动文件的 pattern。展示给用户：

```
⚠️ 这些文件有已知坑点：
  - Theme.kt: graphicsLayer Debug/Release 不一致（出现过 2 次）
  - Animation.kt: return@Column 导致 SlotTable 越界（出现过 1 次）
```

用户确认已知风险后再动手。

## Phase 2: Build

**有测试的项目**：RED（写测试→失败）→ GREEN（实现→通过）→ REFACTOR（清理）

**无测试基础设施的项目**（HITA、QQ Bot 等）：
1. 逐个文件改动
2. 每改完一个逻辑块，记下验证步骤（commit message 用 `验证:` 标注）
3. 手动验证通过，确认无副作用
4. Commit message 写清：验证步骤 + 验证结果

需要大规模调研时用 `Agent (Explore)`。

## Phase 3: Verify

**有测试的项目**：跑测试，确认全绿。

```bash
./gradlew assembleDebug   # Android
python -m pytest           # Python
```

**无测试的项目**：
1. 编译确认
2. 调用 `checklist_read("<slug>")`，跑相关模块的已有验证步骤
3. 跑 Phase 2 记下的新验证步骤

编译不过不进 Review。

## Phase 4: Review `[S 规模可跳过]`

- 正式审查 → `Skill("pensive:unified-review")`
- 快速检查 → `Skill("simplify")`
- 影响面评估 → `Skill("pensive:blast-radius")`
- Bug 自查（M/L 建议跑）→ `Skill("code-audit")` — 扫出新问题可选跳 `Skill("fix")`

## Phase 5: Harden `[L 规模，或涉及认证/支付/权限/敏感数据]`

- 安全敏感代码 → `Skill("pensive:harden")`
- 性能关键路径 → `Skill("pensive:performance-review")`
- 死代码/无用依赖 → `Skill("conserve:unbloat")`

## Phase 6: Ship

- M/L 规模 → `Skill("commit-commands:commit-push-pr")`
- S 规模 → `Skill("commit-commands:commit")`
- 合并后 → `Skill("commit-commands:clean_gone")`
- L 规模，多人协作 → 考虑 `Skill("to-issues")` 拆 Issue 追踪

Ship 完成后提示用户 `Skill("wrap")` 收尾沉淀经验。

## Session 追踪

每个 phase 结束时调用 MCP：

```python
session_write("<slug>", workflow="dev", phase="<current>", checks={...})
```

- Phase 0 确定规模后：`session_write("<slug>", workflow="dev", phase="plan", scale="M")`
- Phase 1 方案审批通过：`session_write("<slug>", phase="build", checks={"grill_me_done": True}  # L 规模)`
- Phase 3 编译通过：`session_write("<slug>", phase="verify", checks={"build_passed": True})`
- Phase 4 Review 完成：`session_write("<slug>", phase="review", checks={"simplify_done": True, ...})`
- Phase 5 Harden 完成：`session_write("<slug>", phase="harden")`
- Phase 6 Ship 后 → `session_cleanup("<slug>")`

## 失败回环

- Phase 3 编译不过 → 回 Phase 2 修，不硬进 Review
- Phase 4 Review 扫出新问题 → 回 Phase 2 修完后重新走 Phase 3 → Phase 4
- EnterPlanMode 用户驳回方案 → 回 Phase 1 改方案，重新提交
- **同一环节回退 2 次还不行** → `Skill("ask-teacher")` 整理问题问老师，或 `Skill("handoff")` 写交接，不硬撑

## Exit Criteria

- [ ] 方案已审批（M/L 规模）
- [ ] 编译通过
- [ ] Review 通过（M/L 规模）
- [ ] Commit/PR 已创建
