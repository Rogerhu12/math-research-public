# 独立中心速度接口：实现与人工核验

日期：2026-11-14。状态：**候选接口已实现并人工核验；没有真实候选评价或优化入口**。

文件：`scripts/frame_independent_height.py`。
开发输出：`notes/frame-independent-height-check-20261114.json`。

数学动机是 [R57 的直接实际度量](../results/R57-direct-reconstructed-metric-and-auxiliary-frame-space.md) 与 [R59 的逐圈中心消元](../results/R59-scalar-center-speed-elimination-and-metric-lower-bounds.md)。本接口选择连续径向参数，不把逐圈最小根直接拼成一个中心函数。

## 1. 接口与真实变化

`IndependentHeightProblem(source, height_free=9, height_angular_nodes=384, frozen_metric_definition=None)` 接受一个已经准确绑定原 c0 的 `NaturalBodyProblem` 作为固定标量源和 u/v 基提供器。

它只把原 u、v 系数作为切向未知量。可变 β 不再进入当前状态，旧 β 仅用于永久固定的参考高度速度

\[
b_0(t)=\langle-\sin\beta_0(t,\theta)/\sqrt{1+v_0(t,\theta)^2}\rangle.
\]

再加 9 个连续径向高度控制。主体 metric 仍可选择原 5 个有限控制，或按同一个准确 basis/系数冻结。对于真实的原 234 维 enriched 布局，设计模式为 167 维，固定 g 为 162 维。

这个有限新空间不声称包含原 81 个 β 参数能产生的全部高度函数；也不预设新 Jacobian 已满秩或条件良好。未来真实方向诊断仍须报告秩、奇异值及步长。

## 2. 一个全局高度积分

`HeightBasis` 使用 `[t_c,t_f]` 上准确有理节点的五次 clamped B 样条，首末各去三列，端点三次消失。它返回 value/first/second jets，并用同一个 B 样条的原函数评价

\[
I_j(t)=\int_0^t C_j(s)\,ds.
\]

积分在支撑右侧准确是同一个常数。位置中的中心为

\[
z(t)=z(0)+\int_0^t b_0(s)\,ds+\sum_j\gamma_jI_j(t).
\]

`geometry` 强制径向列表从物理 `t=0` 开始且严格递增。没有任何子 chart 可以重新设置高度锚。核心控制准确零；开放尾只整体移动一个高度，`b,b′` 和全部尾部位置导数保持。

## 3. 固定均值评价与身份

`height_baseline(radial)` 用一个固定完整角网格评价 b0、b0′、b0″。它不使用 `geometry` 本次传入的 θ 集合。其数学定义仍是全角准确积分和原无限 Gaussian 热定义。

`geometry` 自身的 Π 必须使用完整均匀角网格，且角点数为四的正倍数；任意散点 θ 会被拒绝，避免把 FFT 原函数误用于子查询。

`identity(state)` 不包含 GH 阶、参考均值的角节点数或径向积分阶。`evaluation_variant` 分别改变这些数值配置并断言完整身份不变。固定 c0 的身份、物理帽、准确 u/v/高度系数以及完整冻结 metric 都进入身份。

当参考高度均值也采用与旧自然模型相同的角规则时，零新控制重放原自然 c0 的位置。规则不同时，只是对同一数学对象的不同评价，不能声称所有浮点值逐位相同。

## 4. 完整位置二jet及参数列

`geometry(state, radial, theta, quadrature_order=4)` 返回

`X, Xs, Xt, Xss, Xst, Xtt, T, Ts, Tss, Ttheta, metric, height, center`。

`jacobian=True` 额外返回直接度量/形状所需的 `jac_X, jac_Xs, jac_Xt, jac_T`；同时指定 `full_two_jet_jacobian=True` 则再给 `jac_Xss, jac_Xst, jac_Xtt`。

场列的完整二jet通过 T 的三阶参数偏导计算。核心标量导数为

\[
c_v=-vc^3,\quad c_{vv}=(2v^2-1)c^5,
\quad c_{vvv}=3v(3-2v^2)c^7,
\]

\[
(vc)_v=c^3,\quad (vc)_{vv}=-3vc^5,
\quad (vc)_{vvv}=3(4v^2-1)c^7.
\]

`tangent_parameter_jets` 在固定物理 θ 下计算这些列，角导数始终使用 `ψ_θ=1+u_θ`。

高度列分别为 `I_j e_z, C_j e_z, C_j′ e_z`；角向及混合位置导数的高度列为零。主体 metric 列保留 `da,da′,da″` 的全部项。可变 u/v 不再改变 b0，因此这里没有旧模型的 `mean(dVz)` 项；这是一份显式新参数化，而不是在旧链式中遗漏它。

`direct_residual_and_jacobian` 仅提供计算接口：

\[
(|X_s|^2-1,\sqrt2 X_s\cdot T)
\]

加来源中已经声明的 ball/strip 项与权重。没有自动更新，没有非线性优化器，也没有给下一真实求解预定一个新权重。

新几何不提供旧的 `R` 字段，也不调用只有旧中心定义才成立的 `X_s−V=−ΠR` 检查。未来若要在旧 distribution/audit 外层中调用本接口，必须写适配并人工覆盖真实调用路径，不能把旧函数签名照搬。

## 5. 人工验证

只使用人工椭圆 `(A,B)=(.9,.72)`、长度 `1.1`、小自由空间和两侧符号。没有评价任何真实 `c0/c1`。

第一轮最终输出中的相对误差：

| 参数 Jacobian | 正侧 | 负侧 |
|---|---:|---:|
| X | `6.10e-9` | `2.30e-9` |
| Xs | `1.61e-9` | `1.23e-9` |
| Xt | `4.86e-9` | `3.99e-9` |
| Xss | `9.46e-10` | `2.99e-10` |
| Xst | `1.29e-9` | `1.27e-9` |
| Xtt | `1.51e-9` | `1.86e-9` |
| 直接 metric 与形状目标 | `3.83e-9` | `3.70e-9` |

此外：

- b0′、b0″ 的解析链式差分误差分别约 `3.11e-10`、`2.09e-8`；
- 同均值评价规则下，零新控制重放原自然 c0 的全部位置二jet差不超过 `4.45e-16`；
- 设计 metric 冻结之后，全部位置二jet重放差为 0；
- 改变查询 θ 不改变 b0 缓存和固定评价规则；
- 高度控制在开放尾不改变任何位置导数，只贡献同一个整体高度；
- GH 精化与 b0 角均值精化分别记录人工数值差，身份保持相同，没有称它们为连续误差界。

`repo_sources` 已逐式独立核 `Tss` 参数三阶偏导、角列、b0 的两阶链式、样条原函数常量延续、完整位置二jet/Jacobian、metric 冻结与评价身份，未发现 blocker。

这些 `passed` 只说明开发检查，不能作为实际度量、整体嵌入、reach 或任务完成证书。

## 6. 唯一公开 CLI

```bash
python topics/visible-flex-new-mechanism/scripts/frame_independent_height.py \
  --check-only \
  --out "$RUNNER_TEMP/frame-independent-height-check.json"
```

目前没有真实候选入口、输入路径或 optimizer 参数。实际初态回执到达后，才决定是否采用这个参数化、哪一个冻结起点、同 g 还是设计 g、是否需要有界方向以及求解预算。任何将来的研究计算仍只使用本公开仓库 Actions。
