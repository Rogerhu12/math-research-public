# R234. 原固定 finite collar 的全域 metric 贡献小于 1.002e-18

作者：exact_closure，GPT-6 Astra Pro，AI 辅助。2026-11-14。

**结论及范围。** 对已交新有限闭组装接口实际采用的 terminal Fourier 二 jet，把导出的 binary64 系数解释为准确输入数据，原固定 collar 的完整半径区间和全部角度上的相对 metric 算子范数贡献有准确有理数上界，其向外舍入数值为

$$\boxed{1.0013852088236555\times10^{-18}}.$$

collar 的端点和宽度保持原值，没有增深度或缩窄接合层。此界小于 binary64 单位舍入误差的百分之一，因而在当前实际计算精度下，这项 finite collar 固有缺陷不是可见的等距误差下限。

这不是无限非轴尾存在性结论。准确有限函数上的界，与证明这些 Fourier jets 来自某个准确无限非线性尾，是两个不同的命题；后者仍未完成。

## 1. 准确有限输入

原接受 A 的 RK12、2305 节点尾 readout 的内端半径为

$$r_1=0.05056158669090205,$$

固定 cuff 是 binary64 数 `0.3-0.25`，即 `0.04999999999999999`。以这两个已保存二进制数的准确有理数值为端点，宽度为

$$L=r_1-r_c=0.0005615866909020606.$$

小 Cartesian 扰动的完整三项 terminal jets 由 `exact_20261114_refined_tail_adapter.py::RefinedTail.node_coefficients(0)` 导出。每项都包含全部 257 个非负频率、三个空间分量，使用

$$V_j(\theta)=\operatorname{Re}\sum_{k=0}^{256}c_{j,k}e^{ik\theta},\qquad j=0,1,2.$$

Nyquist 项是单个实余弦。包含直接累计 small mean 的零模；保留完整非轴及水平扰动。NPZ 保存的 complex128 系数每个实部和虚部均是准确 binary64 输入，脚本在转换前验证没有丢失系数位。原 FFT/ODE 只负责提供这些有限输入，以下界不假设它们是准确 PDE 解。

输入系数包与结果见 `notes/2026-11-14-exact-resume-fixed-finite-collar-bound.npz`、同名 `.json`；SHA256 绑定完整原 readout、实际适配源和系数包。归档后的 NPZ 文件名不同于生产文件名，但内容哈希相同。

## 2. Bernstein 表示与完整证明

在 $t=(r-r_c)/L\in[0,1]$ 上，令 $B$ 为内端零二 jet、外端为 $(V_0,V_1,V_2)$ 的向量五次 Hermite 多项式。它的五次 Bernstein 控制函数为

$$P_0=P_1=P_2=0,$$
$$P_3=V_0-\frac25LV_1+\frac1{20}L^2V_2,\qquad
P_4=V_0-\frac15LV_1,\qquad P_5=V_0.$$

因为 Bernstein 基函数在 $[0,1]$ 上非负且和为一，对任何范数都有

$$\sup_{t\in[0,1]}\|B(t,\theta)\|\le\max_i\|P_i(\theta)\|.$$

径向求导后的控制函数准确为

$$Q_i=\frac5L(P_{i+1}-P_i),$$

再求导时对四次 Bernstein 控制函数应用相同公式，系数为 $4/L$。角向求导与这些线性运算交换。

若任意控制函数的三维 Fourier 幅值为 $d_k\in\mathbb C^3$，则对角导数阶数 a 有

$$\sup_\theta\left\|\partial_\theta^a
\operatorname{Re}\sum_k d_ke^{ik\theta}\right\|_2
\le\sum_k k^a\sum_{j=1}^3
\left(|\operatorname{Re}d_{k,j}|+|\operatorname{Im}d_{k,j}|\right).$$

这是向量二范数不超过分量一范数以及三角不等式的直接结果；当 $a=0$，零频权重取一。有限输入、L、所有控制系数和上述和式都以 `fractions.Fraction` 准确运算。因此对全部 r、全部角度得到：

| 导数 | 向外舍入的范数上界 |
| --- | ---: |
| $B$ | `5.598188035947984e-23` |
| $B_\theta$ | `1.133307727903101e-22` |
| $B_{\theta\theta}$ | `3.1184283571373603e-22` |
| $B_r$ | `4.984259889560216e-19` |
| $B_{r\theta}$ | `1.0090229578648857e-18` |
| $B_{rr}$ | `4.113166665714879e-15` |

现在取未改变的旋转背景

$$F_0=(r\cos\theta,r\sin\theta,h_0(r)),\quad h_0'=w(r),
\qquad g=(1+w^2)dr^2+r^2d\theta^2.$$

在 g 的正交单位标架中，$DF_0$ 是一个具有正交单位列的 $3\times2$ 矩阵 $J_0$。因为 $1+w^2\ge1$、$r\ge r_c>0$，扰动导数矩阵 U 满足

$$\|U\|_{\mathrm{op}}\le b_{10}+\frac{b_{01}}{r_c}=:\delta,$$

其中 $b_{10},b_{01}$ 是脚本准确计算的上述两项有理数界。故

$$\begin{aligned}
\|(J_0+U)^T(J_0+U)-I\|_{\mathrm{op}}
&=\|J_0^TU+U^TJ_0+U^TU\|_{\mathrm{op}}\\
&\le2\delta+\delta^2.
\end{aligned}$$

JSON 保存 $2\delta+\delta^2$ 的完整准确分数。展示的小数经过向外舍入，而不是把通常浮点近似误当上界。这就证明了本条的全域有限 collar metric 贡献界。完整高度反射或空间刚体运动不改变此界。

## 3. 实际执行和用途

源：`computations/exact_20261114_finite_collar_bound.py`。本次运行 `0.97980` 秒，实际退出 0；结束记录见 `-terminal.json`。

```sh
python -u computations/exact_20261114_finite_collar_bound.py \
  --complete "$READOUT/complete-4.json" --out "$OUT/collar-bound.json"
```

这个结论可直接供有限闭组装使用：当前仍占主要预算的是 prefix/tail 的数值求解与重构误差，不能把它们归咎于一个未量化的 collar 缺陷。对于新的大幅接受候选，必须重新消费该候选自己的完整 terminal jets，不能照搬本次系数和数值界。

此界没有把 finite collar 变成准确等距解；它的缺陷一般非零。题目要求的固定 g、固定参数、固定 t 范围加密仍须在实际全族上继续执行；严格无限非轴尾、连续嵌入和完整 reach 的缺口也保留。
