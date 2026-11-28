# GSR 使用原 GG 图载体的逐字恢复

[GSR](R149-supplement-selected-signed-Newton-nu-and-whole-cell-Grassmann-response.md) 消费两列真正普通源时需要认证节点基 $L,R$、双基 $\ell,\rho$ 与齐次递推 $C,D$。本实现的 graph-only 恢复接收 [GG](R149-supplement-joint-Grassmann-true-low193-and-whole-source-maps.md) 的 original actual、execution、manifest。三者全部 bytes/SHA256/Git blob、同 run/attempt/checkout、完整两目标、四个原 map 结果、九份 math/proof binding、1424+1424 图及1425个节点、原 21 件历史输入及当前源闭包都由原完整 validator 准入。当前没有可在此报告的恢复成功 SHA。实现位于 [graph restore](../scripts/fourfold_codazzi_grassmann_response_graph_restore.py)。

对 TF 的0–80格调用原 [restore_whole_prefix](../scripts/fourfold_codazzi_true_low193_checkpoint_carrier_restore.py)，包括原失败矩阵的完整 serializer。packed prefix、raw checkpoint、gzip checkpoint 三个原身份和 GG 的 passive-raw-flow 全 SHA 都要匹配。只取此次必要恢复已形成的81对齐次方向，分别按原 GG 的完整 joint ball 字节格式保存。第81格失败 checkpoint 的原64 cuts 与该后继格真正使用的新 order16 自适应 dyadic cuts 各有其原定义。

对81–1423的每格，用 GG 原同一 actual coefficient provider、4个初始子盒和有向 $1-\beta/18$ 门仅细分原失败叶，至多 denominator64，完整叶数还须等于原 actual 对应项。保持两方向 order16 的 complete raw physical transitions。必要的两个齐次方向不需要另外五个 covariance 包。原 Peano 的 prefix span 与四族 moments 在独立变量中求值，其分支不改变计算 forward/backward 的有向式。每个完整 $193\times193$ 中心与 joint radius、norm upper 依原 packing 原样往返。所有大数组只在同一次公共作业的私有工作目录及内存中存在。

在同样原序中，由完整左97图提议 dyadic Householder vectors，将每份定义全部保存再读回。右96图采用原有向非零中心、相同节点全转移及原 outer Robin/independent mean。每枚 graph/node 的实际有向 denominator/residual/radius/transversality 等记录全体按原 JSON canonical 进入 original ordered journal。旧结果的最后1424个 source-map 进度记录是固定的 index、whole count、four roles 元数据；为比较原整个 journal SHA，只串入这些已经准入的字面元数据。科学上没有重新计算任何旧 map 或原 covariance，也不将恢复记作新图证明。

输出前逐份重读四类全部私有基矩阵，另包括 frames 与 $C,D$。要求原 exact-vector 全文件 index、总 bytes、live-matrix 全文件 index、每次原 matrix write 的 journal、计数、live/peak bytes 全相同；任何一份掉失或 SHA/规格不同就没有向后继提供模型。比较完整 signed graph/node 数值记录的原 chain，同时也排除了尺寸相同而所取图不同。浮点仅选择原 exact dyadic frame；若实际 BLAS 调度产生其它提议，不能以仍正交或数值接近替代逐字 identity。

新 signed solver 后续对真实源及边界的计算独立于此恢复。恢复不生成新的允许物理根迹、height、外 Robin、mean、whole positive inverse、负区 ordinary 响应或 nonlinear solution。若图只在本次 GG 原作业内真正保留且源/定义一致，可直接使用该对象而省去跨作业恢复。
