# R791 方法：原 Hom 的 Galois 作用、真实极化尺度与 η 的加法除子输入

日期：2026-11-15。状态：**下述公式与有限算法已证明；本文件不是新计算成功报告。**
运行 `R791_original_Hom_galois_and_eta_inputs.py` 后才能登记具体矩阵、次数和
原 index 4 的 CM 切向非零性。本文不声称已经求出极除子、任何 $\eta_h$ 的
Jacobian 坐标、$\ker\eta$ 中的非零元或高度首项。

## 1. 完全固定原输入，先解决实下降

保留 R593/R724 的 $X=X_1$、$Y=W_{41}$、$\phi:X\to Y$、
$q:J_X\to A=A_{\theta,1}$、原极化 $\lambda_A$、原 $c_0,c_1$，以及

$$
\kappa=qq^\dagger,\qquad
F=\operatorname{End}_{\mathbf Q}^0(A),\qquad
F^0=\{h:\operatorname{Tr}_{F/\mathbf Q}(\kappa h)=0\}.
\tag{791.1}
$$

原目标为 $C/L:y^2=x^3+b$，$K=\mathbf Q(\zeta)$、$L=K(b)$、
$L^+=\mathbf Q(b)$，$[L:K]=7$。R745 的六个 $\omega_j$ 是
原 $q^*H^0(A,\Omega^1)$ 的 **$\mathbf Q$ 定义**基。
R759 的完整整数 Hom 格 $\mathcal H$ 的原列基记为
$f_0,\ldots,f_{11}$；这里每个 $f_i(c_0)=O$，其微分为
$\sum_jv_{ij}\omega_j$。本文的已选原函数是
$f=f_4$、$\deg f=1206$，不另选短向量。

从 $L$ 定义不能直接推出 $L^+$ 定义。令 $c$ 为复共轭，固定 $b$，
在实际微分系数中有

$$
c(a(b)+d(b)\zeta)=a(b)-d(b)-d(b)\zeta.
\tag{791.2}
$$

基点 $c_0$ 是原 $a=0$ 的唯一有限 deck 固定点，定义在
$\mathbf Q$ 上；所以微分相同且在 $c_0$ 为零的唯一性同时识别实际
映射的复共轭。若 $c(f)=f$，直接取 $f_R=f$。否则使用实际整数群和

$$
f+c(f),\qquad [\zeta]f+[\zeta^2]c(f).
\tag{791.3}
$$

二者均被 $c$ 固定，且不可能同时为零：第一式为零时第二式是
$[\zeta-\zeta^2]f\ne0$。程序在非零候选中按原次数取最小者，
保留群和 recipe、原十二维整数坐标及次数。它不除掉任何整数公因子，
也不把新映射的次数继续写成 1206。

于是 $f_R:X_{L^+}\to C$ 是一个真实非零映射。Weil restriction 的
伴随性给 $\mathbf Q$ 同态

$$
q_R:J_X\longrightarrow B=\operatorname{Res}_{L^+/\mathbf Q}C.
\tag{791.4}
$$

R728 给 $B\sim A_{42}\times A_6$，维数分别为 6 和 1，且每块一次。
每个共轭微分仍在原 $A$ 的 Hodge 空间，故
$q_R=vq$，其中 $v:A\to B$ 是实际有理同态。
原 $A$ 在 $\mathbf Q$ 上单，且 $A\sim A_{42}$ 与 $A_6$ 不同源；
所以 $v$ 的像恰为六维本原因子，且 $v:A\to A_{42}^{\mathrm{mod}}$
是有理同态范畴中的同源。没有借用剩余椭圆因子形成虚假的
$\eta$ 核，也没有假设 $v$ 的整同源次数在 41 处为单位。

## 2. 原 γ 的作用是 21 阶，不是 42 阶

直接读取 R754 已完成的 `R754-gamma-descent.json.gz`。原
$\gamma=7+30\zeta$ 给 $\sigma=\sigma_\gamma$ 及
$\rho=\sigma(r)/r\in L$。原成功计算已经证明

$$
\rho^6=\sigma(b)/b,\qquad \sigma^7=1,\qquad
\prod_{i=0}^6\sigma^i(\rho)=\zeta^2.
\tag{791.5}
$$

