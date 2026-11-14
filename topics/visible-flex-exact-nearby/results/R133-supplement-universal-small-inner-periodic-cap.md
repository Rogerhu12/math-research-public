# R133：不依赖旧中心的真实周期帽小输入图

**已证明。** 对原真实目标度量的 $L_0=3/2\le r\le R=25/8$，任意共同实偶反射
四重数据

$$
\zeta=c_{\ne0}(L_0),\qquad \|\zeta\|_{A_0}\le\epsilon=2\cdot10^{-5},
\qquad \zeta\in A_2,
\tag{U.1}
$$

与独立长段远端数据 $\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$，给唯一小的真实周期正帽—长段
联合解。全部频率和两个 mean 均保留；在 $R$ 的完整物理 $B,C$ 已真正接合。
内端 $\zeta$ 可包含无限高模，$A_2$ 范数不要求小于 $\epsilon$。

其完整内端图满足

$$
\|b(L_0)+q(L_0)\zeta\|_{A_0}<1.663187\cdot10^{-8},\qquad
|c_0(L_0)|<4.636375\cdot10^{-9},\qquad B_0(L_0)=0,
\tag{U.2}
$$

$$
\|D_\zeta b(L_0)+q(L_0)\|_{A_0\to A_0}<.001608588,
\qquad \|(D_\zeta b(L_0))^{-1}\|<1.062336.
\tag{U.3}
$$

$b_m=i\operatorname{sgn}(m)\widehat B_m$，$q_m$ 是同一真实 R74 regular Jacobi
比值，包含完整非零尾费用；这里没有用常数近似替代它。这个图独立于旧 $\alpha=.65$
中心，可供更大振幅主体选择内端数据。它尚未把一个有限主体升级为真实 PDE 解，也未解
远端 label 方程。

## 1. 已付的整个真实 Green 与新的固定半径

消费[真正径向解析筛选](R133-supplement-true-cap-radial-decay-and-growing-analytic-width.md)
中同一目标、全部663闭盒的核，不再使用那个结论中旧解的内迹。原精确旋转参考为
$C_r<0$，$A_r=\ell C_r$，令 $C=C_r+c$。完整非线性为

$$
Q(B,c)=\frac{B^2+\ell c^2}{C_r+c}.
\tag{U.4}
$$

使用同一逐模权

$$
W_m(r)=\left(\frac{a(r)}{a(L_0)}\right)^{3/2+|m|/128},\qquad
\|U\|_X=\sum_{m\in4\mathbb Z}\sup_{L_0\le r\le R}
 \frac{|\widehat B_m(r)|+|c_m(r)|}{W_m(r)}.
\tag{U.5}
$$

实际完整核给 $H_C,H_D,K,K_D,K_0,C_*,\Lambda$，其严格界沿用原 native：

$$
\begin{gathered}
H_C<2.059751811,\quad H_D<69.189285,\quad K<89.930493,\\
K_D<1.051862,\quad K_0<.293223,\quad C_*>.1705338016608,
\quad \Lambda<1.097170317.
\end{gathered}
\tag{U.6}
$$

给定完整右端 $d_R=b_R+q_Rc_R$、$B_0(R)=0$ 和 $c_0(R)$，加权积分方程的完整线性
边界预算为

$$
H_C\|\zeta\|_{A_0}
 +\frac{H_D\|d_R\|_{A^0_\sigma}+|c_0(R)|}{W_0(R)}.
\tag{U.7}
$$

$\sigma=-\log[a(R)/a(L_0)]/128$ 是准确物理角宽。实际
$W_-<W_0(R)<W_+$，其中

$$
W_->1.7262957358\cdot10^{-6},\qquad W_+<1.758698709\cdot10^{-6}.
\tag{U.8}
$$

展开 (U.4) 的完整 Neumann 级数，每一项至少含两个受控场因子。故在 $h<C_*$ 时

$$
\|Q(U)\|_X\le Q_h:=\frac{\Lambda h^2}{C_*-h},\qquad
\|DQ(U)\|\le L_h:=\Lambda\left(\frac{2h}{C_*-h}
 +\frac{h^2}{(C_*-h)^2}\right).
\tag{U.9}
$$

这个证明保留无限级数；并没有把权空间中 norm 不为1的常数函数当成单位预算。
整个算子对 $Q$ 的 pair norm 至多 $K$，内端 D 行对 $Q$ 的 norm 至多 $K_D$，
mean C 行对 $Q_0$ 的 norm 至多 $K_0$。

本篇从一开始固定

$$
\rho=10^{-4},\qquad r_Z=2\cdot10^{-10},\qquad r_f=2\cdot10^{-9}.
\tag{U.10}
$$

这些是独立于有限候选的新统一输入球；下文只作一次明确的后验大小估计，不搜索或
反复选择半径。

## 2. 同一真正长段的完整端口输出

