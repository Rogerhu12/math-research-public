# R137 补篇：直接有限缺陷的伴随细胞因子

2026-11-20，`visible-exact-astra-ac637-20261120 / joint_kernel`。

**已证明的条件性改进。** [连续到有限桥](R137-supplement-continuous-to-finite-principal-lift-bridge.md)的直接缺陷具有第二个原细胞长度因子。这个因子来自完整伴随输出的 cellwise Poincaré，不来自任意输入的径向导数。下文给出保留 193 个原子、原 normalizer 和完整 WJK 返回的实际导数公式。没有执行数值目标，也没有证明尚未取得的连续逆或严格有限门。

## 1. 同一有限桥与第二个投影

沿用前篇 (F.1)--(F.21)。特别是
$\mathscr Z=\mathscr H\oplus\mathbb R^{97}\oplus\mathbb R^{96}$，
$\mathscr H=L^2(I;E_L)$ 的变量为 $Sa$，$P_f$ 在 body 取原 normalized cell averages、在原子上为 identity。原网格仍为 $N=24480$，有限维数仍为 $4724833$；每个真长度是原 parent 真长度的 $1/160$。

记 $\iota:\mathscr H\to\mathscr Z$ 为零原子包含，定义**正交** body 投影
$$
Q=I-E_NE_N^*,\qquad
(\Lambda_h u)|_{I_i}=(h_i/\pi)u|_{I_i}.
\tag{D.1}
$$
它不同于前篇的斜投影 $Q_D=I-W_DP_f$。准确有
$$
Q_DHW_D=\iota Q\iota^*Q_DHW_D,
\qquad \|Q_DHW_D\|\le(6/5)M_{\rm mesh}.
\tag{D.2}
$$
这里 $M_{\rm mesh}\ge\|\Lambda_h S\mathcal R_cS^{-1}\|$ 是前篇的完整 ordinary-body 界，
$\mathcal R_c=(A_L-D_f)+C\mathcal F B$。接收端的 $\Lambda_h$ 不可穿过非局部返回。

假设 $T=(I-H)^{-1}$ 已按原完整对象取得。定义新的完整 receiver 目标
$$
\mu_Q=\|P_f(T-I)\iota Q\|.
\tag{D.3}
$$
有限缺陷本身仍是前篇的 signed composite；由 (D.2)，
$$
\boxed{\quad
\|\mathcal E_f\|=\|P_f(T-I)Q_DHW_D\|
\le(6/5)\mu_Q M_{\rm mesh}.
\quad}
\tag{D.4}
$$
这既未假设 $\|T-I\|$ 小，也未把 atoms 从输出删去。

## 2. 全部 finite/atomic 接收器的伴随 Poincaré

对 $z\in X_f$，令
$$
g_z=\iota^*(T-I)^*P_f^*z\in\mathscr H.
\tag{D.5}
$$
若 $g_z$ 在每个原细胞属于 $H^1$，并且某个完整算子界满足
$$
C_{\rm adj,h}\ge
\|z\longmapsto\Lambda_h\partial_r g_z\|_{X_f\to\mathscr H},
\tag{D.6}
$$
则向量值 mean-zero Poincaré 和 Hilbert 对偶性给
$$
\begin{split}
\|Qg_z\|^2
&\le\sum_i(h_i/\pi)^2\|(g_z)'\|_{L^2(I_i)}^2,\\
\boxed{\quad\mu_Q=\|Q\iota^*(T-I)^*P_f^*\|
&\le C_{\rm adj,h}.\quad}
\end{split}
\tag{D.7}
$$
这是第二个 $h_i/\pi$ 的来源。第一个因子在 (D.2) 的正向 source remainder 上；第二个在 (D.7) 的伴随接收方向上。二者不能被当作同一个径向乘子移动或合并穿过 Green 核。

$P_f^*$ 把 finite body 数据作 normalized constant lift，并保留全部 root97/outer96 原子。为避免分配四百多万列，可以把 (D.6) 的输入扩大为任意 $\mathscr Z$ 输入：$P_f^*$ 是 isometry，这只放宽算子界。ordinary source 核和 193 个端点 source columns 必须同时保留，不能仅计算 body-body 部分。

## 3. 完整中心的伴随方程给出所需正则性