令 $D_u(x,y)=(u^2x,u^3y)$。在 $\mathcal H$ 上定义

$$
\mathcal T(f)=D_{\rho^{-1}}\,\sigma(f).
\tag{791.6}
$$

因为 $D_{\rho^{-1}}^*(dx/(2y))=\rho\,dx/(2y)$，且
$\omega_j$ 都定义在 $\mathbf Q$，原微分坐标的准确作用是

$$
(v_0,\ldots,v_5)\longmapsto
 (\rho\sigma(v_0),\ldots,\rho\sigma(v_5)).
\tag{791.7}
$$

这不是 R728 (728.17) 的 Weil 余切 trace 坐标；两者的指标次序不同，
不应把该式的 $\sigma^{-1}$ 直接移植到 (791.7)。
R728 的真实移位构造对本次原 $\gamma$ 给

$$
\mathcal T^7=[\zeta^2],\quad \mathcal T^{21}=1,
\quad c\mathcal Tc=\mathcal T^{-1}.
\tag{791.8}
$$

这里正 CM 约定为 $[u]=D_{u^{-1}}$。
原 $\gamma$ 是范数一元，其射影作用的阶为 21；本次不替换
$\gamma$ 以凑出 R728 全生成元的 42 阶。

在 $B$ 上，完整多项式为 $U^{14}+U^7+1=\Phi_3(U)\Phi_{21}(U)$。
原本原因子对应 $\Phi_{21}$；$A_6$ 对应 $\Phi_3$。
因此

$$
F=\mathbf Q(\zeta_{42}+\zeta_{42}^{-1})
 =\mathbf Q(\zeta_{21}+\zeta_{21}^{-1}),
$$
$$
\Psi_{21}(Z)=Z^6-Z^5-6Z^4+6Z^3+8Z^2-8Z+1.
\tag{791.9}
$$

设 $T$ 是 (791.6) 在原十二维列基中的矩阵，$J$ 是原 $[\zeta]$
矩阵，$R$ 是复共轭矩阵，$G$ 是 R759 的 **两倍次数** Gram。
程序不重新计算周期、格或 Gram。它在六个 $L$ 坐标，即 84 个
$\mathbf Q$ 坐标中求解 (791.7)、(791.2)，并完整代回。由真实映射
和原完整格，所得作用必须整且幺模，且准确满足

$$
T^7=J^2,\quad T^{21}=I,\quad R^2=I,\quad RTR=T^{-1},
\quad RJR=J^2,\quad TJ=JT,
$$
$$
T^tGT=R^tGR=J^tGJ=G.
\tag{791.10}
$$

还验证 $\Phi_{21}(T)=0$、$\Psi_{21}(T+T^{-1})=0$、
$\operatorname{rank}(I\pm R)=6$，及

$$
I,\quad T^j+T^{-j}\ (1\le j\le5)
\tag{791.11}
$$

的线性独立性。它们在本原因子上给整个真实 $F$ 的基。
一个非零实 Hom 向量的该轨道也必须为六维；程序直接验证这项。
一般 $p$ 可用 R728 的全生成元证明相同结构，但不能将本次
“42 与 21 的实圆分域相同”推广到 $4\mid p+1$。

## 3. 由原次数 Gram 恢复实际 Hermitian 配对

本节给出真实尺度输入，而不把 $v^\dagger v$ 任意设为一。
所有 adjoint 均使用 Jacobian 和椭圆的原主极化；$B$ 使用 R728
逐分量椭圆极化下降所得的 $\lambda_B$。

对实际整数映射 $u,w:J_X\to C$，令

$$
H(u,w)=uw^\dagger\in\operatorname{End}_L(C)=\mathbf Z[\zeta].
$$

写 $H=\alpha+\beta\zeta$。加法映射的次数恒等式给

$$
a=u^tGw=\operatorname{Tr}_{K/\mathbf Q}H=2\alpha-\beta,
\qquad
b=u^tGJw=\operatorname{Tr}_{K/\mathbf Q}(\zeta^2H)=-\alpha+2\beta.
$$

故

$$
\boxed{H(u,w)=\frac{2a+b}{3}+\frac{a+2b}{3}\zeta.}
\tag{791.12}
$$

