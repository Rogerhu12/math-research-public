# continuation02 的同模数 warm 缩放：只读源码核查

日期：2026-11-09。作者：`/root/tail_theory`。

状态：固定源码和已关闭输入的静态核查；没有新 root、RK、flow、Jacobian、BVP、导出或连续后端调用。没有读取活跃的 trace、iteration checkpoint 或完整 shooting state。本稿不判断当前请求是否已收敛，不改变主求解器。

## 1. 结论及作用域

同一 persistent worker 从成功的 $s_0$ 请求转向 $s_1$ 请求时，当前分支是**整个旧 shape state 乘同一个首模比例，再加满足新 cut 高度差的原有限线性解**。它不是把第 $j$ 模的整个旧 state 乘 $(s_1/s_0)^j$。

虽然 continuation02 配置中 `harmonicAmplitudePredictor=true`，该分支还要求新请求的第 2 至第 15 个存储模态全部严格等于零。冻结 affine 目标的 15 个高度系数全部非零；在本稿讨论的 $s\in\{11/16,12/16,13/16,14/16\}$ 下也不会下溢为零。因此此处 harmonic 分支不触发。配置中没有 `correctInitialBoundary` 键，原默认条件 `!==false` 使全模边界修正启用。

这说明没有由开关切换引起的新初猜机制。高模 cut 目标的相对变化可以明显大于首模变化，但这本身既不是 shooting 残差的上界，也不是实际非线性 root 接近 guard 的原因证明。以下只给出可核验的源码公式及其限制。

## 2. 冻结输入与真实调用链

来源及 SHA-256 全列于同名 `-sources.json`。本次读取的数值对象仅是已关闭的配置、launch 元数据及固定 affine prefix 的目标向量；输出只有维数、非零判据和少数比例标量，不复制源数组。

实际链为：

1. `db6f-prefix-tail-amplitude-continuation.py` 从 `predicted_cut_height` 读取物理高度 $h^*$，以存储下标 $j-1$ 对应幂 $j$，请求 $h_j(s)=s^jh_j^*$；$s=1$ 单独使用 `goal.copy()`。
2. `db6f-prefix-tail-continuation-client.py` 创建 `db6f-prefix-tail-trial-worker.mjs`，不是零态 pilot 的单独配置。新高度不同于 cache key 时发出真实请求。
3. worker 通过 `db6f-prefix-tail-trial-split.mjs` 使用原 `db6f-prefix-tail-trial-core.mjs` 的 `initial` 与 `solve`。split 包装替换 engine 的 root/RHS，但不替换 warm 缩放或线性边界修正。

已读 continuation02 配置为 $M=15$、physical depth 12、每 raw segment 分 8 个 shooting stage、每 stage 32 个 RK 步、angular quadrature 256、`solveTolerance=2e-9`。配置没有 `projectionFloor` 覆盖；本稿不重新证明原默认 guard。旧原方程和当前活 worker 均未修改。

## 3. warm 初猜的精确实算术公式

记同一冻结物理 cut 半径为 $c$，每个节点的 shape state 为 $y_n=(Q_n,\Pi_n)$。原 `cutJets` 返回的非均值物理高度是 $c^4Q_0$；原 DN 包装将新物理高度除以 $c^4$ 交给 shooting。

令 $\mathcal L_n(v)$ 表示原 `tail.initial(v)` 在第 $n$ 节点的值。其定义为

$$
Q_{0,j}=v_j,\qquad \Pi_{0,j}=G_{0,j}v_j,
$$

$$
Q_{n+1,j}=Q_{n,j}/g_{n,j},\qquad
\Pi_{n+1,j}=G_{n+1,j}Q_{n+1,j}.
$$

这里 $g_{n,j}$ 与 $G_{n,j}$ 是同一固定离散背景上的 linear gain 和 graph；$\mathcal L_n$ 是对目标 $v$ 的线性算子，不是非线性 DN 解。

令 $h^{\rm old}=c^4Q_0^{\rm old}$ 是 `last.jets.height`，并令

$$
\widehat\rho=\frac{h^{\rm new}_1}{h^{\rm old}_1}.
$$

若原 guard $1/4<\widehat\rho<4$ 成立，当前分支给出

$$
y_n^{\rm guess}
=\widehat\rho y_n^{\rm old}
+\mathcal L_n\left(\frac{h^{\rm new}}{c^4}
                     -\widehat\rho Q_0^{\rm old}\right).
