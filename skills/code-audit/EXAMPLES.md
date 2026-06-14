# Code Audit — 使用示例

---

## 场景 1: 开发完成后自查

**背景**：在 HITA 的新功能分支 `feat/xxx` 写完代码，准备 commit 前。

```
你：查bug，只看最近改过的文件
Claude：
  1. git -C "C:/Users/Rinat/Desktop/HITA_Agent" diff --name-only HEAD~1
  2. 扫到 3 个可疑点：

  [HIGH] app/.../LoginFragment.kt:142 — 登录成功回调中未处理网络异常
  根因: try-catch 只包了 EAS 请求，没包 token 刷新
  影响: token 刷新失败会导致 crash
  修复方案: 把 token 刷新也包进 try-catch，失败时跳登录页

  [MEDIUM] app/.../TimetableAdapter.kt:67 — notifyDataSetChanged 在子线程调用
  根因: 网络回调线程直接更新 adapter
  影响: 偶发 "Only the original thread..." 异常
  修复方案: 包裹 withContext(Dispatchers.Main) { }

  [MEDIUM] app/.../CourseDetailActivity.kt:203 — Log.d 残留
  根因: 调试用 log 没删
  影响: 无功能影响，代码不干净
  修复方案: 删掉

  共 3 项，要修哪些？（all / 1 2 / 1 / none）
```

---

## 场景 2: 接手项目后全面体检

**背景**：刚 fork 了一个项目（比如 DateMemory），想了解代码质量。

```
你：audit 全项目
Claude：
  扫了 45 个 .kt 文件，发现 8 个问题：

  CRITICAL — 2 项
  [1] CountdownWidget.kt:89 — !! 强制解包 SharedPreferences，首次安装 NPE
  [2] MainActivity.kt:156 — Room DB 在主线程查询

  HIGH — 3 项
  [3] EventDao.kt:34 — LIKE 查询拼接字符串，SQL 注入风险
  [4] SettingsFragment.kt:112 — SharedPreferences edit 未 apply/commit
  [5] NotificationHelper.kt:45 — Android 13+ 未请求通知权限

  MEDIUM — 3 项
  [6] 3 处重复的时间格式化逻辑（DateUtils.kt / EventAdapter.kt / Widget.kt）
  [7] build.gradle:23 — targetSdk 33，Google Play 要求 34+
  [8] proguard-rules.pro — Retrofit 数据类未 @Keep，Release build 可能混淆破坏

  要修哪些？
```

---

## 场景 3: 模块级深度检查

**背景**：别人改了 HITA 的 EAS 解析模块，你担心三校区兼容性。

```
你：查bug EAS 解析模块
Claude：
  锁定 app/.../source/web/eas/ 下 6 个文件，重点查 REFERENCE.md 中 EAS 专项：

  [HIGH] BenbuEASWebSource.kt:78 — 解析 selectGotoTerm 用了固定 selector
  根因: 威海校区的 HTML class 名不同
  影响: 威海校区学期切换功能失效
  修复方案: 加 selector fallback：先试本部格式，失败再用威海格式

  [MEDIUM] WeihaiEASWebSource.kt:112 — 成绩解析 .sum() 未处理空列表
  根因: 当学期无成绩时空列表 .sum() 抛异常
  影响: 无成绩学期点进成绩页 crash
  修复方案: .ifEmpty { return 0.0 }

  就这 2 项，和 EAS 相关的。要修吗？
```

---

## 场景 4: Python 后端检查

**背景**：FlightCompare 后端新增了机票搜索 API。

```
你：查bug flightcompare api 模块
Claude：
  [CRITICAL] api/search.py:45 — SQL 拼接 f"SELECT * FROM flights WHERE date='{user_input}'"
  根因: 用户输入直接拼接 SQL
  影响: SQL 注入
  修复方案: 改用 SQLAlchemy 参数化查询

  [HIGH] api/search.py:89 — requests.get 调用无 timeout
  根因: 调用外部机票 API 没设超时
  影响: 第三方 API 超时时整个请求挂起
  修复方案: requests.get(url, timeout=10)
```

---

## 触发词总结

| 你这么说 | 触发行为 |
|---------|---------|
| `查bug` | 全项目扫描 |
| `查bug 最近改动` | 只扫 git diff |
| `查bug <模块名>` | 只扫指定目录 |
| `audit` | 同查bug |
| `代码审查` | 同查bug |
