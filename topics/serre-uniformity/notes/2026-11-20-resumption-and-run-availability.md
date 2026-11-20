# 2026-11-20 接手续跑与产物可用性

状态：运行元数据与保留日志的只读核实，**不是新的数学结论**。
维护会话：serre-public-astra-20261120-de0a3e3b。

从部分克隆的 main `882aa9b74efeaac682df43c197820e7280156357` 接手，已真实 `git pull --rebase origin main`。相比旧规则提交 `b77de2c73aa4565ab4f3c09f1884b455b6b3d4f5`，根 README 只新增 held-10pct 课题行，课题 README 无变化。读取全部当前 H/open、最新 log 和 R907 方法；旧完整 H 保存在 `handoff-archive-2026-11-20-before-resume.md`。

## 实际终态

通过 GitHub CLI 的 Actions run、jobs、artifacts 与 job logs 接口查询；截至本次读取，下列六个 run 都是 completed/failure，其 artifacts API 均返回空列表。空列表不能恢复原字节，也不证明数学否定。

|任务与run|保留日志所证明的事实|不得推断|
|---|---|---|
|[R787 primal 43912581432](https://github.com/Rogerhu12/math-research-public/actions/runs/43912581432)|2026-11-16 21:56 UTC，`complete=false, exit_code=1, error=null`；曾上传 artifact14275737009，478732930 bytes|没有当前CRT对象，不能登记新的prime数或关系完成|
|[R824 43912577191](https://github.com/Rogerhu12/math-research-public/actions/runs/43912577191)|2026-11-16 20:16 UTC，runner shutdown，exit143|不是代数否定；无新产物证明|
|[R854 43921950983](https://github.com/Rogerhu12/math-research-public/actions/runs/43921950983)|2026-11-16 22:48 UTC，exit124，outer_timeout=false；IO报告1625个complete stages、1635个输出文件、1665个carrier成员；四响应、A.1、Z、height均false；曾上传14279297109|不能从阶段数推实际最大Smith指数或四响应|
|[R787 half-dual 43923558852](https://github.com/Rogerhu12/math-research-public/actions/runs/43923558852)|2026-11-17 00:34 UTC结束failure；compute job133539305443日志接口404|内部失败原因、新CRT断点未知|
|[R815 43908105148](https://github.com/Rogerhu12/math-research-public/actions/runs/43908105148)|2026-11-16 21:40 UTC，`complete=false, exit_code=1, error=null`；曾上传14274072540，5302865935 bytes|不能补填Γ进度；已证g696保持|
|[R907 43924786163](https://github.com/Rogerhu12/math-research-public/actions/runs/43924786163)|2026-11-16 19:12 UTC，`KeyError: configuration_sha256`；verify明确`stopped_before_core=true,new_mathematics_executed=false,run_complete=false`|verify中的IO `complete=true`不能当数学完成；j1尚未实际运行|

## 接续决定

先修R907真实生产者schema，不把配置缺键伪造为任意默认值；重新运行还必须取得完整原输入，不能以metadata代替数千维数组。当前一日artifact已不可从run列表读取，旧已证明定理仍按已登记证明使用，现有缺失不能自动撤销或升级它们。

同时接续原R932全SS配对与Q′源比较，以及R929同h偏移；新小计算用公开Actions，提交脚本、参数、run号、确定性输出SHA，不提交可重算产物。主目标保持OPEN。

## 本次读取日志的字节身份

原始日志只在本次临时目录读取，不加入Git；以下哈希用于区别实读日志与摘要。

- `43908105148-133442347214.log`：SHA-256 `3b40621ca14e8669be46406d7500630e8e4e0851284c2636496291f46f80311a`。
- `43912577191-133458143804.log`：SHA-256 `b5c2fff8e4cb9277a548369373f28aaeb2419deeb7e53107e2ac9c5d36b30ef2`。
- `43912581432-133458306139.log`：SHA-256 `cfa5316e056b83a485c75fe94ef9e0c9945af324ead5d92a9522e660270bb66e`。
- `43921950983-133491358255.log`：SHA-256 `4506c711c11a9daa3a1eb42e63968d2f49089fb66a0549f766cb9ae9f7dbf244`。
- `43923558852-133539305443.log`：SHA-256 `7f45a48c400e493a443436e68392ae3f24208878719fc91ded21edd307f52de4`。
- `43924786163-133543328511.log`：SHA-256 `7f55e7c9033427142432e9fccd119dbfe265afcd134fd832fa7fd73c3de52bde`。
