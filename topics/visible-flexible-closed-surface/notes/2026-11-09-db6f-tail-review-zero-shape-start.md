# 原有限尾求解器的零 shape 初猜：独立静态审查

审查人：`/root/tail_theory`，2026-11-09。**结论：下列输入条件下，原 worker 确实把零 shape 数组交给原 shooting；其首次 shape 残差只有切口行，归一范数为 1。** 这是只读源码审查，没有执行新 moment root、RK、flow、DN 或求解器。本审查不保证第一次 Newton 方向可接受，也不保证八轮对照收敛。

## 1. 冻结源码与输入条件

本题文件的 SHA256：

| 文件 | SHA256 |
|---|---|
| `scripts/db6f-prefix-tail-trial-worker.mjs` | `6d53b430a956ba688122cafd11f6e4033f9716ea4d9f4989871f324ac900d837` |
| `scripts/db6f-prefix-tail-trial-core.mjs` | `d475d0f6a0dab247efa751e468052d0f30829e1761ccf7f85094a13fe95902e5` |
| `scripts/db6f-prefix-tail-trial-split.mjs` | `aa50ed54848a0e4e7e2be64a08160e17fa4379df2eed8bf8675baf2d2f344727` |
| `scripts/950f-tail-warm-remesh.mjs` | `91686f1c9e70c36ea53357101b619830015288354d1045116a75b5a9ce47667b` |
| `scripts/950f-tail-subdivision.mjs` | `e44317579d483147aa7fe73b086aba059695aa0f675b831c178902a2c0cb62e6` |

在本题 `repro/source-root/topics/large-amplitude-twist-flex/scripts/` 下的原引擎：

| 文件 | SHA256 |
|---|---|
| `general_root_tail_momentum.mjs` | `182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c` |
| `f6tail_momentum_split_flux.mjs` | `5d77ca058adb634547c91998002eeffb9de5395a9e1e130f7edd4fa65014f578` |
| `f6tail_fast_split_flux_engine.mjs` | `a1c84ba25846f0bf6e9d35092dbc0281d01f60f3d68700dfad20fd598e27e4b6` |
| `f6tail_fast_momentum.mjs` | `3e3e619f255d104e5f86761346f536d722d1de07f40f7cef73161caba8d6793e` |
| `f6tail_cusp_grid.mjs` | `b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f` |

适用的拟议对照是同一个 $s=1/4$ 目标、同一物理背景、同 M15/N256/depth12/p8/s32 和原 `.05` guard、原容差。只替换 shooting 初猜及运行/记录预算。以下条件必须由实际输入包单独核对，本文未把尚未运行的配置当作已验证结果：

1. 恢复 CP 明确标为未收敛初猜；所有 $2M$ 维 shape 节点及对应 raw 节点为零，维数、rawNode、M、physicalDepth、shootingParts 和本次 worker 网格一致。
2. CP 的 `cutHeight` 保留**它所针对的实际非零请求目标** $H$，并明确说明零 shape 尚不满足该边值。这与原 iteration-recovery 记录中的“请求目标”语义一致，不能把它称为零态的已实现几何高度。
3. 本次请求逐项使用同一 $H$，其首模非零；配置 `correctInitialBoundary` 必须是 JSON 布尔 `false`。
4. 沿所用有限 profile，原几何、缩放因子、流和变分所需系数均在原有限浮点定义域；原 stage graph 可构建，归一 scales 保持有限正值。对本次已运行过的同源目标，这不是一项新几何假设；首次实际输出仍应确认非有限量没有出现。

## 2. worker 是否覆盖零初猜

加载 CP 后，worker 将其 `cutHeight` 复制到 `last.jets.height`。收到请求时，它计算

$$
\mathrm{ratio}=\frac{H_0^{\rm request}}{H_0^{\rm saved}}.
$$

只有 ratio 有限且严格位于 $(1/4,4)$，才复制/缩放 `last.states`。上述标签相同时 ratio 恰为 1，零数组仍为零；是否启用 harmonic amplitude predictor 不影响这个结论。

这是一个实质输入陷阱：若将 CP 的 `cutHeight` 也写成零，非零请求除以零得到非有限 ratio，`initial` 就不会赋值。原 `tail.solve` 随后会调用 `initial(target)`，得到线性初猜。因此“零 states、零 cutHeight”并不是所需零态实验。

