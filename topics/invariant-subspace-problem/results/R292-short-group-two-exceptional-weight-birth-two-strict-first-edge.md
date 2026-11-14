# R292：两异常位四维首边：全部短普通组的真实 S2 与严格常数一

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下短组范围已证明。** 先证明旧“两普通组加一异常位”在 $\min(q,L)=2$ 时相对出生二的严格 S2，再与已证 S1 和真实旧下出生第二边合成加入第二异常位后的严格四维首边。最后保留全部组内重数，得到同范围的原物理出生二结论。$q,L\ge3$ 的 S2、一般相对出生和一般高度仍未关闭。

## 1. 不丢失非正交源度量的 S2 直接式

使用[出生二 S1 主稿](R288-appendix-two-group-singleton-birth-two-s1-positive-certificate.md)的实际共同源、完整五维／三维逆及记号：
$$
H_j=E_2^*\mathcal F_{2,j}^{-1}E_2,
\quad \Lambda_j=E_1^*\mathcal F_{1,j}^{-1}E_1,
\quad U_0=H_0,
$$
$$
K=\begin{pmatrix}2(z-1)&w-1\\0&z-1\end{pmatrix},
\qquad
\widehat H=E_{2,\rm phys}^*[d,d^*]E_{2,\rm phys}.
$$
$H_0,\Lambda_0$ 是真实物理源度量，未置为单位矩阵。旧上高度至少为一，所以只需要 $H_1$ 的本节在 $q=L=2$ 也合法。

真实两塔式
$$
d^*|_{K_2}=\mathcal J_{1,2}C_1-\mathcal J_{2,1}B
$$
的两项正交。取 Gram，得到
$P_{K_2}[d,d^*]|_{K_2}=C_1+B^*L_2B$。因此在当前非正交坐标中准确有
$$
\boxed{C_{\rm form}=\widehat H-K^*\Lambda_2K
=H_0H_1^{-1}H_0>0.}
\tag{1.1}
$$
这是真实完整首精度的形式；不能以粗压缩 $\widehat H$ 代替。

定义
$$
Y=H_0^{-1}K^*\Lambda_2,
\quad Z=K^*\Lambda_2\Lambda_3^{-1}\Lambda_2,
\quad R=C_{\rm form}Y+Z,
$$
$$
D_{\rm low}=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1.
\tag{1.2}
$$
R275 的实际混合系数在此坐标中为
$$
A=\frac12\left(H_1^{-1}K^*\Lambda_2
+H_0^{-1}K^*\Lambda_2\Lambda_3^{-1}\Lambda_2\right)
=\frac12H_0^{-1}R.
\tag{1.3}
$$
由 $H_1=H_0C_{\rm form}^{-1}H_0$，真实 S2 缺陷于是准确为
$$
\boxed{\mathcal D_{\mathrm{S2}}
=\Lambda_0-\Lambda_1\Lambda_2^{-1}\Lambda_1-A^*H_1A
=D_{\rm low}-\frac14R^*C_{\rm form}^{-1}R.}
\tag{1.4}
$$
所有非交换次序原样保留；特别 $\Lambda_2\Lambda_3^{-1}\Lambda_2$ 没有与 $K$ 或 $H_0$ 交换。

本稿直接对 (1.4) 给证书。以下两个更强的列估计虽然可用范数凸性合成 S2，但本稿不需要先证明它们：
$$
Y^*C_{\rm form}Y\preceq D_{\rm low},
\qquad Z^*C_{\rm form}^{-1}Z\preceq D_{\rm low}.
$$

## 2. 五个完整短侧参数区及精确证书

与[S1 短侧稿](R288-appendix-birth-two-s1-short-sides-hard-top-and-full-physical-layer.md)同样，交换普通组并整体缩放后取
$$
z=1+Z_0,\quad w=V,\qquad Z_0\ge0,V>0,
$$
$$
(q,L)=(2,2),(2,3),(3,2),(2,4+R_0),(4+R_0,2),
\qquad R_0\ge0.
\tag{2.1}
$$
源码中的变量名为 $Z,R$；这里加下标只为与 (1.2) 的矩阵 $Z,R$ 区别。两种长短方向均保留，故覆盖全部原正权比。

至多四阶的真实计数权在每个区中都有非负系数。所有完整核、$H_0,H_1,\Lambda_2,\Lambda_3$ 都在这些实参数域上严格正定；证明为基点的合法有限模型加上非负系数正半定项。式 (1.1) 是一般真实代数身份，故在同一个有理表达式域也成立，进而 $C_{\rm form}>0$。因此 (1.4) 的所有逆和分母均合法，约分后的分母在该连通域不变号。

[短侧生成器](../notes/2026-11-14-two-group-singleton-s2-short-sides-789f-next.py)调用冻结的[完整源／完整逆生成器](../notes/2026-11-14-two-group-singleton-bridge-certificates-789f-next.py)中的 `s2_direct_defect`，精确生成 (1.4)。所得两前导主子式的规范分子如下：

