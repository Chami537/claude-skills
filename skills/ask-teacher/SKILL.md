---
name: ask-teacher
description: Anti-stuck mechanism. When the agent is going in circles, hitting the same error repeatedly, or stuck on a design choice with no clear answer, STOP and output a precise problem description the user can copy-paste to their teacher. Use when user says "问老师", "问一下老师", "卡住了问老师", or when the agent has tried the same approach 2+ times without success.
alwaysApply: false
trigger: 问老师, 问一下老师, 卡住了问老师, 帮我问老师, 请教老师, ask teacher, stuck ask teacher
---

# Ask Teacher: 卡住时的精准提问

## 什么时候用

- 同一个方向试了 2 次还不行（dev/fix/refactor 的失败回环已经触发过）
- 多个方案选不定，各有利弊
- 报错/行为完全无法解释，怀疑是环境或平台 bug
- 用户主动说 "问老师"

## 流程

### Step 1: 停下来

**不许再试**。不要再跑编译、不要再改代码、不要再猜。当前状态冻结。

### Step 2: 描述问题

用以下结构精准描述，不超过一屏（方便老师快速看完）：

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

### Step 3: 输出给用户

把上面的内容渲染成一段紧凑文本。用户复制粘贴发给老师。

### Step 4: 等老师回复

老师回复后，按老师的方案尝试。如果老师给多个方向，先试第一个。

## 规则

- **不许美化问题**：不要说"可能是个小问题"、"应该很好解决"——精准描述，不预判
- **附代码要精**：贴文件路径+行号+关键 3-5 行，不是整个文件
- **试过的方案诚实写**：包括看起来蠢的方案。别让老师重复建议
- **一个 skill 调用 = 一个问题**：如果同时卡在多个不相关的地方，分次问
