# 两组完整 14 行的全物理带法方程：实际有限核验

状态：**启发式 / 数值证据，新的有限算子实现核验**。本条不是实际 gap1.05 场的接受步，也不报告 5292 列求解成功。完整代数依据是 R244；这里把该结构接到已定义的两网格、倒面积平方目标。

## 保留的实际目标

消费 `6a65-geometry-area-ratio-power-two.py` 的 `CompleteAreaTwoGrid`。每个网格保留原 metric、曲率和几何引导的全部 13 行，再加

$$
r_A=\sqrt w\max\{0,(c/\sigma)^2-1\},\qquad
\sigma=|X_s\times X_u|/a,\quad c=1/2.
$$

该供应器的 `gs`、`gu` 已含全部网格权、面积行强度和导数 $-2c^2/\sigma^3/a$。新实现只把其六 jet 梯度的外积加入原 13 行的局部协方差，**不再乘一次半网格权**。两个网格分别使用各自实际 $N$、径向点和原残差顺序。两组 $H=J^\top J$ 相加后，原共同 Sobolev 矩阵只加入一次：$P=H+\eta S$。

全部 Cartesian 分量、角通道之间的交叉项保留。角乘积使用完整离散 rFFT 的有符号矩；频率超出 rFFT 半网格时按实际离散 alias 处理，没有切去高频乘积。新坐标 $T$ 只用于预条件：实际增广算子为 $[JT;\sqrt\lambda L_S^\top T]$，LSMR 的 `damp=0`，原物理二次型没有改变。

## 本次输入与实际返回

使用已公开有限 fixture 的 literal 六 jet 背景定义，另外取新 seed `202611261505` 的 126 个非零系数；没有消费或重生任何研究 checkpoint。径向自由基数 6，全实周期最大角频 3，每个 Cartesian 分量均含常数及全部正弦 / 余弦通道，共 21 个角通道。

训练组为 27 个径向点、10 个整周角；第二组为 36 个径向点、14 个整周角。两组各按原半权参与完整目标，共 774 点、10836 行。面积行有 340 个活跃点，实际面积法矩阵范数约 688.405，故此核验确实检查了新增行。第一组的频率乘积超过其 rFFT 半网格，实际记录 360 次非零 alias 频率对。

本地进程自然 **exit 0**，内部总耗时 `7.040056458004983 s`，NumPy 2.3.5 / SciPy 1.17.0。原始完整输出仅在 Git 外 scratch；本条记录命令、身份及结论。

| 完整比较 | 实际相对误差 / 数值 |
|---|---:|
| 新物理 $J$ 与原共享 Sobolev 坐标的完整算子换回物理坐标 | $2.28798\times10^{-16}$ |
| 全物理带矩阵与独立显式 $J^\top J$ | $2.81612\times10^{-16}$ |
| 所有跨角通道块 | $4.63192\times10^{-16}$ |
| $T^\top(H+\eta S)T$ 与单位阵 | $1.78306\times10^{-15}$ |
| 增广算子与原物理增广矩阵乘 $T$ | $4.68310\times10^{-16}$ |
| 完整增广伴随点积 | $9.21495\times10^{-16}$ |
| 新旧相同二次型的显式物理最优方向 | $2.41914\times10^{-15}$ |
| 原物理 normal 的显式最优方向相对残差 | $1.63055\times10^{-15}$ |

取 $\lambda=.03,\eta=.1$，新旧二次型最小值分别为 `108.31787517162823` 与 `108.3178751716282`。实际增广法矩阵谱落在 `[0.9921141544, 0.9998921911]`，属于 R244 给出的精确区间 `[.3,1]`。LSMR 实际 `istop=2`、4 次迭代，原物理 normal 相对残差 `3.320728877615187e-13`，耗时 `0.14098890300374478 s`。这不是与其他 seed / 网格的速度排名。

完整组装耗时 `0.2687766150047537 s`：点协方差约 `.060645 s`，角收缩 `.192312 s`，径向累加 `.010055 s`，带 Cholesky `.000633 s`。有限核中法矩阵与因子各 127008 字节，记录到的最大显式临时数组合计 1072440 字节；这不是进程 RSS。实际 5292 列的成本尚未测量。这个 6 径向基小核不含径向距离超过 5 的列对，故不将零 off-band 项冒称为新的非平凡带宽实验。

## 可复算命令与源码身份

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  6a65-cartesian-complete-radial-normal-two-grid-area-fixture.py \
  --scripts /path/to/topics/visible-flexible-closed-surface/scripts \
  --solver /path/to/6a65-cartesian-complete-radial-normal-two-grid-area.py \
  --output /outside-git/complete-two-grid-area-normal-fixture01-report.json
```

| 文件 / 定义 | SHA-256 |
|---|---|
| 新双网格完整法矩阵 helper | `8e8d40c05ba5b5e15c49be4c7d91c882d93007567f67caa19a4a43ad39bc2084` |
| 本次 126 列 fixture | `fd2859ebe9f07bff5a10496e27a12ec8b2bb59f0af41af2099127b28a08a4dff` |
| 实际 q=2 面积供应器 | `d8fb8710d4957430b66b474d79a61d3b7bf4fff9915bba1d62ecfea0f96ee97e` |
| 原两组 13 行供应器 | `26b53da871749b90358cef659dc8c23621f649061e0a65b4b9a7f500a05398b3` |
| literal 背景定义 | `48b05a801b07dbff80474f4d0e95d0f6341d61287e4783a0c19a1aa69eaa1935` |
| 本次全部系数 little-endian float64 字节 | `9908b17d5047503f6f63a43edc63e66cf896ed9f5d0a5a911bd58d63908ae832` |
| 实际完整 scratch 输出 | `c3fa40f7610850b30a3243e9458d7e7867d8c8d5f709a1f86be48957a8453c88` |

完整输出的 SHA-256 由本次实际文件计算，不把完整可重算输出入库。后继应由显式新入口消费实际 gap 场，以同一 q=2 目标、固定 $g$、全部 5292 列做完整 nonlinear value、LM 试步和观察。当前活动 q=1 / v5 源码没有改动。