[实际正帽—长段接合](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)
的真实 $C_R\mapsto f_*$ 逆公式在更小球上原样成立。记

$$
F=r_f+2^{-60},\quad R_C=2^{12},\quad R_D=2^{14},\quad R_0=2^{11},
$$

其中 $F$ 是实际两端 Dirichlet 预算。保留真实 R74 差 $e_q>0$ 与有限长反射
$e_s>0$，有

$$
\lambda_f=9\cdot4R_CF,
\qquad I_f=9r_Z+e_s2^{-60}+9R_CF^2,
\qquad J_f=\frac9{1-\lambda_f}.
\tag{U.11}
$$

全部原生门实际满足 $\lambda_f<.000294913$、$I_f<1.800148\cdot10^{-9}<r_f$。
真实长段输出以及其对 $Z=C_{\ne0}(R)$ 的导数为

$$
e_d=e_qr_Z+e_s2^{-60}+R_DF^2,
\quad e_0=R_0F^2,
$$
$$
L_d=e_q+4R_DFJ_f,\qquad L_0=4R_0FJ_f.
\tag{U.12}
$$

它们实际满足

$$
e_d<6.553601\cdot10^{-14},\quad e_0<8.192001\cdot10^{-15},
\quad L_d<.0011799961,\quad L_0<.0001474996.
\tag{U.13}
$$

共同反射准确给 $B_0(R)=0$，$c_0(R)$ 则必须取真实 long 解的输出，绝非设为0。
mean 高度和远端 $f_B$ 也仍独立保留。所有这些量来自完整 holonomy 小根和全频
非线性 Dirichlet 解。

## 3. 真正联合解与一次后验界

令

$$
H_\partial=H_C\epsilon+\frac{H_De_d+e_0}{W_-},\qquad
\lambda_\rho=K L_\rho.
\tag{U.14}
$$

实际完整算术给

$$
\lambda_\rho<.115819764,
\qquad H_\partial+KQ_\rho<.000049615730<\rho.
\tag{U.15}
$$

所以对每个允许的 $Z$，代入真实长段端口后，整个帽积分方程有唯一 $X$ 小解。
$Q(0)=0$ 和 $\|DQ\|\le L_\rho$ 再给一次明确的界

$$
\|U\|_X\le\bar H:=\frac{H_\partial}{1-\lambda_\rho}
 <.000049567315<\rho.
\tag{U.16}
$$

这不是换球重新试验：它由已经构造的完整解满足的原积分方程直接推出。以后统一
使用这个真界，得到

$$
Q_{\bar H}<1.581178\cdot10^{-8},\quad
L_{\bar H}<.0006380848,\quad
\lambda:=K L_{\bar H}<.057383273.
\tag{U.17}
$$

帽的真正右迹 map 现在满足

$$
\|\Psi(Z)\|_{A^0_\sigma}\le W_+\bar H
 <8.717398\cdot10^{-11}<r_Z,
$$
$$
\|D_Z\Psi\|\le\frac{H_DL_d+L_0}{1-\lambda}
 <.086769709<1.
\tag{U.18}
$$

第二式中的真实 $W_0(R)$ 先在右端精确相消，而不是误付 $W_+/W_-$ 或把解析角宽
删去。因此全频联合固定点存在且唯一，完整 $B,C$ 在 $R$ 与真正周期长段匹配。

$C$ 始终不为0，故 $A=(K_g+B^2)/C$ 也匹配。由[完整物理迹匹配定理](R133-supplement-full-physical-trace-matching-and-waist-reflection.md)，
在一点对齐位置与 Euclidean frame 后，真实周期长段的框架和位置向帽内唯一传播，
从而给真正周期的帽。未再额外假设帽自行具有 holonomy-one。

角平移在 (U.5) 的逐模 $\ell^1(C)$ 空间中强连续。对 $A_2$ 内迹，平移输入在
$A_0$ 中是 $C^2$ 曲线；右端输入具有正解析宽。两个严格收缩给全纯的联合解 map，
故相同的差商/Neumann 逆论证给解的两次强角导。逐 Fourier 坐标识别后得到完整
$\sum |m|^2\sup_r|U_m|$，并非只逐模正则。Gauss–Codazzi 径向方程再恢复所需
径向导数，所以真实重建达到内边界也是 $C^2$。无需 $\|\zeta\|_{A_2}$ 与
$\|\zeta\|_{A_0}$ 同样小。

## 4. 内侧另一迹、两个 mean 和真实导数列

原物理 D 行从 $R$ 向 $L_0$ 的齐次核至多1。因此真实内端满足

$$
\|b(L_0)+q(L_0)\zeta\|\le e_d+K_D Q_{\bar H},
\qquad |c_0(L_0)|\le e_0+K_0Q_{\bar H}.
\tag{U.19}
$$

