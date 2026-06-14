# Dev Examples

## Example 1: Add lunar calendar display to DateMemory

User: `/dev DateMemory 加上农历日期显示，DateEvent 里 isLunar 字段一直没用到`

Workflow:

1. **Plan** — EnterPlanMode，读 `DateEvent.kt`(isLunar 字段)、`DetailScreen.kt`(日期展示逻辑)、`TimeUtils.kt`(时间工具)。方案：在 DetailScreen 的日期文字旁加农历日期行，New 一个 `LunarUtils.kt` 做公历→农历转换。用户审批通过。

2. **Build (TDD)** — 先写 `LunarUtilsTest.kt`，测试已知日期的农历输出。RED → 实现 `LunarUtils` → GREEN → 在 `DetailScreen` 中接入 → REFACTOR 清理。

3. **Review** — `/simplify` 检查重复代码。`pensive:blast-radius` 确认 DetailScreen 改动不影响其他页面。

4. **Harden** — 农历转换算法可能有边界条件(闰月、春节前后)。`pensive:harden` 扫一遍。

5. **Ship** — `commit-commands:commit-push-pr`
   ```
   feat: add lunar calendar display on detail screen
   ```

## Example 2: Add dark mode toggle to QQ Bot dashboard

User: `/dev QQ Bot 后台加个暗色模式切换`

1. **Plan** — 读现有主题系统、Dashboard 组件。方案：复用系统已有的 ThemeProvider，加 Toggle 组件到 Settings 页。
2. **Build** — TDD 写 ThemeToggle 测试 → 实现 → 接入。
3. **Review** — `pensive:unified-review` 全面审查。
4. **Harden** — `/simplify` 快速过。
5. **Ship** — commit + push。
