# R133：只补缺失 midpoint 的同 germ Taylor/Hessian 消费合同

本消费者接完整 quarter/cached-centre-Hessian 的实际成功原件。它先消费已成 1341 行的四源系数，分出 16 行缺 midpoint 的预算组；仅当这一组的数值 majorant 至少占当前 selected majorant 的一半时，才对缺点作下面的封闭运算。这个阈值是已使用上界的分组诊断，不是未知实际 residual 的下界。

原 7844 个已成 residual、全部 7908 quarter target 数据、1977 父格、全部 trial/端点和原失败过程不改。最多新增原 64 个缺点对应的 residual 消费；新 target 求值为 0。若诊断不触发、无完整同 germ 路径或无可用原锚点，仍使用原完整 local 行。

## T.1. 分组费用

原实际每行选定四源为 $s_{i,c}\ge0$，四个既成 Green 增益为 $G_c$，原 Hessian resolvent 为 $H$。对任意行集 $J$，只作

$$
B_J=H\sum_cG_c\left(\sum_{i\in J}s_{i,c}^2\right)^{1/2}.
$$

这里每条 $s_{i,c}$ 已有原 ordinary 真 $dr$ 或 divergence joint module 单位，不再乘一次格长。$J_{\rm miss}$ 由实际 native 的 `missing_midpoint_uses_original_full_row` 判定；准确补集也消费。完整各通道平方和应与原 selected 行集一致。触发条件是针对这些数值 majorant 的定向比较 $B_{\rm miss}\ge B_{\rm all}/2$，不用于证明实际残差非零。

## T.2. 同一固定参数与完整闭路径

每个原 quarter 都绑定同一 intrinsic 对象、候选物理 $\eta_0$（仿射偏移 0）以及准确 `actual_scalar_germ`。原零宽球及末端 graft 的 $10^{-9}$ 参数包络都包含这一固定 $\eta_0$；正宽包络没有因此变成零宽的原生点证书。这里只转授到固定 $\eta_0$。

缺点 $y$ 只能使用原生已保存 midpoint 锚点 $x$。沿 $x$ 到 $y$ 的全部闭路径须由原 quarter 连续覆盖，所有 pieces 的 scalar germ 一致、属于该 germ，且保留 $\gamma,\beta,K,s$ 的三阶导数区间。不能跨未证明的接缝，也不把新派生点递归冒充原锚点。

令 $J_3$ 是完整路径上同一真函数三阶导数球的区间凸包，$d=y-x$ 为准确有理数。由带积分余项的 Taylor 公式，

$$
\begin{aligned}
f(y)&\in f(x)+d f'(x)+\tfrac12d^2f''(x)+\tfrac16d^3J_3,\\
f'(y)&\in f'(x)+d f''(x)+\tfrac12d^2J_3,\\
f''(y)&\in f''(x)+dJ_3.
\end{aligned}
$$

这些公式对 $d<0$ 同样成立：积分参数从 0 到 1，余项核非负，积分质量分别为 $1/6,1/2,1$；有符号的 $d^3,d^2,d$ 已包含方向。

每个所得点球与目标 quarter 原 whole0..2 球求交。左右两个合法原锚点都可贡献独立球，再求交；空交失败，不能只挑半径最小的一份。目标点的 third 键仍用原目标 whole3，绝不称其为新准确三阶点值。

## T.3. 原件和派生件分开绑定

原 quarter 行不修改。另建带 `midpoint_derivation_receipt` 的新包络，保存原行 SHA、目标和锚的准确半径、原锚点 jet SHA、完整路径/参数包络、third 凸包、派生 midpoint SHA 和 0 target 计数。

新 residual 仍使用原准确候选多项式、同一 $M=32$、同一 alpha 和完整 moving 公式；只将目标模型的 centre0..2 换成已证明的点球，whole3 原样。原 scalar/Arb 余项全部保留，角支撑 $|j|\le96$、385 的完整 A1 error 因子和 even mean 不变。

其记录明确区分原 quarter SHA 与派生包络 SHA，将 `exact_scalar_midpoint_and_whole_jets_reused` 标为 false，另记准确 whole jets 加已验证派生 midpoint。不得把派生点标成原生已存点。

## T.4. 只更新受影响的完整 local 行

原 7844 residual 行逐字复用；新请求必须是原完整 7908 cover 与这 7844 请求的差集之内，至多 64 个。未受影响的 1325 个完整 local 行也逐字复用。若原缺点组只有部分可合法派生，余下 local 行仍使用原完整界。

受影响行调用原相同的 joint/pointwise 合并与四源公式。内部完整点包络可以包含新派生点；输出必须标明其来源，不能因此把原 `all_target_midpoints_saved` 改成 true。有限系数仍按逐槽跨交段最大值，joint 误差按所有相关完整余项相加；pointwise max 只供 ordinary 乘法。精确 alpha 一次、repair 的 point/joint 费用、物理角 composition、两完整 mean、原 trial 模块和原正交 Gram 全部不变。

每行只在完整四源向量间择一。全区四个平方和、对应四个 Green 增益和同一个 resolvent 共同消费。最后与原完整合法 additive 作整套比较，保留更小者；不能将不同分解的单个通道拼成新向量。

## T.5. 两端和全问题范围

本次只改善同一 $w_0$ 的已知 Hessian additive $E_H(Tw_0)$，不改物理帽 14 项与原六个边界，也不改 $Z-w_0$ 所乘的旧完整误差算子。

后继同一 $Z$ 的真实 odd96、独立 mean、完整 low97 与已知全高输出必须按原切口转换再次完整消费。这个消费者自身不授权新的帽算子范数、未知 high 反馈逆、全 PDE 响应、$\delta_*$ 背景转移或最终参数 Schur。

全部新数值只在公开仓库 Actions 中计算。完整成功/失败过程、真实 pull/README 差异检查、已算点/残差前缀及 lossless native 分片分别保存。后续恢复必须核原科学 source 和输入 SHA，已成功的目标、残差与派生点不重算。
