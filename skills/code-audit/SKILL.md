---
name: code-audit
description: 项目级 bug 自查。扫描代码中的潜在 bug，分析根因，给出修复方案，可选调用 fix 执行修复。Use when user says "查bug", "自查", "audit", "扫描问题", "代码审查", or wants to find bugs in their project.
---

# Code Audit — 项目 Bug 自查

**⚠️ 先调 MCP 再读文本：**
```python
steps = mcp__claude-mcp__workflow_step("<slug>", workflow="code-audit", phase="init")
# MCP 失败或 10s 超时 → 读本文件文本退化为手动模式。
```

## 快速开始

用户说 "查bug" / "audit" 即触发。

## 工作流

### Step 1: 收集中情报

四件事 + 一项 ponytail 检查：

1. **读项目 CLAUDE.md** — 读 `<project_path>/CLAUDE.md`
2. **读 patterns** — 调用 `mcp__claude-mcp__patterns_list("<slug>")`。对每个 pattern：
   
   **用 symptoms 关键词 grep 全项目**：
   ```bash
   git -C "<project_path>" grep -n "<symptom关键词>" -- "*.kt" "*.py" "*.java"
   ```
   命中的文件 = 可能存在同类问题。

   **用 files glob 定位范围**（Glob 工具）。

   **count >= 2 的 pattern 优先级最高**（反复出现 → 几乎一定有同类问题藏匿）。
3. **读 Memory** — 读 `~/.claude/projects/C--Users-Rinat/memory/MEMORY.md`，找到匹配项目的 `project_*.md` 和 `feedback_*.md`，逐个用 Read 读。**文件不存在就跳过**——新项目没有 memory 很正常，别卡在这一步。
4. **读 REFERENCE** — 读本 skill 同级 `REFERENCE.md`，获取项目专属陷阱的静态备份
5. **扫描 ponytail 技术债** — 跑 `/ponytail-debt`，把代码中所有 `ponytail:` 注释汇集成债台账。这些是开发者自己知道有坑但暂时绕开的地方，直接作为 audit 关注点

### Step 2: 确定范围

```
扫描范围？
1. 全项目
2. 指定模块/目录（请说明）
3. 只看最近改动（git diff）
```

### Step 3: 执行扫描

**优先查项目专属陷阱（patterns.json > CLAUDE.md + memory + REFERENCE），再查通用底线。**

用 Grep/Glob 定位可疑模式，Read 确认是否真 bug。**只看不改**。

**新增：同时跑 `/ponytail-audit`** — 全仓库扫描过度工程（重复实现的标准库、不必要的依赖、投机性抽象、死弹性）。结果并入最终报告。

### Step 4: 输出报告

```
[严重级别] 文件:行号 — 问题简述
根因: xxx
影响: xxx
修复方案: xxx
来源: patterns.json / CLAUDE.md / wrap-memory / 通用清单
```

按严重级别排序，统计汇总。

**严重级别定义**：

| 级别 | 标准 | 示例 |
|------|------|------|
| **CRITICAL** | 必崩/数据丢失/安全漏洞 | NPE 无保护、SQL 注入、未加密敏感数据 |
| **HIGH** | 特定条件下必现的 Bug | 状态不一致、内存泄漏、并发竞态 |
| **MEDIUM** | 潜在风险，条件苛刻 | 废弃 API 使用、性能退化、边界条件遗漏 |
| **LOW** | 代码味道，不影响运行 | 命名不规范、重复代码、可简化逻辑 |

不确定就标 MEDIUM，不拔高。

### Step 5: 修复

用户确认后逐项修复：

- **同根因、多文件**（例如 pattern 扫出 5 处同类问题）→ 一次修完，一个 commit
- **不同根因** → 逐项调 `Skill("fix")`，每项独立 commit
- 每项修完验证编译

## 重要规则

- **先查后修**：扫描阶段只看不改
- **经验优先**：patterns.json (count>=2) > memory 反馈 > CLAUDE.md 陷阱 > REFERENCE 静态备份 > 通用底线
- **可追溯**：每项标注来源
- **不确定就标 MEDIUM**：不拔高严重级别
