# n4：同一 .5H 的原 DN 已真实进入迭代

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

完整 native 流接口完成后，已实际启动原 worker 的同 H 非线性 DN 求解。原程序自己接受了步长 $1/32$，第二个完整 Jacobian 评估给出残差 $5.706851798321002\times10^{-9}$，低于初始的 $1.5211857880292614\times10^{-8}$，但仍高于原 $2\times10^{-9}$ 接受门。当前记录不声称 DN/Jac/audit 已完成。

## 固定入口

continue_native_tail_checkpoint.py（117b0a6d…）固定计划7aadf151…从 b4356eab… 的完整保存态出发。源、plan、config、实际 observer 命令和已发生的日志前缀绑定在 native_original_DN_entry.json。

原 cfg 只改 initialCheckpoint 与 traceFile 两个路径。M20、spacing4、N512、物理深度8、parts32、RK16、原线性远端图、生产 projectionFloor=.05、36次迭代上限、原线搜索、原 sparse 后向误差门、2e-9 与 audit32 均保持。只请求一次完整 H 向量，jacobian=true、audit=true；没有新的 warmup 比例列表、手动邻数或局部状态调整。

这里的 .5H 是既存 raw b=.16、lambda=.02 前缀的初始化路径中的目标。它尚不是 fullH 与前缀的实际联立结果。

## 实际初值身份

原 worker 的 same-M/same-parts remesh、相同 H 的 ratio1 和 Dirichlet 初猜修补照原代码执行。不是仅据这几个名称推定相同：首份完整21640952字节 payload 与已登记的完整同态评估逐字节一致，二者 SHA256 均为 bd9b1121152881c0ece0d4e28de2a9c660cca3b53fe32f14d3a58439c46abb1e。

因此，实际送入 native 的全部节点分量、两个0均值、网格、系数与门槛没有被初猜步骤另作改变。实际 ready 的原物理/数值参数，以及真实 request 的全部 H、Jac/audit 布尔值也已核对。

## 已发生的原迭代

observer 会话35038先完成首个完整 Jacobian，iteration0 的原 norm 与入口逐位一致。原 sparse correction 返回后，程序照既定的 $1,1/2,\ldots$ 线搜索检查候选，前五个未被接受；第六个即 $1/32$ 被原严格下降条件接受。

随后 call8 是新状态的完整 Jacobian。其输入除 withJac 标志与 payload token 外，逐字节等于已接受的 call7 state-only 输入。原 iteration1 报告：

- 归一残差：$5.706851798321002\times10^{-9}$；
- minA：0.9807523328210461；
- minD：0.9999448760732821。

没有把 scalar 试步的结果直接当作完整 Jacobian 验收。新的原修正与线搜索正在自然继续；曾讨论的 node0 补齐或具名邻数备选均未执行。

## 记录范围

record_native_DN_entry.py 只读取已经完成且真实返回0的前八个 batch，保存日志的完整前缀和当时资源观察快照，避免给仍增长的日志写虚假的最终哈希。每段场、节点和完整变分仍留在 scratch；发布件只保来源、命令、哈希、计数和上述少量进展标量。

首版只读 collector 把已声明改变的 initialCheckpoint 路径也列入 ready 身份比较，因而返回1；该源和失败说明已单独保存。随后比较仅排除这两个已声明的运行路径，实际返回0。此记录层修正没有修改正在运行的 DN、adapter、manifest 或数值输入。

最终是否通过原2e-9、cutJets、完整审计和 heightJetJacobian，必须另按真实终态登记。本条没有完成 fullH、前缀联立、精确圆弧、闭合或10%连续几何比例。