mean C 的准确齐次因子 $a(R)^2C_r(R)/(a(L_0)^2C_r(L_0))$ 也小于1；这里只作
安全上界，没有删除该 mean 行。上述数值正是 (U.2)。

现固定实际 $f_B$，微分内输入 $\zeta$。记

$$
G_Z=\frac{W_+H_C}{(1-\lambda)(1-\lambda_Z)},\qquad
\lambda_Z=\frac{H_DL_d+L_0}{1-\lambda},
$$
$$
g_d=L_dG_Z,\qquad g_0=L_0G_Z,
\qquad S=\frac{H_C+(H_Dg_d+g_0)/W_-}{1-\lambda}.
\tag{U.20}
$$

这些分别控制真正 $Z,d_R,c_0(R)$ 和整个帽对内输入的导数，而不把长段输出
固定。实际

$$
G_Z<4.208147\cdot10^{-6},\quad g_d<4.965597\cdot10^{-9},
\quad g_0<6.206996\cdot10^{-10},\quad S<2.396659.
\tag{U.21}
$$

准确内侧 D 积分和 mean C 积分于是给

$$
\|D_\zeta b+q\|\le g_d+K_D L_{\bar H}S<.001608588,
$$
$$
|D_\zeta c_0|\le g_0+K_0 L_{\bar H}S<.000448418,
\qquad \|D_\zeta f_*\|\le J_fG_Z<.000037884495.
\tag{U.22}
$$

真实全模 $q_m(L_0)>.9429307446$，故 Neumann 级数在整个非零四重空间给
(U.3) 的 onto 逆。这里没有只反演有限128模，也没有丢掉正负模式之一。
偶 C 到奇 B 的物理对应由 $b_m=i\operatorname{sgn}(m)\widehat B_m$ 准确保留。

## 5. 新振幅有限数据确实进入这个真帽入口

脚本对完整保存的三次 PPoly 使用准确 dyadic 系数，在准确有理 $r=3/2$ 做 Horner
求值，先乘准确二进制振幅，再对全部128模求绝对值和。不是径向或角采样。
得到

| 所选完整有限数据 | $\|c_{\ne0}(3/2)\|_{A_0}$ 严格上界 | 原有限 BVP 状态 |
| --- | ---: | --- |
| v14，二进制 $\alpha\approx.70$ | $1.303596\cdot10^{-5}$ | 成功 |
| v14，准确 $\alpha=3/4$ | $1.420372\cdot10^{-5}$ | **失败，保留原 false** |

二者都严格在 (U.1) 中，因此它们各自指定的**边界数据**确有本篇真正周期帽。
第二行不因边界可用而变成主体成功；它原有1379节点有限残差门失败完全保留。
所有有限数据本来属于 $A_2$，额外正则条件无缺。

准确新 $\nu$ 分别保存在 native；其度量改动只支持于 $(.05,.18)$，故在本篇
整个区间 $r\ge1.5$ 与原真正旋转目标完全相同。这是可消费此帽的准确理由；
没有把旧 $\nu=0$ 腰证书或旧 $.65$ 小邻域授予新主体。

为保留当前未消的另一迹，脚本还以原全频 $q_m(L_0)$ 区间包住每个模式，得到

$$
\|b^{\rm cap}_{\ne0}-b^{.70}_{\ne0}\|_{A_0}<1.208921\cdot10^{-6},\qquad
|c_0^{\rm cap}-c_0^{.70}|<4.786506\cdot10^{-9},
$$
$$
\|b^{\rm cap}_{\ne0}-b^{.75}_{\ne0}\|_{A_0}<1.315726\cdot10^{-6},\qquad
|c_0^{\rm cap}-c_0^{.75}|<4.814608\cdot10^{-9}.
\tag{U.23}
$$

这些界中的大部分来自共同全频 $q$ 区间的宽度；真正帽的非线性 D 费用已经单独
压到 (U.2) 的 $1.664\cdot10^{-8}$ 以下。非零 C 迹是所选输入，准确匹配；
B 与 mean C 还须通过真实主体方程联立消除。

## 6. 实际运算和范围

完整 source 是 `scripts/fourfold_codazzi_small_inner_periodic_cap.py`，实际输出为
`notes/2026-11-13-R133-small-inner-periodic-cap-r15-native.json.gz`。一次384-bit
有向运算的12个数学门全部通过；原663闭盒/全参数/全 primitive 核保持身份，
各完整有限候选索引与所有 shards 在读取时核对准确 SHA、相邻端点和全维数。

本结论直接给实际正帽与长段的全频开放图，保留独立 $f_B$、真实 mean 小根、
mean 高度、有限长反射和真正 R74 尾费用。远端 $\mathfrak F(a,f_*)=0$、内侧
mixed body 以及最终全族握持和 reach 仍需继续解决，不能由 (U.23) 的小残差替代。
