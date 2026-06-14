# Refactor Examples

## Example 1: Optimize DateMemory image loading

User: `/refactor DateMemory 详情页切换时图片加载有卡顿`

Workflow:

1. **Measure** — `pensive:performance-review` 扫描 `DetailScreen.kt`。发现：每次 VerticalPager 翻页都重新 decode 全分辨率图片。指标：翻页耗时 ~800ms，目标 <200ms。

2. **Plan** — 方案：加图片内存缓存（Coil 自带的 memoryCachePolicy）+ 预加载相邻页。用户确认。

3. **Build (TDD)** — 现有测试保持绿。加 `DetailScreenTest` 验证缓存命中。实现 Coil 缓存配置 + `preload`。

4. **Review** — `pensive:blast-radius` 检查缓存影响面。验证指标：翻页 ~150ms。

5. **Harden** — 缓存大小限制，防止 OOM。

6. **Ship** — commit: `perf: add image memory cache for detail screen pager (fling: 800ms -> 150ms)`

## Example 2: Extract duplicate card layout

User: `/refactor NormalEventCard 和 PinnedEventCard 有很多重复布局，提取公共组件`

1. **Measure** — `pensive:code-refinement` 分析：两个 Card 共享 60% 布局代码（标题、日期、封面图）。重复行数 ~80 行。

2. **Plan** — 小范围，直接说方案：提取 `EventCardBase` composable，两个 Card 各自传入差异化 slot。

3. **Build** — 现有 UI 测试保持绿。创建 `EventCardBase`，改造两个 Card。重构全程测试绿。

4. **Review** — `/simplify` 确认无新重复。

5. **Ship** — commit: `refactor: extract EventCardBase from NormalEventCard and PinnedEventCard (-80 dup lines)`
