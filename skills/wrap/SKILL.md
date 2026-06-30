---
name: wrap
description: Post-development retro. Summarize what was done, capture lessons
             learned, update project progress. Use when user says "wrap up",
             "总结", "回顾", "复盘", "wrap", "retro", "retrospective", or at
             the end of a dev/fix/refactor session.
alwaysApply: false
trigger: wrap, /wrap, 总结, 回顾, 复盘, retro, retrospective, wrap up, 收尾,
         总结一下, 做个总结, done, 搞完了
model_hint: standard
---

# Wrap: Post-Development Retro

每次开发收尾做三件事：回顾变更、提炼经验、更新进度。

## Step 1: Summarize What Was Done

先确定项目路径。优先从 conversation 上下文中推断（最近 git 操作的目标目录），推断不出就问用户。

```bash
git -C "<project_path>" log --oneline -5
git -C "<project_path>" diff HEAD~1 --stat
```

多 commit 时用 `git diff main..HEAD --stat` 代替 `HEAD~1`。

**附带跑 `/ponytail-gain`**：展示 ponytail 基准指标（代码量/成本/速度节省中位数），一次性记分板，不放常驻模式。

**检查工作流健康**：调用 `workflow_health(slug)`。汇总本次会话中所有降级事件（fallbacks）和规则拦截（blocks），输出到 wrap 总结里。用户看到这些就知道哪里踩坑了。

**压缩上下文再保存**：调用 `headroom_compress` 把当前会话的关键上下文压缩精简，确保 wrap 输出的经验不会随 context 膨胀而丢失。

输出：

```
## 本次开发总结

**项目**: <project name>
**类型**: bug修复 / 新功能 / 重构优化

**变更文件**:
- file1.kt — 改了什么
- file2.kt — 改了什么

**做了什么**:
一句话概括核心改动 + 为什么这样改。
```

只读 git，不翻代码。读 `git log -1 --format="%B"` 取完整 commit body 就够了——Step 1 和 Step 2 共用同一次读取。

### 更新验证清单

从 commit message body 提取手动验证步骤（格式 `验证:` 或 `Verify:` 或 `- [ ]` 开头的行），逐个调用：

```python
checklist_append("<slug>", module="<模块/页面>", step="<验证步骤>", source="<commit hash>")
```

MCP 自动去重（同文本不重复加）、自动分模块段落。

## Step 2: Capture Lessons

**自己从 git diff 里提炼经验**，不要让用户想。

1. 直接用 Step 1 的 `git log` 输出 + 读 `git diff HEAD~1 --stat` 看改动范围（多 commit 用 `git diff main..HEAD --stat`）
2. 从改动中识别模式：
   - 因为不知道某个 API 行为而踩坑？→ 记录
   - 改了 A 结果 B 炸了（耦合）？→ 记录
   - 反复改了好几版才稳定的代码？→ 记录
   - 这次用了一个新技巧/pattern？→ 记录
3. 提炼成一条 `feedback` memory，用 `AskUserQuestion` 确认：

```
问："我从这次改动里提炼了这条经验，你看对不对：<一句话经验>"
选项：对，存 / 不对，我补充 / 没什么可记的，跳过
```

**格式**：

```
---
name: <project>-<topic>-lesson
description: Lesson from <project> on <date>
type: feedback
---

<一句话经验>
**Why:** <从 diff 里看到的根因>
**How to apply:** <适用场景>
```

如果改动太简单（typo、改文案、单行配置），跳过，不存。

### 联动 code-audit

存完经验后，如果经验和 bug 排查相关，问：

**"这个经验要不要加入 code-audit 的检查清单？以后查bug会自动扫这个。"**

如果要 → 追加到 `code-audit/REFERENCE.md` 对应项目段落。

### 联动 patterns.json

经验如果是**可复现的 bug 模式**，调用 MCP：

```python
patterns_append("<slug>",
  id="<project>-<short-slug>",
  pattern="<一句话：问题现象 + 修复方式>",
  symptoms=["<报错关键词>", "<堆栈函数名>", "<现象描述>"],
  files=["<glob>", "<具体文件路径>"],
  root_cause="<根因一句话>",
  fix="<修复方法一句话>"
)
```

MCP 自动处理：同 id → count+1；新 symptoms 合并不重复。

向用户确认前，先把 pattern 草稿展示出来：
```
从这个 Bug 提炼的模式：
  现象: graphicsLayer 在 Debug/Release 行为不一致
  症状关键词: ["动画撕裂", "graphicsLayer", "Debug/Release"]
  影响文件: ["*.kt using Modifier.graphicsLayer"]
  根因: graphicsLayer 在 debug build 使用不同渲染路径
  修复: 用 Modifier.alpha 代替 graphicsLayer
存到 patterns.json？
```
选项：存 / 不存，这经验太一次性了

## Step 3: Update Progress

问用户：**"当前完成状态？"**

选项：
- 已完成，可以合并
- 核心完成，缺测试/文档
- 部分完成，下一步是 X
- 遇到阻塞，卡在 Y

后三种 → 更新对应项目的 `project` memory。**同时检查项目 `CLAUDE.md`**，如果进度段过时了，同步更新。

### 收尾清理

- `session_cleanup("<slug>")` — 删除 session（工作流已完成）
- 已合并的分支 → `Skill("commit-commands:clean_gone")` 清理本地 [gone] 分支
- 部分完成且有明确下一步 → `Skill("to-issues")` 把剩余工作拆成 Issue

## Exit Criteria

- [ ] Git 变更已总结
- [ ] 经验已记录到 memory（或用户跳过）
- [ ] code-audit REFERENCE 已同步（如果相关）
- [ ] 项目进度 memory 已更新（或已完成无需更新）
