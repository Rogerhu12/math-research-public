# T–Pr 固定预算的一次执行器续接

这不是数学终态或新预算。检查原 session99082 时，句柄返回 unknown process，OS 中也没有该 Python 进程；没有终态退出记录，原因未确定。最后完整 checkpoint 保有 8 个已完成逻辑方向、8 次接受，raw SSE=`8.009221142154029e-9`，下一索引8、damp=`.00390625`。已接受 Y/U 二进制身份为 `aa6e740ca6e2997bafdb975a2bb2e1f760fd347afd81528ae8f7f1d5d1e2b409`。

active 最后停在方向8的 LSMR：Jv/Jᵀv 各432次，当前调用已见178.772s。`direction-008.ready.json` 不存在，因此此方向尚无可复用的完整返回数组；已付 partial 工作至少为这两类各432次乘积，不能隐去，不能称线性收敛或算法失败。

恢复使用同一 `0f2691136d584101317cbbde796050c8896d610f5df186665d2fe92e7db09213` 源和原完整CLI，仅追加 `--resume`，stdout另写 `parallel-implicit-integrated-budget-resume1.log`。原24总方向/20接受、后续512次LSMR、全部580328行/原BC/同g/同尺度/全部门均保持；已完成0..7方向不重做。恢复检查逐项核通过来源、policy、accepted008档及全部完成方向SHA，原active自动进入partial_runs。

真实新session97062的启动回执为：directions_completed=8、accepted_steps=8、damp_next=.00390625、partial_runs=1、SSE不变。随后从同一accepted008重新执行未完成方向8，逻辑索引和总预算没有刷新。

中断输入已另名原字节保存，均只在scratch：

|文件|SHA256|
|---|---|
|parallel-implicit-integrated-budget-interruption1.checkpoint.json|927aecbf4c171a6038c737bec13590e34f1ae49238d8c8330e409520282adbbd|
|parallel-implicit-integrated-budget-interruption1.active.json|a33f8f1b1fcf0d12b0208f44129c8272faf2cab86005d961d3f8ed12d87762dd|
|parallel-implicit-integrated-budget-once.log|79c6ee307132d9e8bd57461034458e01b7968a37f59290f32d656c0a50adcc7d|
|parallel-implicit-integrated-budget-work/accepted-008.npz|648fdbf2a28ed25e8c7cfba70fc3d8440b3a733805ce4c66d12fffc69e13c002|

新Gram–T `efe92…` 预算另用session1878及独立work/out；它从513缓存方向0出发，与本续接互不共享状态或目标。此记录只说明既定预算的恢复事实，最终数值结论另报。
