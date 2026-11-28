# 固定 g v8：成功解方向后必须观察到完整映射页释放

日期：2026-11-28。root 对已准备但未执行的 v7 发现一个具体资源合同缺口：已核映射 helper 的 `discard_after_solve()` 在 `MADV_DONTNEED` 失败时只记录错误，以保留原 solve 的返回或异常；v7 在原 solve 成功返回后没有检查这个记录，却会继续使用“已提示释放因子页”的非线性阶段预算。

v7 及其所有绑定文件保持原字节。独立 `fixed_support_literal_driver_v8.py` 仅在 `answer=apply(rhs)` 成功返回之后增加检查：`last_solve_page_release.clean_mapped_pages_advised_DONTNEED` 必须严格为 true，否则先记录真实完整方向已经返回，再抛出**工程 MemoryError**，不进入按释放因子预算的下一原 RHS 评估。若原 solve 本身抛异常，流程在这项新检查之前传播原异常，不以页释放错误覆盖它。

这项门不宣称操作系统必定立即回收全部页；原内存预算仍为调度估计。它只保证采用该估计之前，实际 helper 已成功执行其声明的页释放提示。

固定 g、完整原 main、全部数值方程/列/原门、RHS64/Jac32、三阶段预算、真实新 initial `8c4305b836eaa5acb34a50108bb971d117e7ce4014fb754dc3cc5a886bd8959b`、完整匿名 CSR 和 factor-only 存储均与 v7 相同。没有再计算初猜、再做 M16 对照或新 J。仅核源码替换、编译，并确认生成的原 main SHA 与 v7 逐字一致。

独立 once launcher `run_fixed_support_mapped_once_v2.py` 对应绑定 v8 源；仍只在真实 child.wait 返回后清理已验 owner 的临时 factor store，不推断数学接受或自动重试。

- v8 入口 SHA256：`de468785db2b16c044208659b4d9d3ffe5cb82545e3f2189fee3f1fb9a9fa7e3`。
- launcher v2 SHA256：`49bbd690ff1a46a5d8eb8adc0021cbd820aabe9793d22979ad74645831fd2af9`。
- 完整命令及 16 项当前不可变来源绑定位于 `held10-analytic-work/fixed-lambda002-m32-v8-preparation/prepared-command.json`，配套 notes JSON 保留其完整内容和 v7 准备前件。

当前 **v8 尚未执行模型或 BVP**；M32 没有晋级，设计 M48 仍优先实际资源窗口。上述发现是静态资源审查结果，不冒称 v7 运行失败或发生过一次真实页释放错误。
