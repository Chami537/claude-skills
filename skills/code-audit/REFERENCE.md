# 项目专属陷阱 & 通用底线

动态数据来自 CLAUDE.md 和 memory。此为静态备份——无相关记忆时使用。

---

## HITA Agent (Android/Kotlin)

| 陷阱 | 检查方法 | 级别 |
|------|---------|------|
| EAS 三校区 HTML 结构不同 | 改 `BenbuEASWebSource` 或 `WeihaiEASWebSource` 时确认三边 | HIGH |
| Room schema 升版缺 migration | `@Database(version` 变但无对应 Migration 类 | CRITICAL |
| 主线程网络 IO | EAS/Retrofit 调用不在协程里 | CRITICAL |
| ProGuard 破坏序列化 | `@Keep` 缺失，proguard-rules.pro 未保护 Retrofit data class | HIGH |
| Hilt 依赖缺失 | 新增 Module 未 `@InstallIn` | HIGH |
| Compose 动画 — Debug vs Release | Debug 无 R8 优化，Compose 动画掉帧严重。必须 `assembleRelease` 测试流畅度 | HIGH |
| Compose 动画 — graphicsLayer | 位移动画用 `graphicsLayer { translationX }` 不用 `offset(Dp)`，避免每帧 layout | HIGH |
| Compose 动画 — 颜色过渡 | 选中态颜色切换用 `animateColorAsState`，不用 `if` 直接切换 | MEDIUM |
| Compose 动画 — FLIP 补偿 | 改 layout 属性（宽高、位置）会导致撕裂，必须用 FLIP 补偿模式 | HIGH |
| Compose clickable ripple | 圆角 tab/pill 上 `clickable` 的 ripple 会溢出裁剪区，需 `indication = null` | MEDIUM |
| CLAUDE.md vs Memory | 执行性指令（fetch upstream 等）必须写 CLAUDE.md，memory 可能被忽略 | HIGH |
| Hilt @Inject 未 scoped + LiveData 被观察 | `class X @Inject constructor` 内部有 LiveData/StateFlow 字段，多个 Fragment/Activity 观察，但无 `@Singleton` — 每次注入不同实例，更新不传播 | HIGH |

## FlightCompare (Python/FastAPI + Kotlin/Android)

| 陷阱 | 检查方法 | 级别 |
|------|---------|------|
| SQL 注入 | `f"SELECT` / `f"INSERT` / `%s` — 未参数化查询 | CRITICAL |
| 外部 API 无超时 | `requests.get` / `httpx.get` 无 `timeout` | HIGH |
| 敏感信息硬编码 | `api_key` `secret` `password` 在代码中 | HIGH |
| Kotlin 端 TLS 配置 | Retrofit OkHttpClient 自定义 TrustManager | HIGH |

## DateMemory (Android/Kotlin)

| 陷阱 | 检查方法 | 级别 |
|------|---------|------|
| Room destructive migration | `fallbackToDestructiveMigration()` | CRITICAL |
| schema JSON 不同步 | `exportSchema=true` 但 schema/ 未随 migration 更新 | HIGH |

## STS2 Modding (C#/Godot)

| 陷阱 | 检查方法 | 级别 |
|------|---------|------|
| Node 空引用 | `GetNode<` 无 null check | HIGH |
| 帧率依赖未乘 delta | `_Process` / `_PhysicsProcess` 中移动未乘 delta | HIGH |
| 信号未断开 | `Connect(` 无对应 `Disconnect` | MEDIUM |
| 资源未释放 | `new Texture`/`Image` 无 Dispose | MEDIUM |

## 通用底线（4 条）

| 陷阱 | 检查方法 | 级别 |
|------|---------|------|
| 空安全强制解包 | `!!` 无前置 null check | CRITICAL |
| 异常静默吞噬 | `except: pass` / `catch (e: Exception) {}` | HIGH |
| 协程/线程错误 | `GlobalScope` / `MainScope` / `time.sleep` 在 async 中 | HIGH |
| 调试残留 | `Log.d(` / `print(` / `console.log(` | MEDIUM |

---

## 个人网站 (Python/Flask + HTML/CSS/JS)

| 陷阱 | 检查方法 | 级别 |
|------|---------|------|
| data/*.json 写入不完整 | 进程终止时 `atomic_write` 未 flush | HIGH |
| SSG 构建路径错 | `BASE_DIR` 相对路径在 `python manage.py build` vs 直接 `python backend/ssg.py` 不一致 | HIGH |
| admin.html JS 函数膨胀 | 124 函数/2263 行，新增功能在范 JS 里改错 | MEDIUM |
| EXIF/GPS 解析异常 | PIL `_getexif()` 返回 None，未保护 | MEDIUM |
| CRUD 路由复制粘贴 | contact/friend/music/work 修改时忘改另一个 | MEDIUM |

## 维护规则

1. `/wrap` 自动存经验到 memory + 更新 CLAUDE.md。不再需要手动问。
2. 发现新项目陷阱 → 手动追加到对应项目段落。
3. 每个陷阱必须可 grep（有具体字符串或文件后缀）。