接着，只有 `initial` 存在且 `correctInitialBoundary !== false` 时，worker 才会添加线性边值补偿。显式布尔 false 跳过这一项。原 `tail.solve` 对传入数组逐行复制，不会把首节点设成 target；数组即使元素全零仍是 JavaScript 真值，不会触发 fallback。

同 M、depth、parts 的 `remeshCheckpoint` 在现有二进分段端点上走直接 copy 分支。它会构造引擎闭包，但不会为这些节点执行插值 RK；零节点及动量的排列均保留。此处不借用 raw 模式升阶或不同网格的额外近似。

## 3. 零 shape 的原 moment root

记一个节点的 shape 为 $y=(Q,\Pi)$。在 $Q=\Pi=0$ 时，原 root 的目标及默认初值 $L$ 都为零。由源码定义，逐角有

$$
P=P_\theta=L=K=U=T=u=0,\qquad D=S=A=1.
$$

原 $f_c,g_c,q$ 都为零，投影 moments 为零，Newton 矩阵恰为单位阵。故首次 root 迭代的 `err=0`，`scale=1e-300`，直接通过原相对门限，不调用 Cholesky 求步或 line search。`.05` guard 在此有严格余量。

在既定有限浮点定义域中，以上结论也保留为数值零；可能出现的正负零不影响残差、guard 或接受规则。本文没有把任何非有限数乘零解释为零，因此 §1 的浮点定义域条件不可省略。

## 4. RK、mean 槽与变分路径

原 split-flux 公式的线性角通量及非线性余项都含 $Q,L,U$，在此均为零。所有 $2M$ 个 shape 导数为零。辅助 mean 槽则为

$$
\dot h_{\rm pert}=r_x w L_0=0,\qquad
\dot h_{\rm bg}=r_x w.
$$

因此**完整带 mean 的状态并不恒为零**。恒零的只是 shooting 实际使用的 shape；背景高度照常积分。root、shape RHS 和其 Jacobian 不读取两个 mean 槽，后者不会反哺 shape。

普通 RK4 的每个 shape 子步都保持零。cusp-aware wrapper 只拆积分区间，重复同一结论。快速变分路径用原 root 和相同 split shape RHS；其 tangent 一般非零，但 tangent 只用于变分传播，不注入 state。故其 shape state 也为零。

`cellFlow` 每段把 $2M$ 维输入复制进补零的 $2M+2$ 数组，返回时只截取前 $2M$ 槽，再除以有限正 `portRatio`。mean 高度另存为报告量，不是 shooting 方程中的未知节点或残差。因此 auxiliary mean 的非零累积不会产生本次 stage 残差。

## 5. 首次归一残差与下一步的范围

以外侧编号 $n=0$、深处 $n=d$，原 stage 残差和深端 Robin 残差为

$$
R_n=\Phi_n(y_{n+1})-y_n,\qquad
R_\infty=\Pi_d-G_d Q_d.
$$

零 shape 使它们全为零。原 DN 接口将物理高度转成 $q=H/r_{\rm cut}^4$；唯一非零行是 $Q_0-q=-q$。原尺度

$$
s_0=\max(10^{-250},\max_j|q_j|),\qquad
s_{n+1}=s_n/|\mathrm{gain}_{n,0}|.
$$

当本次非零目标的最大模大于 $10^{-250}$，其切口归一范数严格为 1；stage 和 Robin 部分均为 0，所以初始总范数为 1。这是原离散方程的残差，不是零态满足完整非零边值的断言。

原 correction 会使用零态处的实际变分矩阵，解含切口 forcing 的原线性化问题；它不必逐位等于独立线性图构造器 `initial(target)`。随后原 guard、全部 shooting 行、原 line search、容差与最终审计照常验收。只知道初始范数 1，不能推断第一步下降、八轮成功、延拓到 1 或完整 prefix/tail 联解。

## 6. 审查边界

本文没有运行数值求解或改变任何引擎。实际输入包还需核对全零、目标标签、配置差分及来源 hash；首次实际日志应确认所述 norm/guard 预期。此对照即使成功，也只给指定 $s=1/4$ 边值下的有限尾 warm，不是完整原 prefix 的边界响应，更不是无限尾或最终几何证明。
