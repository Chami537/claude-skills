# Wrap Examples

## Example 1: After fixing DateMemory destructive migration

User: `/wrap`

Agent output:

```
## 本次开发总结

**项目**: DateMemory
**类型**: bug修复

**变更文件**:
- AppDatabase.kt — 用 addMigrations 替换 fallbackToDestructiveMigration
- build.gradle.kts — 加 ksp schemaLocation + room-testing 依赖
- MigrationTest.kt (新) — 1→2 迁移测试
- libs.versions.toml — 加 room-testing

**做了什么**:
修复 Room 数据库升级时静默清空用户数据的问题。
改为手动 Migration，缺迁移时崩溃报错而非丢数据。
```

Agent: "这次有什么踩坑或经验？"

User: "exportSchema 设成 true 之后必须在 build 后手动复制 schema JSON，不然 MigrationTestHelper 找不到"

→ Saved as memory: `datememory-room-schema-export`

Agent: "当前完成状态？"

User: "核心完成，但 2.json 还没生成，需要在 Android Studio 里 build 一次"

→ Updated project memory: DateMemory destructive migration fix — pending schema JSON generation

## Example 2: After adding a new feature

User: `/wrap`

Agent output:

```
## 本次开发总结

**项目**: QQ Bot
**类型**: 新功能

**变更文件**:
- WeatherPlugin.kt (新) — 天气查询插件
- BotMain.kt — 注册新插件
- WeatherPluginTest.kt (新) — 测试

**做了什么**:
新增天气查询功能，用户发"天气 深圳"返回实时天气。
接入了和风天气 API，加了 1 小时缓存防刷。
```

Agent: "有什么经验？"

User: "API 返回值里 city 字段有时候是 null，得用 safe call"

→ Saved as memory

Agent: "完成状态？"

User: "已完成，可以合并"

→ No progress update needed.
