---
name: fix
description: Fast bug-fixing workflow. Triage -> Diagnose -> Plan -> Fix -> Review -> Ship.
             Use when user reports a bug, says "fix bug", "debug", "broken",
             "crash", "error", "bug", "不工作", "报错", "修", "崩了".
alwaysApply: false
trigger: fix, /fix, bug, fix bug, debug, broken, crash, error, 修, 修bug,
         修一下, 改bug, 报错, 崩了, 坏了, 有问题, 不工作, not working,
         regression
model_hint: standard
---

# Fix: Bug Fixing Workflow

快速修 Bug。先确认根因是否已知，再动手。

**⚠️ 每个 phase 开头先调 MCP：**
```python
steps = mcp__claude-mcp__workflow_step("<slug>", workflow="fix", phase="<phase>", context={"symptoms": [...], "files": [...]})
# MCP 失败或 10s 超时 → 读本文件文本退化为手动模式。
```

## Phase -1: Resume Check

调用 `mcp__claude-mcp__session_read("<slug>")`。

**session 存在且 `phase` 不是 `init`**：
展示当前进度（phase + checks），问用户"继续还是重头来？"

| session.phase | 跳转到 |
|---------------|--------|
| diagnose | Phase 1 |
| plan | Phase 2 |
| baseline | Phase 3 |
| fixing | Phase 4 |
| review | Phase 5 |

用户选重头走 → 正常进 Phase 0。
**session 不存在或 phase=init** → 正常进 Phase 0。

---

## Phase 0: Triage

**Step 0a: 扫 patterns.json**

**如何提取 symptoms**（从用户报错中）：
1. 异常类名 → 直接取（如 `NullPointerException`, `SlotTable`）
2. 堆栈中的函数名 → 取最后 3 个 project 内的调用
3. 报错关键词 → 取引号内字符串或英文报错原文
4. 用户描述的现象 → 取中文动词短语（如 "闪退"、"白屏"、"卡死"）

示例：用户说 "打开课表页就崩了，报 SlotTable IndexOutOfBounds" →
  symptoms: ["SlotTable", "IndexOutOfBounds", "课表页崩溃"]
  files: ["*Schedule*", "*Course*"]

调用 MCP：

```python
mcp__claude-mcp__patterns_match("<slug>", symptoms=["<报错关键词>", "<堆栈函数>"], files=["<出问题的文件>"])
```

**⚠️ MCP 调用失败（server 没配/挂了）？** 直接跳到 Phase 1 诊断，不阻塞。别报错，别重试。patterns 只是加速器，不是闸门。

返回结果按置信度排序：
- `confidence: "high"` — 症状+文件都命中 → **高置信度，可直接用已有方案**
- `confidence: "low"` — 只命中一项 → 作为提示

**高置信度（症状+文件都命中）** → 直接展示 pattern 的 root_cause + fix：
```
这个 Bug 可能和之前遇到的一样：
  模式: Compose graphicsLayer Debug/Release 不一致
  根因: graphicsLayer 在 debug build 使用不同渲染路径
  修复: 用 Modifier.alpha 代替 graphicsLayer
  出现过: 2 次
直接按这个方案修？还是走完整诊断？
```
用户确认 → 跳到 Phase 4（跳过 diagnose 和 plan）。

**低置信度（只命中症状或文件）** → 展示匹配的 pattern 作为提示，然后正常进 Phase 1。

**无匹配** → 正常进 Phase 1。

**Step 0b: 确认根因**

**已知根因？**（你知道哪行代码有问题）

→ 直接跳到 Phase 3，不需要诊断。

**不知道原因？**（只知道症状：闪退/报错/不对）

→ 进 Phase 1。

## Phase 1: Diagnose

**必须调用 `Skill` 工具执行 `diagnose` skill：**

```
Skill("diagnose")
```

内部流程：Reproduce → Minimize → Hypothesize → Instrument → Fix → Regression-test

不许猜。用日志/断点/二分法定位到具体行。

**复杂 Bug、根因有多个假设？** → 先调用 `superpowers:systematic-debugging` 走结构化调试流程（Reproduce→Minimize→Hypothesize→Instrument→Verify），同时调用 `Skill("grill-me")` 拷问每个假设，避免修错方向。

