# R267 附录：全部切口的实际平方收缩与无条件平方强收敛

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 固定[相容有理根](R267-appendix-coherent-bounded-rational-roots-of-one-flat-common-denominator.md)中的同一个原 Haar 尾 $C$ 和同一组实际因子。本文增强[固定分子与实际分母](R267-appendix-fixed-numerator-actual-denominators-and-odd-cut-contractions.md) §5：不再假设 $Q_N$ 一致有界，即可证明整个合法尾列的 $Q_N^2$ 强*收敛。新的输入是所有切口比值的平方都具有同一个实际收缩来源；比值本身只在旧稿的奇数切口已付收缩。

## 1. 同族对象与范围

沿用
$$
M_n=(n+1)!,\qquad d_n=M_{n+1}-M_n,\qquad
\epsilon_n=\frac{2^{-n-6}}{1+d_n}.
\tag{1}
$$
$Z_n=C U_n(C)$ 是保持函数正锥的实际多项式收缩，全部因子交换，且对单位 Walsh 基 $h_\ell$，
$$
\|(Z_n-I)h_\ell\|+\|(Z_n^*-I)h_\ell\|
\le\epsilon_n\qquad(\ell\le n).
\tag{2}
$$
对正有理数 $r$ 及 $rM_N\in\mathbb N$，实际整数尾积为
$$
T_{r,N}
=\operatorname*{SOT^*\!-\!lim}_{K\to\infty}
\prod_{\nu=N}^{K-1}Z_\nu^{r d_\nu},
\qquad \|T_{r,N}\|\le1.
\tag{3}
$$
每个指数均为非负整数。$P_r$、同一解析单位前缀以及全部原幂逆仍取自原构造。

固定 $t\in\mathbb Q_{>0}$，记
$$
\delta_N=\frac1{2M_N},\qquad
V_N=\prod_{\nu<N}U_\nu(C)^{d_\nu/(2M_N)},\qquad
D_N=T_{1/M_N,N},
\tag{4}
$$
$$
Y_N=P_{\delta_N}V_N^{-1},\qquad
Q_N=P_{t-\delta_N}V_N,\qquad
Z_t=C^{-1}P_{2t}.
\tag{5}
$$
$Q_N$ 只在 $\delta_N<t$ 时使用，$C^{-1}P_{2t}$ 是已经支付的实际全域有界来源。各算子互相交换；每一个分别有界。旧稿已证明
$$
Y_NQ_N=P_t,\qquad
Y_N^2=CD_N,\qquad
D_NQ_N^2=Z_t,\qquad D_N\longrightarrow I\quad\text{强*}.
\tag{6}
$$
$Q_N,D_N,Z_t$ 在每个非零原有限放大闭不变旗子商上均单射、像稠密。这里只引用原同因子的强单位证明，不从平坦性推范围。

对 $M>N$ 置
$$
R_{NM}=P_{\delta_N-\delta_M}V_N^{-1}V_M.
\tag{7}
$$
旧同源恒等式为
$$
Q_M=Q_NR_{NM},\qquad
D_N=D_MR_{NM}^2,\qquad
R_{NL}=R_{NM}R_{ML}\quad(N<M<L).
\tag{8}
$$

## 2. 全部切口的真实平方因子

无需对整数 $M_M/M_N$ 加奇偶条件，定义
$$
\boxed{
L_{NM}
=
\left(\prod_{\nu=N}^{M-1}Z_\nu^{\,d_\nu/M_N}\right)
T_{\,1/M_N-1/M_M,\,M}.
}
\tag{9}
$$
这是合法的实际整数来源。确切地，$M_N\mid d_\nu$ 对所有 $\nu\ge N$ 成立，而
$$
\left(\frac1{M_N}-\frac1{M_M}\right)M_M
=\frac{M_M}{M_N}-1\in\mathbb N.
$$
所以 (9) 的有限段和尾段全部只含非负整数幂。它保持函数正锥，且
$$
\|L_{NM}\|\le1.
\tag{10}
$$
这里的正性指函数正锥，不是 Hilbert 空间自伴正性。

为直接核对来源，先取 $K>M$。$D_M$ 的有限尾积乘上 (9) 的相应有限乘积，在 $\nu\ge M$ 的指数相加为
$$
\frac{d_\nu}{M_M}
+\left(\frac1{M_N}-\frac1{M_M}\right)d_\nu
=\frac{d_\nu}{M_N}.
$$
连同 $N\le\nu<M$ 的有限段，所得恰为 $D_N$ 的同一个有限尾积。所有部分收缩，故乘积可通过强*极限，得到全空间上的准确恒等式
$$
\boxed{D_N=D_ML_{NM}.}
\tag{11}
$$
由 (8) 和实际 $D_M$ 单射消去，
$$
\boxed{R_{NM}^2=L_{NM},\qquad \|R_{NM}^2\|\le1.}
\tag{12}
$$
这不声称 $\|R_{NM}\|\le1$。尤其没有在偶数倍率切口对 $C$ 或 $Z_\nu$ 施加半整数幂。

同一乘积来源还给
$$
L_{NL}=L_{NM}L_{ML}\qquad(N<M<L).
\tag{13}
$$
若 $N\ge\ell$，(9) 中每个实际整数指数不超过 $d_\nu/M_N$。由 (2) 的收缩望远镜，
$$
\begin{aligned}
&\|(L_{NM}-I)h_\ell\|+\|(L_{NM}^*-I)h_\ell\|\\
&\qquad\le
\frac1{M_N}\sum_{\nu\ge N}d_\nu\epsilon_\nu
<
\frac{2^{-N-5}}{M_N}.
\end{aligned}
\tag{14}
$$
此界对所有 $M>N$ 一致。因此 $L_{NM}\to I$ 强*，且极限对 $M>N$ 一致；全空间延拓仅用统一收缩界与 Walsh 基稠密性。

