# 完整物理径向正规带：新非零 91 列实际核验

日期：2026-11-26。会话：Astra-visible-flex-6a65。完整代数证明另见 [R244](../results/R244-complete-radial-normal-preconditioning-spectrum.md)。本文只登记实际新有限输入与执行回执，不重复登记旧主块小核；当前 v5 活动源码未改。

新 helper 保留全部角通道及 Cartesian 分量交叉协方差，完整十三行与旧 $\lambda S$ 方程不变。生产矩阵只存径向半带宽 5 的完整块带；rFFT 对正负和频及超过半网格的离散别名全部正确取用。对角合同缩放仅用于带 Cholesky，三角带调用 BLAS dtbsv。

## 本次实际输入和回执

两源码在 `/tmp/visible-flex-6a65e705/solver-work/`，供 root 按同名复制到本题 `scripts/`；raw 报告留 scratch。

| 文件 | SHA-256 |
|---|---|
| `6a65-cartesian-complete-radial-normal.py`，17831 B | `1fdaa80e4a56631c858c1a0f4f31557ec8a72254170b6b1df4ec16cbe6437361` |
| `6a65-cartesian-complete-radial-normal-fixture.py`，9406 B | `3dce4783c8babede75603aa04d3bb3b019064e2bb274ebaeb2af377bc51a4471` |
| scratch `complete-radial-normal-fixture01-report.json`，5918 B | `dd2bc501f5bda6bced68f30f428ff66f06cffd8d4a010d4a5062717a81dcf0fd` |

实际命令：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  /tmp/visible-flex-6a65e705/solver-work/6a65-cartesian-complete-radial-normal-fixture.py \
  --scripts /tmp/visible-flex-6a65e705/math-research-public/topics/visible-flexible-closed-surface/scripts \
  --solver /tmp/visible-flex-6a65e705/solver-work/6a65-cartesian-complete-radial-normal.py \
  --output /tmp/visible-flex-6a65e705/solver-work/complete-radial-normal-fixture01-report.json
```

进程自然退出 **0**，内部总秒数 **1.4696124519978184**。NumPy **2.3.5**、SciPy **1.17.0**。背景是已有文字定义的完整六 jet 旋转面，本次改用新随机种子 **202611261435**，实际 **91 个非零系数、360 点、4680 行**。不是 Cauchy checkpoint，也没有恢复或借用旧生产输出。

| 本次实际核验 | 数值 |
|---|---:|
| 完整带状 $H$ 对完整小 $J^\mathsf TJ$ 相对差 | $3.8514267028\times10^{-16}$ |
| 全部跨角通道项相对差 | $6.0797613260\times10^{-16}$ |
| 跨角通道块实际范数 | $3708.646115264$ |
| 跨 Cartesian 分量块实际范数 | $3556.407892503$ |
| 完整物理 $H$ 径向带外最大值 | $0$ |
| $T^\mathsf T(H+\eta S)T$ 对 $I$ 相对差 | $3.4654392360\times10^{-15}$ |
| 新增广矩阵对直接旧矩阵乘 $T$ 相对差 | $4.4087653331\times10^{-16}$ |
| 完整增广伴随配对误差 | $3.0912895615\times10^{-16}$ |
| 同一旧 LM 二次问题的稠密物理方向相对差 | $1.5025972871\times10^{-15}$ |
| 旧、新二次最小值（各自实际算得） | $70.63550123814007$ |
| 稠密方向相对原物理正规方程残差 | $1.1752650497\times10^{-15}$ |
| 实际别名频率对计数 | $240$ |
| 角矩相对虚部舍入量 | $2.1009069073\times10^{-17}$ |

取 $\lambda=.03,\eta=.1$，精确代数谱区间为 $[.3,1]$；实际小增广正规谱为 $[.9862436897094943,.9998939202755049]$。新矩阵自由 LSMR 真实 **4 次迭代、istop=2**、**0.0348176770 s**，相对原物理正规方程残差 $4.9653922612\times10^{-13}$。这些是本次小核数据；没有把不同种子的旧主块小核作同输入速度对照。

实际完整装配 **0.0990562510 s**，其中点协方差 **0.0325702030 s**、角收缩 **0.0593368260 s**、径向累加 **0.0040186160 s**、对角缩放 **0.0005957840 s**、带 Cholesky **0.0005289220 s**。小带和因子各 **56784 B**；最大已计显式局部临时量 **603120 B**。该临时量不是进程 RSS，也不包含整个调用者的缓存。

## 当前消费边界

这两个新文件没有改变任何已在 Actions 载入的源码、请求或身份。生产入口仍需另名、显式新来源和自己的实际 baseline；不得把 v5 原 checkpoint 的入口哈希改标签后直接冒成本次生产验证。

当前已支付的是完整有限算子的装配、伴随、原 LM 等价和一个真实新小核。未支付：7760 列成本、真实 Cauchy 输入上的带因子稳定性、任何新完整非线性接受、全曲面连续 metric/reach、共同 $g$ 的族和网格收敛。上述精确谱界也不能替代这些物理门槛。
