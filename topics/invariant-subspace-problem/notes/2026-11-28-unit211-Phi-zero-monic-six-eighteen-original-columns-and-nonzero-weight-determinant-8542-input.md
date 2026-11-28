# Phi：首一 λ6 的十八列原关系与固定好点的非零纯权 determinant 输入

日期：2026-11-28（Asia/Taipei）。尚未执行；120 秒 / 1 GiB。

## 1. 原模型和真正新目标

已成[整个 Phi 的原 NS/PS 六次标量](../results/R150-appendix-unit211-Phi-zero-whole-original-NSPS-sixth-scalar-and-regular-three-source-extension.md)
给 $C_6\in I_6\subset I_{10}$，不需要 $\Delta_N\ne0$。记其真实最高系数为 $h=[\lambda^6]C_6$；在当前旧权环中，$h$ 与完整未付 $H_{42}$ 相差已付单位。

本次在 $h\ne0$ 图定义
$$
G=C_6/h,\qquad
E=\mathbb Q(u,Q)[\lambda]/(G),\qquad V=E^3.
$$
固定十八个坐标 $\lambda^j(1,T,z)$，$0\le j<6$；编码先取成分 $i=0,1,2$，再取次数 $j$，下标为 $6i+j$。这个自由十八维空间只是必要的环境，不是假定原商自由。

真正新目标是在一个明确好模权点，从有原来源的关系中选出十八个独立列。若成功，完整 QQ 矩阵由这些列的有限原 DAG 定义，通过 adjugate 给出非零纯权必要式；不展开巨大 QQ 行列式，不把单点满秩说成整个 Phi 空。若秩不足，准确保留余维，不宣称该纯权目标已经完成。

## 2. 九个原种子和三个真实动作

九个完整种子为
$$
n,\quad c_{T^2z},\quad c_{Tz^2},\quad
N_S,\quad P_S,\quad R_6,\quad
N_{\rm low},\quad P_{\rm low},\quad V_{\rm low}.
$$
其中 $n$ 是原 N1 余式，两条 $c$ 是原三个均值规则在两个次序下的实际差；后六条就是
[完整 I10 定理](../results/R150-appendix-unit211-Phi-zero-complete-original-values-exact-eighteen-by-two-presentation.md)
的原值定义。它们先由原均值降到 $(1,T,z)$，均有完整原来源，不以裸三维矩阵交换性代替来源。

每个系数只按真首一 $G$ 对 $\lambda$ 降次。动作定义为
$$
r\longmapsto \operatorname{rem}_G(\lambda r),\qquad
r\longmapsto \operatorname{rem}_G(rM_T),\qquad
r\longmapsto \operatorname{rem}_G(rM_z).
\tag{1}
$$
$M_T,M_z$ 是原三个均值的真实规则矩阵。每次替换与原乘法的差属于原三个均值；$\lambda$ 降次的差是 $C_6$ 的已付 $h^{-1}$ 倍。故三个动作都把一个真正原关系送到真正原关系。

全过程不把 $M_T,M_z$ 当作自由代数中的交换矩阵。两个真实歧义种子也一直保留。模计算使用完整首一六次商，包含所有幂零和重复因子，不做根分解。

## 3. 明确 QQ 矩阵与清分母幂

令 $\Gamma$ 是所有九种子、$M_T,M_z$ 输入系数的真实权分母及 $h$ 的有限乘积，重复的同一多项式只取一次。该乘积由源中的准确对象定义；不必展开。每个输入分母直接是其一个因子，因此整除性没有未知步骤。除 $h$ 外，所有这些分母都只含整个当前 Phi 图的旧已付权；本次明确不加入 $\Delta_N$。

九种子的 $\lambda$ 次数至多六，降次至多一次，所以每个种子列的分母由 $\Gamma^2$ 清除。$M_T,M_z$ 的系数次数至多二，作用于最高 $\lambda^5$ 基时只到 $\lambda^7$，至多两次单首一降次；因此它们的十八列动作矩阵分母由 $\Gamma^3$ 清除。$\lambda$ 动作矩阵只需 $\Gamma$。

