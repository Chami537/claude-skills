---
name: ask-teacher
description: "Anti-stuck mechanism. Auto-triggered by MCP retry_limit_2 rule. Also manual: user says 问老师."
alwaysApply: false
trigger: 问老师, 问一下老师, 卡住了问老师, 帮我问老师, 请教老师, ask teacher, stuck ask teacher
---

# Ask Teacher: 卡住时的精准提问

**触发**: MCP 硬约束 `retry_limit_2` 自动触发，或用户手动说"问老师"。

## 流程

### Step 1: 停下来

**不许再试**。不要再跑编译、不要再改代码、不要再猜。当前状态冻结。

### Step 2: 输出精准问题描述

```
【要做什么】
一句话：目标是什么

【现在卡在哪】
- 现象：具体报错/行为（贴关键日志/错误信息，不贴全文）
- 试过什么：A → 结果X（不行），B → 结果Y（不行）
- 相关代码：<文件路径>:<行号> — 只贴最相关的 3-5 行

【我怀疑是】
- 猜测1: xxx（因为 yyy）
- 猜测2: xxx（因为 yyy）

【项目上下文】
平台: Android Kotlin / Python / etc.
相关依赖/版本: 如果有
```

### Step 3: 等老师回复

老师回复后，按老师的方案尝试。如果老师给多个方向，先试第一个。

## 规则

- **不许美化问题**：不预判"应该很好解决"
- **附代码要精**：文件路径+行号+关键 3-5 行，不是整个文件
- **试过的方案诚实写**：包括看起来蠢的方案
- **一个 skill 调用 = 一个问题**：多个不相关的问题分次问
