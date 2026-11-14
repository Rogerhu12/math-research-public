# 真实浅头源函数区间包络

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

完整推导已经登记为
[R26](../results/R26-real-head-source-interval-and-port-coordinates.md)。
实现为 `computations/closure_real_head_source_enclosure.py`；精确向外dyadic端点、所有输入hash和运行统计保存在同名JSON包。

当前node12真实半径区间宽度小于 $2^{-96}$；保存的double与真实源的radius、w、mu差已显式包络。求值器同时返回同一个实函数的r、r_x、w、w_r，另提供整闭panel上的线性生成元区间。

这没有启动或认证新的ODE求解，也不占用团队的大作业窗口。下一实际数学工作是利用该实系数接口构造可靠线性流/Green界，并将R23完整非线性源预算接入真实浅trace。