写 $R_0=A_L-D_f$，令 $G_c$ 为
$$
\partial_r x-A_Lx-C\mathcal F Bx=f
\tag{D.8}
$$
在 R137 原低边界条件下的 ordinary-source inverse。完整 $T$ 的假设恰给此逆：由原 $G_D$ 的 resolvent identity，
$$
(T-I)\iota=\mathcal O G_c\mathcal R_cS^{-1}.
\tag{D.9}
$$
$\mathcal O$ 是前篇的同一 body-plus-atoms observation。它在 raw 解上读取 $Sx$、root odd96 加 mean、以及带原 $H^{-5/6}$ Riesz 权重的 outer even96。实际 root 条件仍是 even96 为零；outer 条件仍是 odd+$13/80$ even 和独立 mean 为零。

把 $P_f^*z=(z_B,z_a,z_R)$，其中 $z_B=E_Nz_{\rm body}$。令 $w$ 为 (D.8) 的完整 adjoint response，即
$$
-w'=A_L^*w+B^*v+S^*z_B,
\qquad v=\mathcal F^*C^*w.
\tag{D.10}
$$
原子不作为普通 $L^2$ source 或一个遗漏的 Dirac 项。它们准确规定 dual endpoint 条件：若 $E_a,E_R$ 是 $\mathcal O$ 的两 endpoint maps，则对满足原低齐次边界条件的每个 $x$，
$$
\langle w(R),x(R)\rangle-\langle w(a),x(a)\rangle
=\langle z_a,E_ax(a)\rangle+\langle z_R,E_Rx(R)\rangle.
\tag{D.11}
$$
这是原积分分部边界式，完整保留 root 的负号和 outer 的 Riesz factors。不能把它改成方便计算的零端点条件。

严格地，先由有界 $\mathcal O G_c$ 定义 $w$ 的 $L^2$ Riesz representative，再对紧支撑 $H^1$ 测试函数使用 (D.8)。因 $A_L,B,C,\mathcal F$ 在该固定有限返回上有界，弱式给 (D.10) 的 $w'\in L^2$，故 $w\in H^1$；此时 trace 和 (D.11) 才被合法取得。没有先向一般 $L^2$ 数据要求一个端点值。

由 (D.9) 得准确的 body adjoint
$$
\boxed{\quad g_z=S^{-*}(R_0^*w+B^*v).\quad}
\tag{D.12}
$$
尤其 $T-I$ 对纯原子输入为零这一事实，没有使 (D.10)--(D.12) 中的原子**接收** source 消失。

## 4. 原 WJK 返回的有限状态公式使导数可计算

这里只使用 [R137](R137-continuous-signed-centre-and-exact-endpoint-system.md) (S.6)--(S.9) 的准确 returned $K_0\to K_0$ composite。其六个辅助状态共 1024 维，可完整写成
$$
\xi'=M\xi+Nf,\qquad \mathcal Ff=E\xi.
\tag{D.13}
$$
这不是新近似。$M,N,E$ 是 (S.7)--(S.9) 的全部 signed coefficient blocks，含 $\chi,\psi,\chi',\psi'$、两个原 reference Green 条件、两个左零 primitive、两个右零 primitive，及真实右端 $R$。输出没有 $f$ 的直接直通项。这里 $E$ 是本节状态输出矩阵，不是 finite projection 或原误差矩阵。