| $(q,L)$ | 一阶分子项数／次数 | 二阶分子项数／次数 | 负系数项 | 仅含 $V$ 的严格正项 |
|---|---:|---:|---:|---|
| $(2,2)$ | $186/26$ | $309/32$ | 两个均为零 | 两个均有 |
| $(2,3)$ | $277/34$ | $427/40$ | 两个均为零 | 两个均有 |
| $(3,2)$ | $302/34$ | $452/40$ | 两个均为零 | 两个均有 |
| $(2,4+R_0)$ | $4761/34$ | $8624/41$ | 两个均为零 | 两个均有 |
| $(4+R_0,2)$ | $9385/68$ | $16562/81$ | 两个均为零 | 两个均有 |

全部十个主子式在精确有理运算中通过，合计运行约三十二秒。实际项数、次数、规范分子哈希及通过状态由程序逐区自动写入[完整小型证书清单](../notes/2026-11-14-two-group-singleton-s2-short-sides-789f-next.json)。没有以有限数值模型代替这些全参数区。

每个分子系数非负，且 $R_0=Z_0=0,V>0$ 仍有严格正项。分母按一个内点定号，所以两前导主子式严格正。Sylvester 判据给
$$
\boxed{\mathcal D_{\mathrm{S2}}>0\quad
\text{对全部 }q,L\ge2,\ \min(q,L)=2,\ z,w>0.}
\tag{2.2}
$$
这里包含旧上高度只有一的 $q=L=2$；S2 从未请求一个上出生第二阶逆。冻结生成器的独立物理校准已核 (1.4) 与 (1.3) 构造的原式完全相同。

## 3. 加入任意第二异常位：真正四维首边

向上述旧模型加入一个任意正权 $v>0$ 的实际物理位。新固定相对出生二 primitive 空间的维数为四，完整出生层维数为八，满高度为 $q+L-2\ge2$。

旧下出生的第二边
$$
L_2L_3^{-1}L_2\prec L_1
\tag{3.1}
$$
由[两普通组加一异常位全出生全高度定理](R239-appendix-two-weight-groups-one-exceptional-all-births-all-heights-strict-bound.md)支付。它应用于真正旧下出生一；不是只引用其首边。

[S1 短侧及主稿](R288-appendix-birth-two-s1-short-sides-hard-top-and-full-physical-layer.md)已证明同一旧模型的 S1，(2.2) 给严格 S2。因此可在[R275 完整三块等价与无参数 SOS](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) §4 中逐项代入。

严格性也由该平方分解直接得到。严格 S2 与 $C_1,L_2>0$ 使 R275 (4.3) 的整个三块矩阵严格正定；新增位权平方 $t=v^2>0$ 时，其合同矩阵 $J_0(t)$ 可逆。R275 (4.4) 第一项遂严格正，第二项由 S1 和 (3.1) 非负，所以 $P(t)>0$。该稿原三块矩阵为 $M(t)=P(t)+W_tW_t^*$，因而也严格正；再沿其真实可逆合同和 Schur 等价反向恢复，得到
$$
\boxed{
H_1^{\rm new}(H_2^{\rm new})^{-1}H_1^{\rm new}
\prec H_0^{\rm new}.}
\tag{3.2}
$$
这里 $H_j^{\rm new}$ 是 R273 的同一个真实四维源下、先完整八维层逆后压缩得到的形式。它不是三个高度分别选择的源，也没有删除首端或末端硬约束。特别 $q=L=2$ 时，新高度恰为二；R275 使用旧真实 $C_2=0$ 硬端，仍给 (3.2)。

**固定块结论。** 对两个普通组 $q,L\ge2$ 且 $\min(q,L)=2$，两个异常权独立任意为正时，R273 整个相对出生二四维 primitive 源的首边具有严格常数一。

## 4. 原物理出生二的全部重数

令原普通组大小为 $Q_1,Q_2\ge2$ 且 $\min(Q_1,Q_2)=2$。先把第一个异常位视为旧模型。由[S1 整层合并](R288-appendix-birth-two-s1-short-sides-hard-top-and-full-physical-layer.md) §3，旧原物理 $K_2$ 的整个 S1 已付。

S2 沿同一对组内实际正交串分块。相对上出生二的块只有原组内出生 $(i,j)=(0,0)$，正由 (2.2) 支付；相对上出生一的块由[任意正权出生一 S2 收缩](R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)的严格余量 $1-2/3$ 支付；相对上出生零的块没有下出生源，所需三块矩阵只剩严格正的 $C_1$。全部块有同一原合法高度，且同时约化 $d,d^*,C,C^*$ 和各完整逆。

因此旧 S2 三块在整个实际空间严格正定。旧下出生第二边在整个 $K_1$ 已由 R239 支付。直接对整个旧空间使用 R275 的一步递推，新增第二任意异常位后，得到整个新物理 $K_2$ 上
$$
\boxed{\Gamma_1^{(2)}(\Gamma_2^{(2)})^{-1}\Gamma_1^{(2)}
\prec I_{K_2}.}
\tag{4.1}
$$
全部组内串及重数均保留；未把固定四维块等同于整个原物理 primitive 层。

本稿只关闭明确短组范围的首边。普通组均至少三的主四参数 S2、其他相对出生和内部高度保持原有缺口；本结论不直接给原连续尾的 graph Schur 返回源估计。

## 后继主参数范围

主q,L≥3的右列后来与左列一并完成；[全参数续稿](R292-appendix-main-parameter-s2-and-all-two-exceptional-birth-two-first-edges.md)将本短侧结论合入所有Q1,Q2≥2的整个物理出生二严格首边。其他出生/内部高度及原graph仍按各自接口保留。