## 3. 无条件的平方强*极限

固定任一 $N_0$ 使 $\delta_{N_0}<t$。由 (8)、(12) 和交换性，对所有 $M>N\ge N_0$，
$$
\boxed{Q_M^2=Q_N^2L_{NM}=L_{NM}Q_N^2.}
\tag{15}
$$
所以逐个向量的两种平方像范数均单调：
$$
\|Q_M^2x\|\le\|Q_N^2x\|,\qquad
\|(Q_M^*)^2x\|\le\|(Q_N^*)^2x\|.
\tag{16}
$$
特别
$$
\boxed{\sup_{N\ge N_0}\|Q_N^2\|\le\|Q_{N_0}^2\|<\infty.}
\tag{17}
$$
不需要任何关于 $\sup_N\|Q_N\|$ 的假设。

令 $A_N=Q_N^2$。由 (6) 及交换性，
$$
A_N-Z_t=A_N(I-D_N).
\tag{18}
$$
(17) 与 $D_N\to I$ 强立即给 $A_N\to Z_t$ 强。取伴随后，$A_N^*$ 与 $D_N^*$ 仍交换，故亦可写
$$
A_N^*-Z_t^*=A_N^*(I-D_N^*).
$$
同一统一界给伴随强收敛。因此
$$
\boxed{Q_N^2\longrightarrow C^{-1}P_{2t}\quad\text{强*，沿全部合法切口}.}
\tag{19}
$$
结合 (16)，对每个 $x$ 有
$$
\|Q_N^2x\|\downarrow\|Z_tx\|,\qquad
\|(Q_N^*)^2x\|\downarrow\|Z_t^*x\|.
\tag{20}
$$
当 $x\ne0$ 时，两个极限都严格正，因为 $Z_t$ 已付单射及稠值；这不是一个一致的正下界。

## 4. 同来源的正能量与误差

(15) 保留完整来源顺序，直接给
$$
\begin{aligned}
\|Q_N^2x\|^2-\|Q_M^2x\|^2
&=\big\|(I-L_{NM}^*L_{NM})^{1/2}Q_N^2x\big\|^2,\\
\|(Q_N^*)^2x\|^2-\|(Q_M^*)^2x\|^2
&=\big\|(I-L_{NM}L_{NM}^*)^{1/2}(Q_N^*)^2x\big\|^2.
\end{aligned}
\tag{21}
$$
这里两种缺陷都由同一个实际收缩 $L_{NM}$ 产生。于是
$$
(Q_N^2)^*Q_N^2\downarrow Z_t^*Z_t,\qquad
Q_N^2(Q_N^*)^2\downarrow Z_tZ_t^*
\quad\text{强}.
\tag{22}
$$
强极限使用 (17)、(19)，单调性使用 (21)，没有将弱收敛乘起来。

还可从 (18) 和原 $D_N$ 的误差得到具体同源测试界：
$$
\begin{aligned}
&\|(Q_N^2-Z_t)h_\ell\|
+\|((Q_N^*)^2-Z_t^*)h_\ell\|\\
&\qquad\le
\|Q_{N_0}^2\|\frac1{M_N}
\sum_{\nu\ge N}d_\nu\epsilon_\nu
<
\|Q_{N_0}^2\|\frac{2^{-N-5}}{M_N}
\qquad(N\ge\max(N_0,\ell)).
\end{aligned}
\tag{23}
$$
固定任意整数 $a\ge1$，(15) 同样给 $Q_M^{2a}=L_{NM}^aQ_N^{2a}$；其向量范数与伴随向量范数也单调，且
$$
Q_N^{2a}\longrightarrow Z_t^a\quad\text{强*}.
\tag{24}
$$
这只是同一平方来源的整数乘积，不包含奇次幂范数预算。

## 5. 原旗范围与未付的根来源

以上每个有限来源都保持所有原 $C$ 不变旗，强极限亦保持；对任意固定有限放大同样成立。实际子商上的乘积、收缩界、单射消去及强*极限因此全部保留。 具体把闭旗 $E\subset F$ 的商识别为 $F\cap E^\perp$，诱导算子及其伴随分别是原算子和原伴随在此固定闭子空间的压缩；故原强*收敛确实传到该商，且乘法由旗不变性保留。具体而言，若 $\mathcal Q$ 是一个非零原旗子商，则
$$
Q_{N,\mathcal Q}^2
\longrightarrow C_{\mathcal Q}^{-1}P_{2t,\mathcal Q}
\quad\text{强*},
$$
右边仍指已付的实际有界来源，不能理解为处处定义的 $C_{\mathcal Q}^{-1}$ 本身。(20)–(22) 在该子商的实际 Hilbert 度量中成立。

本文付的是整个同族平方序列的无条件控制。它与某些合法分离块选择中 $\|Q_N\|\to\infty$ 完全相容：平方范数的上界不控制算子本身的范数。

仍未证明 $Q_N$ 本身一致有界、强收敛子列，或弱聚点可通过平方。若能付真正强子列，旧固定分子稿 §4 才给 $CQ^2=P_t^2$ 及同一个实际最大闭稳定根。本文没有越过这个来源与紧性缺口，也没有完成普通 Hilbert 不变子空间问题。