这里 $b$ 的 $J$ 在第二变量上；若放错一侧，复共轭会反向。
两系数为整数，因为 $uw^\dagger$ 是实际整数椭圆自同态。
程序逐列检查整性，未以数值拟合取整。

令 $w$ 是所选 $f_R$ 的原整数坐标，$w_i=T^iw$，$0\le i<7$。
把 $B_L$ 的第 $\sigma^i$ 分量通过 $D_{\rho_i^{-1}}$
运输到 $C$，其中 $\rho_i=\prod_{r<i}\sigma^r\rho$；这都是保极化
同构。于是

$$
q_R^\dagger q_R=\sum_{i=0}^6 w_i^\dagger w_i.
\tag{791.13}
$$

右端对任意 $u$ 的预合作用是
$u\mapsto\sum_iH(u,w_i)w_i$，故准确的十二维矩阵为

$$
E=\sum_{i=0}^6\left[
 w_i\frac{2w_i^tG+(Jw_i)^tG}{3}
 +(Jw_i)\frac{w_i^tG+2(Jw_i)^tG}{3}\right].
\tag{791.14}
$$

令 $M_v=\lambda_A^{-1}v^\vee\lambda_Bv=v^\dagger v\in F$。
由 $q_R=vq$，(791.13) 等于 $q^\dagger M_vq$。
在原 Hom 空间预合作用正对应 $\kappa M_v$。所以 **$E$ 是
原 $\kappa v^\dagger v$ 的准确矩阵**，不是未经记录的比例。
程序验证 $E$ 非奇异、$E^tG=GE$，与 $T,J,R$ 交换，并在
(791.11) 中准确展开。

设 $d=\deg f_R$、$d_0=7d$。标准迹/次数公式或 (791.14) 的逐项
迹直接给

$$
\operatorname{tr}_{\mathbf Q^{12}}E=2d_0.
\tag{791.15}
$$

这完整保留 R593 的 $\kappa$；若后继要把 $M_v$ 单独写成原
$F$ 元素，仍须用原 $\kappa^{-1}$，不能由此设 $\kappa=1$。

## 4. 原 $F^0$ 的全部五个方向与准确次数

在 $B_L$ 的原分量上设

$$
\Theta_B=\sum_\tau\operatorname{pr}_\tau^*[O],\quad
D_0=f_B^*\Theta_B=\sum_\tau f_{R,\tau}^*[O],
$$
$$
D_j=((1+\mathcal T^j)f_B)^*\Theta_B-2D_0
\qquad(1\le j\le5),
\tag{791.16}
$$

其中 $f_B=q_R\circ[x-c_0]$。
$\mathcal T$ 保持 $\Theta_B$ 这个实际分量除子。
定理平方（亦可直接拉回 Poincaré 双扩张）给

$$
\lambda_{(1+\mathcal T^j)^*\Theta_B-2\Theta_B}
 =\lambda_B(\mathcal T^j+\mathcal T^{-j}).
\tag{791.17}
$$

因此是 **加法** 映射，且右端没有额外 $1/2$。
$j=0$ 使用 $D_0$，不把它误认成 $\mathcal T^0+\mathcal T^{-0}=2$。
由于
$\mathcal T^{-j}(1+\mathcal T^j)=1+\mathcal T^{-j}$，有
$D_{-j}=D_j$，作为实际除子成立。复共轭送 $j$ 到 $-j$，其余
Galois 元素置换分量，故 $D_j$ 都在 $\mathbf Q$ 上定义。

次数可直接由旧 Hom Gram 求出：

$$
\deg(f_R+\mathcal T^jf_R)
 =\tfrac12(w+T^jw)^tG(w+T^jw),
$$
$$
d_j:=\deg D_j
 =7\bigl(\deg(f_R+\mathcal T^jf_R)-2d\bigr).
\tag{791.18}
$$

令 $\vartheta:F\xrightarrow{\sim}\operatorname{End}_{\mathbf Q}^0(A_{42}^{\rm mod})$
由实际 $v$ 共轭给出，$s_j=\mathcal T^j+\mathcal T^{-j}$。
原 $F$ 中的元素

$$
h_j=M_v\vartheta^{-1}\left(s_j-\frac{d_j}{d_0}\right),
\qquad1\le j\le5,
\tag{791.19}
$$