从一个种子经过 $d$ 次实际动作得到的列，故由
$$
\Gamma^{\,2+3d}
$$
清除全部系数分母。这里的次数上界都由实际原输入检查。

如果选出十八个列，令 $L$ 为它们在固定基中的 QQ 有理矩阵，$d_*$ 为所选 DAG 最大深度，定义
$$
B=\Gamma^{\,2+3d_*}L,\qquad F(u,Q)=\det B.
\tag{2}
$$
(2) 是一个完整、可再生的 QQ$[u,Q]$ 多项式定义，不需要把它的巨大系数展开后才存在。

每个 $B$ 列仍是原关系。源的 $h$ 极点也有相同控制：种子降次最多引入一次 $h^{-1}$；每次 $T,z$ 动作至多再引入两次，原均值来源本身只含旧权分母。因此所选列的完整原来源的 $h$ 极点至多 $1+2d_*$，被 (2) 的幂一并清除。其它原来源分母仍是旧单位。于是
$$
B\operatorname{adj}(B)e_0=F e_0
$$
给出当前旧权环中 $F$ 的完整原 $I_{10}$ 来源。整个 $H_{42}=0$ 分支不会因此被删除；(2) 可能含该旧头的显式幂，所有零支继续保留。

## 4. 模好点只证明这个 determinant 非零

固定素数 1009，并预先列出权点
$(3,2),(3,5),(4,2),(5,3)$。
只根据旧原单位、实际输入分母和 $h$ 是否非零，选择第一个合格点；不根据秩挑选新的点。全部 QQ 系数在 1009 的整性先严格检查，之后只使用这个确定点。

在完整十八维模环境中，Gaussian 只用于挑选原独立列。加入队列的后继始终是一个**实际所选原列**乘 $\lambda,T,z$；不把 Gaussian 余向量、模逆主元或任何点值系数放进 QQ 原来源。

若得到十八列，实际返回整个 $L_{\rm mod}$ 乘其逆为 $I_{18}$，以及清分母后的 $B_{\rm mod}$ 乘其逆为 $I_{18}$。故 (2) 的确定多项式 $F$ 在这个严格可积的点非零，证明 $F\ne0$。所有原来源早已在 QQ 环给出；这里不是把模空性直接提升到所有 QQ 权点。

因此成功时，当前原点必须落在定义 (2) 的真正纯权零集。该零集与整 $H_{42}=0$ 图均保留；本条不会宣称整个 Phi 空。若秩小于十八，则只记录本次实际秩、余维与来源，没有新的非零纯权 determinant 结论。

## 5. 源与依赖

建议源：
`2026-11-28-unit211-Phi-zero-monic-six-eighteen-original-columns-and-nonzero-weight-determinant-8542.py`。

14404 字节，SHA256
`f62613154879f17f529c7f441b34eede870606f89e714cd1b7e6dc4c6357a401`。

只需当前四件纯源码：

- `2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py`，`ISP_PHI_CENTERED_NSPS_SOURCE`；只取其 6125 字节必要原标量和三行定义，SHA `4b152304c41026c94b93147d1360644217c5f15fff88e30264d2e7b02ae6b31d`。
- `2026-11-28-unit211-Phi-zero-slope-full-original-values-twelve-new-rows-eighteen-two-model-8542.py`，`ISP_PHI_I10_SOURCE`。
- `2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py`，`ISP_PHI_SLOPE_SOURCE`。
- `2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py`，`ISP_PHI_FIRST_HEAD_RULE_SOURCE`。

四个新增值仅在真实三列中按已发表定义构造，没有执行原二列变换或旧大 cofactor。无历史 JSON 依赖。所有 timer 限于同一个最初 120 秒截止。最终只输出小的十八列来源 DAG、点值、秩、实际逆乘回、Gamma 定义标识及 SHA；不输出或保存可重算矩阵、行列式系数、编码或分片。