\tag{1}
$$

因此在精确实算术模型下，初猜的 cut 高度满足新 Dirichlet 目标；它的内层 state、momentum、stage matching 和非线性 Robin 残差仍须由原求解器实际评价。

若仅为解释比例，另外假设旧 cut 完全满足 $h_j^{\rm old}=s_0^jh_j^*$，并写 $\rho=s_1/s_0$，则

$$
\widehat\rho=\rho,\qquad
\delta Q_{0,j}
=\frac{(\rho^j-\rho)h_j^{\rm old}}{c^4}.
\tag{2}
$$

一般实际旧 cut 有非零求解和舍入误差，仍应使用 (1)，而不能把 (2) 当作保存浮点数组的逐位恒等式。程序中的 `np.float64(s)**powers`、乘除法以及线性传播都按原 binary64 运算；本稿的有理比例仅核查其理想实数关系，不认证这些操作的总舍入误差。

## 4. 较高模目标变化较大，但相邻三步相对变化递减

在理想路径上，从 $13/16$ 到 $14/16$ 时 $\rho=14/13$。首模增加约 $7.6923\%$，第 15 模的目标倍率为 $(14/13)^{15}\simeq3.03928$。原线性边界修正的第 15 模占新 cut 目标的比例为

$$
\frac{\delta Q_{0,15}}{h^{\rm new}_{15}/c^4}
=1-\rho^{-14}\simeq0.645665.
$$

这只是一个**相对很小高模目标**的比例：冻结 $h^*_{15}=8.873136367407456\times10^{-16}$。它不是说所有节点的第 15 模都被额外放大三倍，更不表示实际 $A,D,S$、Newton 方向或残差按这个比例变化。

| 理想 $s_0\to s_1$ | 首模比例 $\rho$ | 第 15 模目标倍率 $\rho^{15}$ | 第 15 模 cut 修正占新目标 $1-\rho^{-14}$ |
|---|---:|---:|---:|
| $11/16\to12/16$ | $12/11$ | $3.6883184694$ | $0.7042258959$ |
| $12/16\to13/16$ | $13/12$ | $3.3222445212$ | $0.6739152322$ |
| $13/16\to14/16$ | $14/13$ | $3.0392767694$ | $0.6456646898$ |

这些比例是用 `Fraction` 计算后显示的诊断小数。三步相对增幅递减。绝对高模高度及线性修正仍可增加；没有 gain、原 state 和非线性敏感度的附加界时，不能从此表推出完整初猜残差递增或递减。

## 5. 状态保留、回退及不成立的归因

原 worker 只有在 `sol.converged` 时执行 `last=sol`。失败调用中的保存迭代和 trial checkpoint 用于诊断，不会替换 persistent `last`。controller 在真实失败响应关闭后将步长减半，并从最近成功的 $s$ 再请求。每次请求仍有完整新 Dirichlet cut 方程；失败不被当作成功。

`remeshCheckpoint` 只在 worker 初次载入 `initialCheckpoint` 时调用。在同一个 persistent worker 的连续请求间没有重新 remesh、换模数、换 physical depth 或重新乘 momentum gauge。`tail.initial` 同时构造 $Q$ 与 $\Pi$ 的线性修正；它没有在此另添 mean-height 状态。mean 背景槽由实际 flow 处理，不是这条 shape 初猜比例的分母。

源码也保留不满足有限比例 guard 时的原退路：不提供 `initial`，由 `tail.solve` 使用当前目标的原线性初猜。这是条件分支说明；本稿没有读取 active trace，不能仅凭本稿宣称某个实际调用的全部状态或分支数值。

本核查支持的窄结论是：固定配置和非零高模目标下，连续 warm 的算法规则没有随这些 $s$ 值发生新切换。实际停滞应由已保存的真实残差、被拒 trial 和 guard 记录判断。公式 (1) 本身不保证良好初猜，不证明当前分支有解，也不证明无解；不据此降 guard、替换方程、接入另一 engine 或启动新求解。

## 6. 复核边界

本稿独立读取并哈希绑定源码、冻结配置、launch 和 affine 目标，只做有理比例运算。没有使用未关闭响应，没有采样新 root，也没有替代 `/root/coupled_prefix` 对实际 call trace 的另外审查。本稿不支付 G5、完整 M15 联解、实际 XYZ metric 或无限尾存在。