满足

$$
j_A^*\mathcal L_{h_j}
 =\left[D_j-\frac{d_j}{d_0}D_0\right]
 \quad\text{于 }\operatorname{Pic}(X)\otimes\mathbf Q.
\tag{791.20}
$$

证明此处线丛相同需要保留 Picard 项：两者都是原点刚性化的对称
线丛，且 (791.17) 给相同的 $\lambda$；它们的 Picard 零次差至多
二挠，故在 $\operatorname{Pic}\otimes\mathbf Q$ 中为零。
拉回沿原 $c_0$ 的 Abel 映射，不另作平移。

$1,s_1,\ldots,s_5$ 是本原 $F$ 的基，$d_0>0$，而 $M_v$ 可逆。
因此 (791.19) 恰是原 $F^0$ 的一组基，涵盖全部五个方向。
这不是仅凭 $\dim B=7$ 的猜测：使用了完整同源类识别、实际
非零 $\mathbf Q$ 同态 $v$、本原域作用与原拉回次数。

在原十二维 Hom 空间上，$\kappa h_j$ 的矩阵准确为

$$
E\left(T^j+T^{-j}-\frac{d_j}{d_0}I\right).
\tag{791.21}
$$

为核矩阵作用的方向，在上述统一的 $C$ 分量中直接有
$q_R^\dagger\mathcal T^j q_R=\sum_{i=0}^6w_i^\dagger w_{i+j}$，
其中 $w_{i+j}=T^{i+j}w$，绕回时保留 $T^7=J^2$。
预合作用因而为 $u\mapsto\sum_iH(u,w_i)w_{i+j}=T^jEu$。
再加 $-j$ 项并用 $ET=TE$，正好得到 (791.21)，不凭
“同一维数”辨认同态，也不遗漏绕回的 CM 单位。

程序生成这五个矩阵，验证迹为零、Rosati 自伴及秩五。
原 $q,\alpha,c_0,c_1$ 和实际 $\kappa$ 都没有更换。
式 (791.19) 不宣称其中任何一个 $h_j$ 属于 $\ker\eta$。

## 5. 真正的 η 由商上极除子给出，因子 1/3 保留

每个以上实际映射 $g:X_L\to C_\tau$ 均满足
$g\delta=[\zeta]g$，且 $g(c_0)=O$。R762 的证明适用于它们的
整数群和与 Galois 运输。故 $y\circ g=\phi^*y_g$，其中
$y_g\in L(Y)$。
因为椭圆上的 $y$ 在 $O$ 处极点阶为三，

$$
\phi^*(y_g)_\infty=3g^*[O].
$$

推前并使用 $\phi_*\phi^*=3$，得到准确等式

$$
\boxed{\phi_*g^*[O]=(y_g)_\infty,\qquad
\deg(y_g)_\infty=\deg g.}
\tag{791.22}
$$

在 branch 点上也成立；不能凭集合像把重数三删掉。
记 $P_g=(y_g)_\infty$。由原 R593 定义
$\eta_h=\frac13\phi_*j_A^*\mathcal L_h$，有

$$
\boxed{
\eta_{h_j}=\frac13\left[
\sum_\tau P_{\,f_{R,\tau}+(\mathcal T^jf_B)_\tau}
-\left(2+\frac{d_j}{d_0}\right)\sum_\tau P_{f_{R,\tau}}
\right].}
\tag{791.23}
$$

该有理除子的次数由 (791.18) 严格为零，且 Galois 不变；
这是原 $J_Y(\mathbf Q)\otimes\mathbf Q$ 中的 $\eta$，包括
原 Picard 修正，不能把 $\phi_*/3$ 的三或 $d_j/d_0$ 约成未知标度。

R787 的原 $y=A/B$ 可作为这些函数的起点：复共轭与
$\sigma$ 作用于原 $L$ 系数，$D_{\rho_j^{-1}}$ 使 $y$ 乘
$\rho_j^{-3}$，实下降和剩余加法使用原椭圆群律。
无需另外选择 $x$ 的立方根相位。具体地，R772 的准确恒等式

$$
x=3(y^2-b)h/dy
\tag{791.24}
$$

