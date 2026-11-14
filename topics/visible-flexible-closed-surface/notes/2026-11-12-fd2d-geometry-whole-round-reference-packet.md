# R166 完整圆参考的最小 jet 包与局部消费

日期：2026-11-12。本组是 [R166](../results/R166-exact-round-prefix-and-complete-increment-equations.md) 的独立数值读取器，不构造 BVP，不改变任何当前主线 provider、状态或缓存。完整数学推导亦见 [已闭说明](2026-11-12-fd2d-geometry-whole-round-reference-and-gap-continuation.md)。

## 1. 冻结入口

源：[fd2d_gc_whole_round_reference.py](../scripts/fd2d_gc_whole_round_reference.py)，SHA256：`b98a1c32b1e28dc1158803892443f415772a78a3ce397a67038a46e71513ffa7`。

```python
from fd2d_gc_whole_round_reference import (
    FrozenRoundPrefixReference,
    round_increment_residual,
    round_increment_jvp,
    fixed_scale_gap,
)

reference = FrozenRoundPrefixReference()  # 固定的 7c3… base δ=0
packet = reference.jet(s, side='right')
definition = reference.definition()
```

候选身份固定为 `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`，复用的准确分片定义与数值半径 reader 为 `fd2d_frozen_ellipse_candidate.py`，SHA256 `393848295e1d8e321c057286d722f47a6c51665aa1a35f4b3bbed3a63ddeac30`。入口不接受当前目标 $\delta$，因此 $S_0$ 不会随未知参数改变。

`jet` 对一个标量也返回一个点的数组。若 $s$ 有形状 $(N,)$，以下分量场形状为 $(N,3)$；可直接广播到 $(N_\xi,N,3)$。分量顺序始终为 $(n,m,l)$。

| 键 | 含义 |
| --- | --- |
| `values` | $S_0=(\cos\phi/a,0,-\phi_s)$ |
| `ds` | 所选分片的真实物理径向一 jet |
| `dxi`, `dxi2`, `ds_dxi` | 完整角函数的零导数，不是投影后零系数 |
| `a`, `a_s`, `a_ss`, `c0`, `K0` | 固定圆参考的物理标量 |
| `phase`, `phase_s`, `phase_ss`, `b` | 数值相位及对应分片的导数；`b` 在末端采用稳定公式 |
| `piece_index`, `cut_mask`, `side` | 实际分片及单侧约定 |

数学参考是准确共享两 jet 和相位积分定义的函数；本读取器是 binary64 求值，不是新的区间包。R166 的全段 $|\kappa_i|<7$ 证书独立保留，不由本组八点检验推出。

## 2. 末端正确的稳定公式与单侧导数

令 $r=s_c-s$，$D=\pi/2-1.45$，$L=.026$。准确末桥满足

$$
\epsilon=D\left(3\frac{r^2}{L^2}-2\frac{r^3}{L^3}\right),
\quad \phi=-\pi/2+\epsilon,
\quad b=\sin\epsilon,
\quad l_0=\epsilon_r.
$$

代码使用以上公式得到 $n_0=b/a$，不在近 cut 处计算 $\sqrt{1-a_s^2}$，也不以 `cos(-pi/2 + tiny)` 的舍入余量代替 $\sin\epsilon$。准确 cut 单独返回 $(n_0,m_0,l_0)=(0,0,0)$、$(a,a_s,a_{ss})=(.8,-1,0)$。

径向导数是

$$
(n_0)_s=-\frac{a_s\phi_s}{a}-\frac{b a_s}{a^2},
\qquad (l_0)_s=-\phi_{ss}=-\epsilon_{rr}.
$$

在 cut 从 prefix 左侧的 $(l_0)_s=-6D/L^2$ 一般不为零。本次数值为约 $-1072.1567467002658$，平尾上的对应导数为零。`jet(s_c)` 明确只给 prefix 左 jet；它不声称第二基本形式在该接合处为 $C^1$。曲面满足 R136 的 $C^2$ 两 jet 接合即可，不能据此增设更高阶门槛。

一般内部分片边界由 `side='left'/'right'` 选择一侧的 $l_s$。共享曲面两 jet 使第二基本形式值连续，但不要求其径向导数处处两侧相同。

同一准确末端还有

$$
n_0\sim\frac{3D}{a_cL^2}r^2,\qquad
l_0\sim\frac{6D}{L^2}r,\qquad
\frac{l_0}{n_0}\sim\frac{2a_c}{r}.
$$

因此本入口和下面的增量核始终保留三个分量，不以 $n_0>0$ 消去 Gauss 后再把这种除法延伸至 cut。该渐近式不被用作非圆分支不存在或额外幅度限制的证明。

## 3. 增量核和完整参数方向

