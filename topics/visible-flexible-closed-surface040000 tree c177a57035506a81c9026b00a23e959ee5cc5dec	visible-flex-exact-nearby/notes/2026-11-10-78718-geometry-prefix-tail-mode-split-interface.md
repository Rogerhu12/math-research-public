# 同一 g 下分开 prefix M 与尾 W 的实施接口

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。
**范围：数学接线及现有 common-cut 的使用条件；没有新 DN/BVP 或兼容性数值。**
物理 profile、cut、width、校准、背景 $E(r)$、参数范围均保持原定义。
$W\ge M$ 只改变尾的 Fourier 分辨率；prefix 仍有 $3M+1$ 状态、$M$ 个
support 参数。当前运行中的 M15/W15 不由本文修改。

## 1. 请求、真实 DN 与 Jacobian

令 $\iota:\mathbb R^M\to\mathbb R^W$ 补零，$P:\mathbb R^W\to\mathbb R^M$
取前 $M$ 项。完整真实尾响应写为
$\mathcal T_W(h)=(S_W,Q_W,m_1,m_2,H_W;\text{完整尾状态})$，依次包含
非均值坡度、二阶、两个均值、实际高度。每个 prefix 请求都真正计算
$\mathcal T_W(\iota H)$，只把
$$
S_{M,W}(H)=P S_W(\iota H),\qquad
DS_{M,W}=P\,DS_W(\iota H)\,\iota
\tag{1}
$$
用于原 BVP 的 $M$ 个非均值边界方程。补零作用在公开高度请求，不是把旧
canonical momentum $\pi$ 补零；升维 warm 必须另按真实几何状态/新模型处理。

按现 `TailMixin` 的物理归一化，$H=\sigma qy_Z$，其原方程为
$$
B(y,p)=qR_Z(y,p)-\frac{P S_W(\iota\sigma qy_Z)}{\sqrt{E_c}}=0,
\quad
D_yB=qD_yR_Z-\frac{\sigma q}{\sqrt{E_c}}
P DS_W\iota\,\Pi_Z.
\tag{2}
$$
再除以原 `bcweights`，不改容差或增加方程。原临时 affine 内步也只使用
(1)的真实当前值与导数；外步/最终 residual 必须重新询问完整 W 尾。
有限差分 Jacobian 若仅近似 $DS_W$，投影接线不会将其升级成准确导数。

当前完整 `heightJetJacobian` 的行顺序是
`slope[W], second[W], meanSlope, meanSecond, height[W]`，尺寸
$(3W+2)\times W$。仅 slope 的前 $M$ 行、前 $M$ 列进入(2)。若旧代码
需要一个 $(3M+2)\times M$ view，行索引应取
`[0:M, W:W+M, 2W, 2W+1, 2W+2:2W+2+M]`，列取 `[:M]`。
该 view 只服务 prefix；原 W 响应、真实请求、全部尾状态和均值必须保留。

## 2. 高模式并没有因此满足接口

$\iota H$ 的高输入高度为0，不推出 $S_{W,>M}=Q_{W,>M}=0$。
数值实际 $H_W$ 也应按输出保留，不能从请求为0推它严格为0。
即使低模(2)通过，高坡度/二阶差仍存在。完整非线性发展还产生高的水平
Cartesian 模式与均值，不能只按高度向量的前 W 项判断全曲面接合。

因此 seam 记录保留全部 W 的 $H,S,Q$、$m_1,m_2$，且实际导出完整
Cartesian 的 $(X,X_r,X_{rr})$。R85 已说明形式 Darboux jet 不能自动替代
导出 XYZ 图的真实导数。后续接合取后者及其已有误差界。

## 3. 把全部两jet交给现有 common-cut

先做原反射、背景补回、刚体/均值配准，再用这张新图自己的 exact bridge。
记尾已配准 Cartesian 图为 $X$，$k=-1/\sqrt{E_c}$、
$k_2=-E_c'/(2E_c^2)$，$\lambda$ 为原 bridge 的经线重标量。
在其实际约定下，完整目标 prefix 两jet是
$$
J_0=X,\qquad J_1=\frac{k}{\lambda}X_r,\qquad
J_2=\frac{k^2X_{rr}+k_2X_r}{\lambda^2}.
\tag{3}
$$
取 $D_j=J_j-(\text{当前 prefix 第 }j\text{ 阶 jet})$，**对全部模式及均值**
使用原宽度 $\ell$ 的 Hermite 补偿。令 $t=(s-s_0)/\ell$，则
$$
\begin{aligned}
\Delta X={}&(10D_0-4\ell D_1+\tfrac12\ell^2D_2)t^3\\
&+(-15D_0+7\ell D_1-\ell^2D_2)t^4
+(6D_0-3\ell D_1+\tfrac12\ell^2D_2)t^5.
\end{aligned}
\tag{4}
$$
直接求导得左端零两jet、右端为 $(D_0,D_1,D_2)$，故它准确匹配所有已
提供的两jet；不论某模式是否属于低维 BVP。现
`78718-prefix-common-cut-storage-v1.py` 已按
$$
M_{\rm common}\ge\max\left\{M_{\rm prefix\ geometry},
\max_{k\in K_{\rm planar}}|(k-1)/3|,
\max_{k\in K_{\rm height}}k/3\right\}
\tag{5}
$$
扩基并对完整 endpoint/first/second 构造(4)。这通常不能简化为
$\max(M,W)$。完整 Fourier 输出/剩余尾仍按实际 exporter 范围处理。

## 4. 能得到什么、仍须实际支付什么

(1)–(2)是同一高模真实 DN 的限制及链式法则；(3)–(4)给完整 $C^2$
接合的代数接口。它们**不证明**高模残差足够小，也不证明补偿后 metric、
曲率、跨片 reach 或全时嵌入通过原门。必须用新 W 包的完整高模式和均值
计算(4)的实际影响，保留原 $g$ 与原补偿宽度；不可截掉高坡度，或增宽
窗口后把该更换当作同一几何的纯加密。

实际顺序可为：保留当前 M15真联解；在需要时只提高 W 的真实尾请求与
Jacobian，继续原低模 BVP；然后原生产链以完整 W 输出作 common-cut并
计算自有全域 metric/reach。这样有机会减少大 prefix 求解的内存，是否
达到原门取决于高模尾响应与接缝补偿的实际大小，本文不预支。

