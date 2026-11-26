# B030 完整回调的径向 1025 真续接

日期：2026-11-26。独立新输入范围，尚未科学执行。只继续原 run45805406202/job139859210576/source09e3c7f0218df2e0f9fe8656e3e2228007ee5001 的 B030 完整已记录状态。

## 原末态与容量需要

原作业因 runner shutdown 中断，没有 FINAL，也没有自然 OptimizeResult。最近完整 THETA_PEAK_CALLBACK_CHECKPOINT 位于 outer1/callback1，UTC10:59:42.0063828。它的 JSON145708 B，SHA25613694ee2aeecf02174c5c578d51c19acdde274aba6477de34ae413428dc9b18e；完整原 stdout1008376 B，SHA25665566cf1ae18c91aa64828a1480c774d0d54a00ab8b5baba4ed9f011a53fb22f。原 stdout 只保 scratch；没有上传 raw/大检查点到仓库。

实际保留的81q就是该完成回调的已接受 metric 候选，binary64 SHA2561f7a907334ebe0fea1b1c2107d05fa1c5ea44ceb052c5ebefeb52367c579482c。旧细读 eta=.26032649730073404、raw几何违约0。旧资格只是这次输入来源；新完整细读会重新判资格。

| 状态 | 径向节点 | 额外角峰 orbit | trust |
|---|---:|---:|---:|
| 回调时实际采用 | 512 | 1167 | 1.20135498046875 |
| 全部已记录待采用提议 | 539 | 1218 | 原trust保留 |
| 新增长的已记录峰 | 对应27个新径向位置 | 51 | 尚未作外层trust适配 |

539真实超过旧513径向容量。关停发生在后续容量判断之前，原终因仍是外部关停；不能反称原run“容量退出”。新范围将径向上限改1025，先采用539实际提议节点，而非直接生成1025均匀点。额外峰容量2048未命中，保持不变。所有原actual和pending坐标逐项保留，原1536全角约束/FFT规则与3072完整细观察不变。新峰仍分512批全部处理，不恢复总候选cap。

原trust尚未适配，不能从原未完成后端猜下一trust；此输入明确继续使用1.20135498046875。不采用任何未刷出的候选，也不把539/1218在原run中叫成已优化状态。

## 最小新实现

新source inverse_r566_theta_peak_radial1025_20261126.py 只负责严格读取这一完整回调、验证完整坐标/来源/成本和已付接口核身份，然后调用冻结的 inverse_r566_theta_peak_checkpoint_20261126.py：

- 原checkpoint算子SHA256 a879573a4dbfd1a58ff7a25e07ac7d03a41916edac250116348dc008b7542a27。
- 原物理模型、空间jet、分块参数AD、完整uniform约束、任意角点oracle、峰定位、SQP接受规则与逐回调flush均不改。
- 只替换输入loader与内存中的schema标签，并以新的CLI上限1025调用同一main；源码文件没有被动态重写。
- 原均匀parity/任意角方向核来自 run45785004209/job139789445888，值parity全部0，方向相对差2.56613526384312e-10。没有重复该科学核，没有重放更早joint或已完成outer。

新source-state小配置137191 B，SHA256756694ac36fcf26d0ece472dc14d39a908e4e25abf588da2fd93688e1d7200ef。它只含后继必须的81q、actual/proposal坐标、物理参数、少量来源/成本/已付核字段；不把大科学结果表作为输入附件。

## 成本和未知区间

原完整回调elapsed=380.59675124700004 s；在此前完整链2254.7471333500002 s之上，已记录科学耗时下界为2635.3438845970004 s。

10:59:42.0063828至11:00:28.3769400关停的46.3705572 s墙钟另记为未刷出的工作区间。这里的具体科学elapsed、后端试点、oracle调用次数和可能新pending未知；不能当作0成本，也不能把墙钟直接并成精确科学计时。新ledger明确 recorded_chain_scientific_seconds_is_exact=false。全局已闭外层和当前尚未fold的两oracle分区在原收据中仅加一次；本次新增成本继续由原a879完整计费。

所有已记录actual/pending均恢复，并不推出关停瞬间全部pending已恢复。新输入明确 all_pending_at_runner_stop_recovered=false 与 post_checkpoint_unflushed_work_unknown=true；known_prior_unflushed_pending_coordinate_count=0只表示此前没有已知丢坐标数，不能否认当前未知后段。

## 单lane执行和静态核

此次workflow只含 rounded-core-B030 一个lane/max1，合作科学时钟2400 s、job50 min。固定Python3.12.14/numpy2.3.5/scipy1.17.0、checkout11d5960a326750d5838078e36cf38b85af677262、setup-pythona26af69be951a213d495a4c3e4e4022e16d87065。复用stdin runner7fde98e3337eb537b18b18789b125fcac57e7382e8f22c755947e907c0ea7785，实际双仓pull/规则差异/QUEUE核/删凭证/stdout-only均保留。

同run的 B038/job139859211031 官方check-run报告hosted runner失去服务器通信，终态11:39:52；原job日志返回BlobNotFound，完整run archive也没有任何B038条目。其本次末q、科学elapsed与新pending未知，不作为此次输入。47分钟job状态窗口不冒充精确科学耗时。它独立保留待核，并不阻塞已识别B030真续接。

新文件：

- scripts/inverse_r566_theta_peak_radial1025_20261126.py：10751 B，SHA2567e05899998ff166808caf821091ab2db4abdbfcd3b4923f02b5907d057a35ad1。
- computations/request-inverse-theta-peak-radial1025-20261126.json：154158 B，SHA25601b8a3704a07db2f170066dac02c230a5f284c91cc15cd2abb3570311313f23c。
- .github/workflows/visible-inverse-theta-peak-radial1025-20261126.yml：3764 B，SHA2568b51538a5fb47222608096118c072b8af63bd4809801fadb5f6c7bfee2f25c5e。

本地仅AST、14份源哈希/静态依赖、request与原已付日志逐坐标比对，不导入或执行科学模块。逆设计中g仍随系数改变；细网接受不升级成固定g加密、连续曲率/全pair reach或README完成。
