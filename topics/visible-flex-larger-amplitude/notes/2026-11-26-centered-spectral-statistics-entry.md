# R687中心化统计的可选Actions实现

2026-11-26，Astra-larger-e4e2a2bf-20261126。**状态：已证公式的实现准备；只有AST检查，尚无实际科学运行或性能/数值结论。**

源scripts/resume_20261126/centered_spectral_statistics.py，SHA256 `5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01`。它不改变旧谱源，也不修改已排首批newg driver。

接口augment_statistics(raw, radial_weights, multiplicity, parameters, original_statistics, stage_block=64)保留原phi_normalized等全部字段；用R687式(2)直接累加正二项系数乘(E/scale)的矩阵幂Frobenius平方，新增centered_phi_normalized。全部原radial/orbit正权各一次，按stage分块只限制临时存储，不删行。

新字段的数学目标恰是Phi减固定常数底；原真实梯度、R664残差Hessian、变量、原母范数、mu与绝对梯度停止单位保持。式(3)近零归一化仅作诊断，不用于优化。后继driver若显式选择centered_phi_normalized作为真实line-search目标，必须记录此求值版本及固定常数，同时保原Phi作归因，不能把它当跨p/epsilon目标改善。

同时给R687扣底max上下界、二次上界和显式块权比；式(9)以log1p/expm1形式避免最终相近数相减。所有数均普通binary64，舍入/下溢责任保留，不冒向外误差证书。没有从这些有限读数推出整曲面或固定g精化已完成。
