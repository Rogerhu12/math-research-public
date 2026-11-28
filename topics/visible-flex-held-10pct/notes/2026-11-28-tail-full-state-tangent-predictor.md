# 用真正末次全段 J 生成完整未知初猜，跳过不必要的幅度序列

## 已实算的有限工程事实

`tail_full_state_tangent_predictor.py` 在新真实 M16/N256/f=.5 接受包 `07981819451ea4d2f48c69f39f7d5c43d3039899915c7c9d5e62fd8bbcda05c3` 上实际运行成功。逐段核验所选原 native J 输入与该包的全部 1153 行接受状态逐位一致，所选记录为 `0003-jac-record.json`，SHA `6f90293aeb6c98020b3d964ab55428ec45c87e86fca1b472cc3b1aefdaac518a`。不是入口 J，也不是上次 Newton 迭代的 J。

这次小规模入口验证保留全部 **1153×32=36,896** 个 M16 shooting 未知。用冻结原 factory 重建相同 gains、各段 portRatio 和深端 Robin graph；按原第一模归一化建立同一全节点稀疏线性系统。右端包含原接受场的剩余各段残差、深端残差，以及向 M16 的完整 f=1 高度向量移动的全部 Dirichlet 差。该向量是 M24 来源的前 16 模；本条没有把它说成完整 M24。

未修改的原 `sparse_shooting_linear.py` 返回：normwise backward error `5.521451343042954e-28`，componentwise backward error `1.0437337122107626e-16`，总维数 36,896、nnz 1,216,560，内部 LU/改进约 .490 s。包括序列化、完整系统构造和检查的本次线性步骤 wall 约 6.18 s。生成物明确标为 **UNACCEPTED**，SHA `dfc5f4ad018adfcb0656ce08ebfa598fcfccb3abe6090a39d3db49fba2029d95`；没有为它支付新的 nonlinear root/domain/residual/audit，也没有宣称 f=1 尾接受。

## 为什么可省后继请求

读过的原 worker 只有在高阶高度全部恰为零时才使用 harmonic amplitude powers；本题全 H 非零，旧 warm start 实际是统一首模 ratio 加原线性边界补偿。原 chord3 每个声称接受的请求仍会做 fresh-final-J。因此预设 `.625,.75,.875,.9375` 各自接受通常会分别重复支付昂贵全段 J；这些幅度值不是课题定义或完成标准。

新独立 `adaptive_full_height_tail.py` 从真实完整维数接受包出发，把上述完整状态预测作为 `initialCheckpoint`，直接请求原 **f=1、全部 H、原 full height J、audit**。原工厂、所有未知/边界、原方程、投影与 Frenet 门、36 次原迭代上限、原线搜索、残差阈值与审计都不变。只有完整原 worker 真返回后才能登记接受。若数学试探失败则保留失败包，在当前真接受幅度和失败目标间二分；工程失败不冒充数学失败来二分。

`pause_after_audited_tail_request.py` 只观察当前请求的真实 final fresh-J 返回且残差已过门后的边界；该请求未请求 height J，原源表明其余 cut/audit 路径不再调用 native。于是仅预占下一次 native 输入的全新路径，使后继预设请求在任何 native 积分前得到明确的 EEXIST 交接。当前接受包和 summary 不作写屏障，源文件、manifest、二进制不动。该观察器自身不把 fresh-J trace 当最终接受，必须等当前原 audit 和完整响应保存。

在本条写作时，新 M24/N512/.5 的原 solve 仍在执行；尚无该请求的最终接受断言，也没有启动它的 full-H 后继。本条新增的是实算过的完整未知切向初猜与后继执行入口，不是 full-H、outer coupling、闭图或共同度量收敛结论。