记 $\mathcal L_M=\partial_r-M$，域为这六状态的原齐次端点条件。对 $v=\mathcal F^*C^*w$，准确令
$$
\widehat\xi=\mathcal L_M^{-*}E^*C^*w,
\qquad -\widehat\xi'=M^*\widehat\xi+E^*C^*w,
\qquad v=N^*\widehat\xi.
\tag{D.14}
$$
全部 dual state endpoint 条件由 $\mathcal L_M^*$ 继承；尤其右 primitive 不能被截到 collar 的右端。$\widehat\xi\in H^1$，而 $N$ 在每个原细胞为 $W^{1,\infty}$。于是 (D.12) 逐细胞的**完整**导数为
$$
\begin{split}
g_z'=S_i^{-*}\{& (R_0')^*w+R_0^*w'
 +(B')^*N^*\widehat\xi\\
 &+B^*[(N')^*\widehat\xi+N^*\widehat\xi']\},\\
w'&=-A_L^*w-B^*N^*\widehat\xi-S_i^*z_B,\\
\widehat\xi'&=-M^*\widehat\xi-E^*C^*w.
\end{split}
\tag{D.15}
$$
它只需要完整的 signed coefficient products、真实 $A_L',B',N'$、以及同一带 boundary source 的 $w,\widehat\xi$。没有 $z_B'$，没有对保存过的 scalar upper 求导，也不需要 $C'$ 或 $M'$。若先乘 signed blocks 再取 norm，可以保留与 $R_0$ 和 $B$ 相关的抵消。

这里的 broken $H^1$ 资格不能略过。$S_i,D_i$ 的全部真正跳点是原 fine mesh 的端点；硬 collar indicator 的跳点是原第一个 parent 的右端 $c$，也是该网格端点。cutoff 在自己的过渡区是连续分片多项式。Qrepair 及其角导在原 cubic 接口连续，径向导允许有跳，因此有限 $A_L,B$ 在跨这些接口的细胞内仍为 $W^{1,\infty}$。各 raw auxiliary state 连续。它们共同证明 (D.15) 在每个原细胞属于 $L^2$。若另一个实现添加了细胞内部真跳，必须单独付其完整 jump 项或重建相应有限桥；不能无费用使用 (D.7)。

## 5. 可复用 low Green 的较小充分计算

若先取得同一 $A_L$ 的完整 low inverse $G_A$，可复用 R141 的 ordinary source/193 endpoint columns。令
$$
K=\mathcal O G_A C\mathcal F BS^{-1}\operatorname{pr}_{B}
=\begin{pmatrix}K_B&0\\K_A&0\end{pmatrix},
\qquad
\mathcal A_Q=\mathcal O G_A\mathcal R_cS^{-1}Q
=\binom{A_B}{A_A}.
\tag{D.16}
$$
$A$ 下标在此表示全部 193 atoms。若完整新界满足
$\|K_B\|\le\tau_B<1$、$\|K_A\|\le\tau_A$、
$\|A_B\|\le\mu_B$、$\|A_A\|\le\mu_A$，则精确 resolvent 分块给
$$
(T-I)\iota Q=
\binom{(I-K_B)^{-1}A_B}
{A_A+K_A(I-K_B)^{-1}A_B},
$$
$$
\mu_Q\le
\left\{\left(\frac{\mu_B}{1-\tau_B}\right)^2+
\left(\mu_A+\frac{\tau_A\mu_B}{1-\tau_B}\right)^2\right\}^{1/2}.
\tag{D.17}
$$
所以收缩只施加于 ordinary-body feedback；原子反馈的范数只作为输出费用。$\mu_B,\mu_A$ 各可由 (D.7) 计算，采用 $G_A^*$ 的 source/atom response 后，(D.15) 中 $w'=-A_L^*w-S_i^*z_B$，其余完整 $\mathcal F^*$ 项不变。仍须保留各 signed 源积，而非用无关旧正上界作减法。

这是一个具体复用入口：全低 Green 的两三角与 endpoint columns、完整返回的 finite coefficient blocks、原 $h_i$ 的接收权。它不需要构造 $4724833$ 维矩阵；它也不保证新的 $\tau_B$ 或 (D.4) 会小于一。直接完整伴随实现 (D.10)--(D.15) 不要求另外采用 (D.17) 的收缩路线。

## 6. 正规化、真实 high inverse 和未付门

若最后保存的上界确实给
$\eta_f=(6/5)C_{\rm adj,h}M_{\rm mesh}<1$，前篇 (F.24)--(F.27) 原样给
$$
\|(I-E_c)^{-1}\|
\le\frac{75}{58}\frac{\|T\|}{1-\eta_f}.
\tag{D.18}
$$
其中 normalizer $I-J_\rho$ 的完整旧 $e_\rho$ 球只读引用前篇 §6；没有重算、删除或免费换 reference。有限 trial 的 identity atoms 和上述伴随 boundary atoms 是不同位置的两件事，两者都已保留。

本篇的 $\mathcal F$ 始终是旧 WJK trial-and-dual 返回，**不是**真实 $G_H$。若正在构造 $A_L+C G_HB$ 的直接实际高频消元，(D.1)--(D.12) 可对其重新定义的完整 $\mathcal R,H,T,F_c$ 使用，但那不自动成为旧 WJK 的有限因子。返回旧因子时必须完整支付 $C(\mathcal F-G_H)B$，连同 ordinary/atomic 接收器与其参数域。真实高返回的伴随正则性应使用 [WPT](R133-supplement-cellwise-principal-inverses-and-dual-radial-head-tail.md) (WPT.15)--(WPT.19) 的真实 source equation、七个原 high ports 与真实 dual 边界；不能把未知无限高解截到旧 1024 状态。

$A_L$ 在本篇仍是 same-actual-$\eta$ hybrid，不能无偿赋予它真正 $DF(Q_{\rm repair})$ 的几何能量。实际 family 差、原外部行、affine/mean、高 stable 条件，以及前篇 (F.28) 的 actual Schur remainder 仍须完成。两个原右侧的恢复保持前篇 (F.29)，第二行不设零。本文只新增了一个可消费的严格缺陷估计，没有把连续逆或上述完整门宣布为已算。