使用原微分 $h=f^*dx/(2y)$。两个同靶映射
$P=(x,u)$、$Q=(rx,v)$ 的 $x$ 比 $r$ 是 $Y$ 上的函数，可由
(791.24) 之比求出。当 $r\ne1$ 作为函数时，

$$
y(P+Q)=-u+\frac{(v-u)(2+r)}{r-1}
 -\frac{(v-u)^3}{(r-1)^3(u^2-b)}.
\tag{791.25}
$$

这是普通割线加法逐项化简的恒等式；$r=1$ 时使用完整群律的
倍点或反点分支。孤立点的分母零必须在函数域中正规化，不能把
未约分的分母零除子直接当成 $P_g$。

**实际仍缺的步骤。** R787 只给原 $y$ 的准确模形式分式；它没有
生成 $Y$ 的函数域/除子实现。R791 的矩阵运行只给 (791.23) 的
真实同态、次数和规范系数。要得到实际 $\eta$，仍须在一个准确的
函数域或 Riemann–Roch 除子表示中实施上述函数运算并计算完整
极除子，再做 Jacobian 群运算。这一界面未实现时，不将 recipe
登记为已计算的除子或 $\eta$ 值。

## 6. 原 CM 点的十二个实际切向系数

R748 的真实成功证书绑定 R745 原六微分，并明确记录
`c1 slash once`。在原粗坐标 $s=a-1$ 下，

$$
(t_0,\ldots,t_5)=
\left(\frac{43719}{11767},\frac{200187}{23534},
\frac{162558}{11767},\frac{687471}{23534},
\frac{659397}{11767},\frac{2521233}{23534}\right)
\tag{791.26}
$$

恰为 $\omega_j/ds$ 在原 $c_1$ 的值。对原十二个映射的实际值为

$$
\left.\frac{f_i^*(dx/(2y))}{ds}\right|_{c_1}
 =\sum_{j=0}^5v_{ij}t_j\in L.
\tag{791.27}
$$

程序先读 R748 原证书并核其 Hodge SHA、基名和相位，再于原
$\mathbf Q[b,\zeta]$ 中精确收缩。输出全部坐标与逐项零标志，
特别保留原 index 4。**不额外乘 $\zeta^2$，不把 $H^3$ 的立方根
当成原 $h$。**

若原 index 4 的 (791.27) 非零，则该原 $f$ 在 $c_1$ 不分歧。
若之后 R790 求得有限 $y(c_1)$ 且 $y(c_1)^2\ne b$，
由 $dy=3x^2h$ 可知 $y'(c_1)\ne0$，于是 (791.24) 只需原
$y$ 的一阶导即可恢复 $x(c_1)$。若 $y(c_1)^2=b$，则
$x(c_1)=0$；若 $y$ 在此有极点，则像为 $O$。
本次切向非零判定不代替这些待求函数值。

## 7. 实际输入、输出与禁止重算的边界

新算术全部由公开仓库 Actions 执行。直接输入为：

| 既有产物 | 来源与 SHA-256 |
|---|---|
| R754 原 γ 下降 | run 43620862489；cf37105d407ace9df6b86a80d112b58915202bfecfc9e2fd118f4be76af2b1d0 |
| R759 原十二映射、Gram、ζ 作用 | run 43625474728；037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc |
| 原 $b$ 模型证书 | run 43608152850；752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574 |
| R748 原六切向系数证书 | run 43617493590；56418d0cef84554584d8777aed4acb54a2dc57bbf95cc38a1bb42b12140769f3 |

runner 核生产 run/source、artifact digest、完整 manifest 以及每份
输入 SHA。只下载既有阶段；不重新运行 Miller、周期、完整 Hom 核、
HNF 或 LLL。核心直接复用 R754 原七次域的精确运算类，核其源 SHA。
新输出只在后继仍需使用期间保留 Actions 临时 artifact；仓库和
Release 不保存可重算矩阵或证书。成功结论另记录实际 run、脚本/
参数 SHA 及输出 SHA，不预填成功值。

依据：R593 (593R.6)–(593R.11)，R724 §§1–4，R728 §§1–5，
R745 §§1、3，R748 (748.9)、(748.44)，R754 原阶段与 R759 完整格，
R762 的原基点/μ3 等变性，R772 (772.18)，以及 R787 的原函数 recipe。