## Phase 2: Plan

**简单修复**（单文件、单函数、有明确修法）：
一句话说修法，用户确认即动手。跳过 EnterPlanMode。

**复杂修复**（多文件、API 变更、可能引发级联影响）：
`EnterPlanMode` 出修复方案：
1. 列出所有改动点和影响面
2. 设计方案（最小改动优先）
3. `ExitPlanMode` 提交审批

方案拿不准、有多个候选修法 → `Skill("grill-me")` 拷问清楚再定。

**复杂修复**：`EnterPlanMode` 方案审批通过后，**必须**调用 `Skill("grill-me")` 拷问修复方案，确认无副作用再进 Baseline。

## Phase 3: Baseline

**在改之前**，先确认项目能编译：

```bash
./gradlew assembleDebug   # Android
python -m pytest           # Python（如果有测试）
```

## Phase 4: Fix

**有测试的项目**：写复现 Bug 的测试 → 确认失败 → 最小修复 → 测试通过。

**无测试基础设施的项目**（HITA、QQ Bot 等）：
1. 手动复现 Bug，确认存在
2. 最小改动修复
3. 手动验证修复，确认无副作用
4. Commit message 写清楚复现步骤和验证方式

## Phase 5: Review `[可跳过：typo/单行修复/配置修改/文案修改]`

- 快速检查 → `Skill("simplify")`
- 过度工程检查 → `/ponytail-review`（修复代码是否引入了不必要的复杂度和抽象）
- 影响面评估（多文件改动）→ 先 `tokensave_impact` 图谱感知影响分析，再 `Skill("pensive:blast-radius")` 交叉验证
- 系统性 Bug 模式 → `Skill("code-audit")` — 排查同类问题是否在其他地方存在

## Phase 6: Ship

- `Skill("commit-commands:commit")`
- Message：`fix: <根因> -> <修复方式>`
- 安全相关或大面积修复 → `Skill("commit-commands:commit-push-pr")`

Ship 完成后提示用户 `Skill("wrap")` 收尾沉淀经验。

**新颖 Bug 提醒**：如果这次修的 Bug 根因不常见（不是 typo、不是配置错误、不是一眼能看出来的），提醒用户：

```
这个 Bug 根因不太常见，跑 Skill("wrap") 时会被提取成 pattern，
下次同类症状会自动匹配。别忘了跑。
```

## Session 追踪

每个 phase 结束时调用 MCP：

```python
mcp__claude-mcp__session_write("<slug>", workflow="fix", phase="<current>", checks={...})
```

- Phase 0 分诊决定诊断：`mcp__claude-mcp__session_write("<slug>", workflow="fix", phase="diagnose")`
- Phase 1 诊断完成：`mcp__claude-mcp__session_write("<slug>", phase="plan")`
- Phase 2 方案确定：`mcp__claude-mcp__session_write("<slug>", phase="baseline", checks={"grill_me_done": True}  # 复杂修复)`
- Phase 3 基线通过：`mcp__claude-mcp__session_write("<slug>", phase="fixing", checks={"build_passed": True})`
- Phase 4 修复完成：`mcp__claude-mcp__session_write("<slug>", phase="review")`
- Phase 5 Review 每项完成：更新对应 check
- Phase 6 Ship 后 → `mcp__claude-mcp__session_cleanup("<slug>")`

## 失败回环

- Phase 3 编译不过（改前基线就坏了）→ 先修编译问题，不进 Phase 4
- Phase 4 修完后症状没消失 → 回 Phase 1 重新诊断
- Phase 5 simplify 或 blast-radius 扫出新问题 → 回 Phase 4 修
- diagnose 定位不到根因 → `Skill("grill-me")` 拷问假设；还是不行 → `Skill("ask-teacher")`
- **同一环节回退 2 次还不行** → `Skill("ask-teacher")` 整理问题问老师，或 `Skill("handoff")` 写交接

## Exit Criteria

- [ ] 根因已定位到具体行
- [ ] 修复方案已确认（复杂修复需用户审批；简单修复自动满足）
- [ ] 编译通过
- [ ] 修复已验证（测试绿或手动验证）
- [ ] simplify 无新问题（非 typo 时）
- [ ] Commit 已创建
