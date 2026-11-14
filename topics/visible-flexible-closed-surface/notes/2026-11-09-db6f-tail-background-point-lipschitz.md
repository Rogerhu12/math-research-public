# 分支交界小盒的单点背景斜率包

状态：**条件引理有完整证明；脚本和本次数值输出待独立审查。** 此文只收紧同一个已冻结背景的区间表示，不改变背景、有限尾图、物理网格或目标度量，也不声称实际 metric 已达到新的门槛。

作者：`/root/tail_theory`，2026-11-09。

## 1. 原因与使用范围

depth4 原函数已由 `independent_geometry` 独立重放全部 36 个 profile，前 18 个 profile 与旧 depth2 表逐值相同。总系数宽判据的 raw2 生产输出覆盖原 M8 网格的 `[2898,3477)`，共有 736 个审计盒。六盒未达 $10^{-6}$ 的工作宽度，其中四盒的反解径向误差已约 $7\cdot10^{-14}$，但跨 cap 分支的值域 hull 仍宽至 $3\cdot10^{-4}$。这不是实际 metric 残差下界，也不需要继续统一加密所有盒。

本稿使用已经独审的同一旋转背景，以及真实物理半径上的界 $|w_r|<24$。在 raw0 内边界的内侧，由 $w\le1/49$ 与背景主曲率界 6 有

$$
|w_r|\le6(1+49^{-2})^{3/2}<601/100.
$$

最后一个严格不等式可平方并作有理数比较。使用 $601/100$ 时必须证明完整连接线段都位于该内侧；不能单凭近似反解选中的 profile 编号作判断。

## 2. 单点 Lipschitz 引理

设 $w$ 在连接区间上连续、分片 $C^1$，且导数的绝对值不超过 $K$。令 $J=[a,b]$ 是需要供应背景的精确物理半径盒。任选合法的二进 source 点 $x_*$，其真实半径和斜率有严格区间包

$$
r(x_*)\in R_*=[r_-,r_+],\qquad
w(r(x_*))\in W_*=[w_-,w_+].
$$

令

$$
d=\max_{s\in\{a,b\},\,t\in\{r_-,r_+\}}|s-t|.
$$

则整个 $J$ 上都有

$$
w(J)\subseteq W_*+[-Kd,Kd].
\tag{1}
$$

**证明。** 绝对值函数在矩形 $J\times R_*$ 上的最大值在某个角点达到，所以每个 $r\in J$ 都有 $|r-r(x_*)|\le d$。在连接线段上的有限个 source/cap/绝对值界面处逐段使用微积分基本定理并求和，得到

$$
|w(r)-w(r(x_*))|\le K|r-r(x_*)|\le Kd.
$$

结合点值包 $W_*$ 就是 (1)。这里不使用 $r$ 的近似反解等式，也不使用跨分支的高阶可微性。证毕。

当前每个审计盒和选点都严格位于 $r>r_{\rm cuff}$，只会经过有限个背景段。各段拼接连续，因此上面的分片论证足够。

## 3. 精确几何与实现

脚本 `scripts/db6f-tail-background-point-lipschitz.py` 读入已完成的背景包、同一 manifest、depth4 primitive 与冻结校准表，并核数据与定义 hash。原物理网格由已有的 `exact_nodes` 恢复：旧 int2 网格使用所存精确二进节点；increment 网格使用精确有理归一系数及精确二进增量和。

每个选定行的 $a,b$ 由该网格及已存二进 $u$ 端点用 `Fraction` 精确计算。近似反解只负责提出一个 $x_*\in[0,1]$；该点转为 binary64 后就是定义上的合法 source 输入。已审 `ProfilePrimitive.point` 供应 $R_*$，已审 stable source 的 order-0 区间求值供应 $W_*$，包括不确定分支时的合法 hull。

令 $r_{\rm inner}^{-}$ 为 raw0 内边界的严格下界。仅当

$$
\max(b,r_+)\le r_{\rm inner}^{-}
$$

时取 $K=601/100$，否则取全域 $K=24$。这同时检查待证盒和实际选点，不会把跨 raw0 边界的盒误放进内尾估计。$d$ 和 $Kd$ 均以 `Fraction` 精确计算，随后经 `qbounds` 向外转成双精度，再向外区间相加，得到 (1) 的常数区间。

若该常数区间的全宽小于原行的“余项加所有系数全宽之和”，便以它替换该行的 $w$ 系数，其余次数精确置零、余项置零。两个候选本来都合法，因此按宽度选择不影响包含性；该比较只决定工作策略，不证明实际 metric 的误差下降。所有 $w_r$ 系数、余项以及整个物理分割保持逐位不变。原 source 编号与 radial residual 辅助列也保持不变，只作为原生产诊断；新选点与其严格物理距离单独保存在 `point_lipschitz.changed_rows`。

输出清楚保留原 producer 的未达工作容差计数，并将旧 `unmet_tolerance_rows` 标为 `null`，因为这里没有重新评判原 producer 的全部 radial/wr 工作条件。新的剩余 $w$ 工作宽度单独记录。输出仍须交实际连续后端计算 metric；原图已通过的曲率结论可以保留，因为图和 $w_r$ 包都没有改变。

## 4. 本次已运行的局部变化

原包 `db6f-tail-background-lowmetric-raw2.json` 的 736 个审计行保留不变；只有四个 $w$ 行被替换。对应的工作全宽为：

| 原 span | 原全宽上界 | 单点包全宽上界 |
| --- | ---: | ---: |
| 2998 | $3.962\cdot10^{-5}$ | $5.891\cdot10^{-8}$ |
| 3115 | $2.967\cdot10^{-4}$ | $6.038\cdot10^{-8}$ |
| 3262 | $1.037\cdot10^{-4}$ | $2.914\cdot10^{-8}$ |
| 3379 | $3.375\cdot10^{-5}$ | $5.832\cdot10^{-8}$ |

原 span 3129 与 3246 的 $2.592\cdot10^{-6}$、$2.551\cdot10^{-6}$ 包保留；它们已低于独立后端预算建议的 $8.4\cdot10^{-6}$，是否实际够用由 metric 权重与后端判定。没有继续为统一 $10^{-6}$ 工作阈值细分。

输出为 `notes/2026-11-09-db6f-tail-background-lowmetric-raw2-point.json/.npz`。运行方式：

```bash
python scripts/db6f-tail-background-point-lipschitz.py \
  --packet notes/2026-11-09-db6f-tail-background-lowmetric-raw2.json \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --primitive notes/2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --out-prefix notes/2026-11-09-db6f-tail-background-lowmetric-raw2-point \
  --minimum-width 1e-6
```

这只解决背景表示中四个宽 hull；既不支付源 ODE 的误差，也不构成无限非线性尾存在定理。
