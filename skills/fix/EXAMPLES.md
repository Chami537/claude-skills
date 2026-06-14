# Fix Examples

## Example 1: Room database crash on upgrade

User: `/fix DateMemory 升级后打开闪退，logcat 显示 Room IllegalStateException`

Workflow:

1. **Diagnose** — `/diagnose`。复现：装旧版 APK → 升级新版 → 闪退。定位：`AppDatabase.kt:57` 用了 `fallbackToDestructiveMigration()` 但没有 Migration 对象，版本号变了就炸。根因：版本号从 1 升到 2 时没写 Migration。

2. **Build (TDD)** — RED：写 `MigrationTest.kt` 测试 1→2 迁移。GREEN：加 `MIGRATION_1_2` + 替换 `fallbackToDestructiveMigration` 为 `addMigrations`。REFACTOR：清理注释。

3. **Review** — `/simplify` 快速过。

4. **Ship** — commit: `fix: replace destructive migration with manual MIGRATION_1_2`

## Example 2: Swipe-to-delete triggers on scroll

User: `/fix 滑动删除太灵敏了，滚动列表时经常误触`

1. **Diagnose** — 复现：快速滑动 LazyColumn，偶尔触发 swipe 手势。假设：swipe 阈值太小，或者没有区分 scroll 和 swipe。
2. **Build** — RED：写 UI 测试模拟 scroll vs swipe。GREEN：加入最小滑动距离阈值和方向判断。REFACTOR。
3. **Review** — 单文件改动，跳过 `/simplify`。
4. **Ship** — commit: `fix: increase swipe threshold to prevent false triggers during scroll`
