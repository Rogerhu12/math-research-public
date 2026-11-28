# R267 附录：有理根近似的同一分子、实际分母与奇数切口收缩

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：下列同源恒等式、全部原旗范围与奇数切口估计已证明。** 继续使用[相容有理根稿](R267-appendix-coherent-bounded-rational-roots-of-one-flat-common-denominator.md)的同一个 $C,P_r,U_n,Z_n,M_n,d_n,T_{r,N}$，不另换分母构造。本文把其中原平方近似化为固定有界分子 $P_t$ 的实际分母问题；尚未证明所需分母列强收敛。

## 1. 固定同一分子后的实际分母

固定正有理数 $t$。记
$$
\delta_N=\frac1{2M_N},\qquad
V_N=\prod_{\nu<N}U_\nu(C)^{d_\nu/(2M_N)},\qquad
D_N=T_{1/M_N,N},\qquad
Y_N=P_{\delta_N}V_N^{-1}.
\tag{1}
$$
已付 $Y_N^2=CD_N$、$\|D_N\|\le1$、$D_N\to I$ 强*。所有 $Y_N,V_N$ 互相交换；$V_N$ 是原范数多项式代数内的可逆元。每个固定 $Y_N$ 有界，未付一致范数。

对 $\delta_N<t$ 定义
$$
Q_N=P_{t-\delta_N}V_N,\qquad
Z_t=C^{-1}P_{2t}.
\tag{2}
$$
$C^{-1}P_{2t}$ 指前稿已构造的实际全域有界来源 $R_{2t,1}$。因此 $Q_N,Z_t$ 都是实际有界交换子，属于共同幂理想，并在所有原有限放大闭不变旗子商上单射、像稠密。这里使用的是前稿的具体强单位，而非由非零或平坦性推出范围。

同族乘法立即给
$$
\boxed{
Y_NQ_N=P_t,\qquad
D_NQ_N^2=Z_t,\qquad
Y_NP_t=CD_NQ_N.
}
\tag{3}
$$
第二式先由第一式平方及 $Y_N^2=CD_N$ 得
$CD_NQ_N^2=P_{2t}=CZ_t$，再用原 $C$ 单射消去。所有等式都在全 $H$ 上成立，也下降到同一个原旗子商。

## 2. 任意两切口的精确比值

若 $M>N$ 且 $\delta_N<t$，置
$$
R_{NM}=P_{\delta_N-\delta_M}V_N^{-1}V_M.
\tag{4}
$$
它是实际有界平坦交换子，同样在全部原旗上单射、像稠密。不能预设其范数不超过一。精确乘法给
$$
\boxed{
Q_M=Q_NR_{NM},\qquad
Y_N=Y_MR_{NM},\qquad
D_N=D_MR_{NM}^2.
}
\tag{5}
$$
前两式直接相加 $P_r$ 的参数。第三式将第二式平方后消去单射 $C$。对 $N<M<L$ 还有同一来源的乘积相容式
$$
R_{NL}=R_{NM}R_{ML}.
\tag{6}
$$

## 3. 奇数倍切口的完整收缩与柱误差

令整数 $L=M_M/M_N$ 为奇数。则
$r=\delta_N-\delta_M$ 满足
$rM_M=(L-1)/2\in\mathbb N$，因而可在第 $M$ 切口合法使用前稿的 $P_r$ 公式。

把 (4) 中的三个有限解析单位前缀全部合并，$\nu<N$ 的指数恰好消失；$N\le\nu<M$ 的指数变成 $d_\nu/(2M_N)$。又
$$
\sum_{\nu=N}^{M-1}\frac{d_\nu}{2M_N}=\frac{L-1}{2}.
$$
因为整段乘数均为奇数，每个 $d_\nu/M_N$ 都是偶数。故得到实际整数来源式
$$
\boxed{
R_{NM}
=
\left(\prod_{\nu=N}^{M-1}Z_\nu^{\,d_\nu/(2M_N)}\right)
T_{\delta_N-\delta_M,M},
\qquad
\|R_{NM}\|\le1.
}
\tag{7}
$$
这一步没有对 $C$ 或 $Z_\nu$ 取半整数幂。