```python
out = round_increment_residual(
    packet, increment, increment_s, increment_xi,
    a=target['a'], c=target['c'], K=target['K'],
    U_s=coordinates['u_s'], U_xi=coordinates['u_xi'],
)

direction_out = round_increment_jvp(
    packet, increment, increment_s, increment_xi,
    direction, direction_s, direction_xi,
    a=target['a'], c=target['c'], K=target['K'],
    a_direction=Da, c_direction=Dc, K_direction=DK,
    U_s=coordinates['u_s'], U_xi=coordinates['u_xi'],
)
```

增量和全部 jet 都是同一实际物理点上的完整角函数，形状为 `(...,3)`。返回 `fields`、`codazzi`（最后一轴为 $C_n,C_m$）、`gauss`；主函数还返回实际 `inv` 和 `adv`。数学公式完全采用 R166，并保留 $(c_0-c_\delta)(l_0-n_0)$ 和 $K_0-K_\delta$。参数方向函数要求调用方提供实际增量的完整方向，包括 tail 的 current-radius 链及任何 R153/R155 非线性合成。它不推测这些链式项，也不偷偷更换 lifting 或投影角函数。

接口中的 target 标量可以来自现 `RadialBumpProfile.jet`；这一次局部核正是如此。若未来零幅 driver 希望把同一准确 $\delta=0$ 背景的浮点相消也写稳定，记 $q=\sum\delta_j\psi_j$，有直接恒等式

$$
c_\delta-c_0=\frac{q_s-c_0q}{a+q},\qquad
K_0-K_\delta=\frac{q_{ss}+K_0q}{a+q}.
$$

这避免将两个独立数值求值的近同标量相减；它仍是同一个准确物理 $g_\delta$。本次薄包没有另改已有 profile 的浮点求值过程。报告中零增量残差为逐位零的核使用同一个 `packet` 的 $c_0,K_0$ 作为目标标量；它不声称任意独立旧求值器之间均逐位相等。

## 4. 中央 circle 与零目标 gap

准确中央仍直接复用

```python
core = BalancedCurvatureCore(coefficients, base_kind='circle')
gap_row = fixed_scale_gap(actual_gap, target_gap, scale=.9)
```

`fixed_scale_gap` 返回归一后的 `value`、对实际 gap 的导数 $1/\sigma$、对目标的导数 $-1/\sigma$ 及固定 `scale`。目标可以严格为零；尺度必须保持为一个预先明确的正常数，不能再随目标幅度趋零。

在固定 seed 角中，准确中央曲率增量就是

$$
n_c(d)-\frac1{a_0}
=\sum_j d_j\bigl(\cos(2j\xi)-\mu_j\bigr).
$$

未来表示可直接求这个完整增量，零 $d$ 时它是准确零，无需从两个不同精度的 $1/a_0$ 求值中相减。本次也如实记录了原 Candidate 的 binary64 $a_0$ 与中央模块长双精度代表之间约 $1.09\times10^{-16}$ 的差，而没有把这一数值差冒充新的物理度量。

## 5. 唯一一次局部真实运行

检查源：[fd2d-whole-round-reference-check.py](../scripts/fd2d-whole-round-reference-check.py)。报告：[whole-round-reference-check-01](2026-11-12-fd2d-whole-round-reference-check-01.json)。实际 session `3755`，初块 `a1fba0`，结束块 `39f29a`，自然退出 `0`；内部耗时 `1.5490842500003055` 秒，最大 RSS `67236` KiB。

范围为 8 个真实标量位置，2 个实际非零 bump-profile 位置乘 3 个固定计算角，以及一个非零 profile/场方向。没有读取任何主求解接受态、装配完整 F/J、积分 body 或启动 BVP。

| 核对 | 实际结果 |
| --- | --- |
| 独立 $l_0n_0-K_0$ | 0 |
| 独立 $(n_0)_s-c_0(l_0-n_0)$ | 最大 $8.8818\times10^{-16}$ |
| 同点原始 Gauss/Codazzi 与增量式 | 最大绝对差 $4.4409\times10^{-16}$ |
| 非零方向 JVP 对独立原式中心差分 | 最大绝对差 $4.0111\times10^{-11}$，步长 $10^{-5}$ |
| 两处径向一 jet 对中心差分 | 最大尺度化差 $6.084\times10^{-10}$ |
| 切口三场值 | 准确返回零 |
| `nextafter(s_cut,-inf)` | $n_0\approx3.30384\times10^{-29}$，$l_0\approx2.38067\times10^{-13}$，有限且为正 |
| 与原 radius reader 的 8 点标量差 | $a,a_s$ 为 0；$a_{ss}$ 最大 $6.6614\times10^{-16}$ |
| 复用 circle core 的实际 gap 及固定尺度零目标行 | 均为 0 |

以上是接口与局部代数核，不是新的连续后验；也不把非零方向差分误差当作整个未来求解器的 Jacobian 证书。全段曲率与准确几何结论来自 R166，分支存在、真实 seam/高度及强目标仍按主课题实际进度处理。