于是对任意 $x\in H$，
$$
\|Q_Mx\|\le\|Q_Nx\|,\qquad
\|Q_M^*x\|\le\|Q_N^*x\|.
\tag{8}
$$
例如 $Q_M=R_{NM}Q_N$ 使用交换性；伴随同理。相反方向的原分子满足
$$
\|Y_NP_tx\|\le\|Y_MP_tx\|,\qquad
\|(Y_NP_t)^*x\|\le\|(Y_MP_t)^*x\|.
\tag{9}
$$
不能把 (8) 用于未满足奇数条件的切口。

对前稿 Walsh 基 $h_\ell$，若 $N\ge\ell$，(7) 中 $N\le\nu<M$ 的整数指数为 $\delta_Nd_\nu$；$\nu\ge M$ 的指数为 $(\delta_N-\delta_M)d_\nu$，仍是非负整数且不超过 $\delta_Nd_\nu$。收缩望远镜和同一原误差 (7) 因而给
$$
\|(R_{NM}-I)h_\ell\|
+\|(R_{NM}^*-I)h_\ell\|
\le\delta_N\sum_{\nu\ge N}d_\nu\epsilon_\nu
<\frac{2^{-N-6}}{M_N}.
\tag{10}
$$
从 (5) 及伴随交换性，
$$
\|(Q_M-Q_N)h_\ell\|
+\|(Q_M^*-Q_N^*)h_\ell\|
\le
\|Q_N\|\frac{2^{-N-6}}{M_N}.
\tag{11}
$$
这里 $\|Q_N\|$ 保留为同一个实际来源的费用。

在本文的阶乘选择中，奇数条件仅覆盖不增加 $v_2(M_N)$ 的切口，不能给所有深切口一个共同收缩控制。也没有用 (11) 自动推出 $\|Q_N\|/M_N$ 有界。

## 4. 真正强极限将直接给原闭稳定根

若 (2) 的某个尾子列 $Q_{N_j}$ 在全 $H$ 上强收敛于有界 $Q$，则一致有界原理及 $D_{N_j}\to I$ 强给
$$
Q_{N_j}^2\to Q^2,\qquad
D_{N_j}Q_{N_j}^2\to Q^2
\quad\text{强}.
$$
由 (3)，
$$
\boxed{CQ^2=P_t^2.}
\tag{12}
$$
$Q$ 仍与 $C,P_t$ 交换，并保持每个原闭不变旗及有限放大。对任一非零实际子商 $\mathcal Q$，(12) 保持成立，而 $P_{t,\mathcal Q}$ 已付单射稠像。故
$$
Q_{\mathcal Q}x=0\Longrightarrow P_{t,\mathcal Q}^2x=0,
$$
及
$$
Q_{\mathcal Q}^*x=0
\Longrightarrow
(P_{t,\mathcal Q}^*)^2x
=C_{\mathcal Q}^*(Q_{\mathcal Q}^*)^2x=0.
$$
所以 $Q_{\mathcal Q}$ 自动单射、像稠密。这一步没有给极限 $Q$ 额外假设，也没有把子列的单射稠像直接传到极限。

因此同一全空间上的最大关系
$$
S=Q^{-1}P_t,\qquad
\operatorname{Dom}S=\{x:P_tx\in\operatorname{Ran}Q\}
\tag{13}
$$
是闭、稠域的实际原根。闭性由 $QSx=P_tx$ 与 $Q$ 单射直接得到；域包含 $\operatorname{Ran}Q$。若 $x\in\operatorname{Dom}S$，则
$$
Q(P_tSx-CQx)=P_t^2x-CQ^2x=0.
$$
所以 $P_tSx=CQx\in\operatorname{Ran}Q$，即 $Sx\in\operatorname{Dom}S$ 且 $S^2x=Cx$。准确地，
$$
\operatorname{Dom}S^2=\operatorname{Dom}S,\qquad
S^2=C|_{\operatorname{Dom}S}.
\tag{14}
$$
同样论证适用于每个原旗子商。这里固定有界分子始终是 $P_t$。

## 5. 仅一致有界仍不足

如果只知道 $\sup_j\|Q_{N_j}\|<\infty$，由实际等式
$$
Q_{N_j}^2-Z_t=Q_{N_j}^2(I-D_{N_j})
$$
仍可推出 $Q_{N_j}^2\to Z_t$ 强*；然而不能把弱聚点通过平方，因而不能据此宣布 (12)。

本文没有付 $Q_N$ 的统一范数或强收敛子列。新的准确余项是增加 $v_2(M_N)$ 的切口上的同源费用及其强紧性，而不是另一个未经证明的子商准亲和条件。普通 Hilbert 不变子空间问题仍未完成。
