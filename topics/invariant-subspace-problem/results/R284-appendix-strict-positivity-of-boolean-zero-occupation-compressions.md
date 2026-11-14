# R284 附录：正权 Boolean 零占据压缩的严格正定性

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态。** 本文是 [跨出生零占据 Gram 主稿](R284-cross-birth-zero-occupation-grams-and-exact-schur-lower-bound.md) 的有限正权补充。它证明主稿里的实际零占据 Gram 在合法非零源上严格正定；不声称得到与权比、位数或出生无关的谱隙。

## 1. 一个平方自由多项式不能有正权集体线性因子

设 $M<\infty$，所有 $b_i\ne0$，令
$$
\ell(x)=\sum_{i=1}^M b_i x_i.
$$
若非零平方自由多项式 $f$ 满足 $f=\ell g$，则对每个 $i$，
$$
\deg_{x_i}f=\deg_{x_i}g+1.
\tag{1.1}
$$
确实，把 $g$ 视为 $x_i$ 的多项式，其最高次系数乘以 $b_ix_i$ 给出 $\ell g$ 的唯一最高次项；$\ell-b_ix_i$ 不含 $x_i$，不能抵消该项。

平方自由性给 $\deg_{x_i}f\le1$，于是 $g$ 与每个 $x_i$ 无关，所以 $g$ 为常数。特别，如果 $f$ 还齐次且次数 $p\ge2$，就不可能有非零的这种因子分解。

## 2. 真空投影在每个 $p\ge2$ 的实际 Boolean 层上单射

仍取主稿的单位归一 $\sum_i|b_i|^2=1$。在 Bargmann 多项式实现中，集体模式
$$
a_0=\sum_i\overline b_i a_i
$$
的 creation 是乘以 $\ell(x)$。将整个齐次 Fock 层按该模式的 occupation 分解，记 $P_0$ 为零 occupation 正交投影。

若 $P_0f=0$，则 $f$ 的每个 occupation 分量都含至少一个集体模式因子，所以 $f=\ell g$，其中 $g$ 齐次次数为 $p-1$。对平方自由 $f\in\mathcal H_p$，上一节表明：当 $p\ge2$ 时只能 $f=0$。

故对于每个非零实际层 $\mathcal H_p$、$2\le p\le M$，
$$
\boxed{P_0|_{\mathcal H_p}\text{ 单射},\qquad
\mathsf E_p=P_{\mathcal H_p}P_0|_{\mathcal H_p}>0.}
\tag{2.1}
$$
第二个结论使用有限维性和
$\langle\mathsf E_pf,f\rangle=\|P_0f\|^2$。

两个低次数端点须分别保留：$\mathsf E_0=I$；在 $p=1$ 上，
$$
\mathsf E_1=I-bb^*,\qquad \ker\mathsf E_1=\mathbb Cb.
\tag{2.2}
$$
所以 (2.1) 不能下移到一粒子层。

## 3. 对跨出生零占据 Gram 的直接后果

在主稿记号中固定 $s\ge1$。每个合法完整最小逆 $\mathcal J_{j,r}$ 都是单射，因为 $(D^j/j!)\mathcal J_{j,r}=I_{K_r}$。它与对应物理层上单射的 $P_0$ 复合仍然单射。因此主稿四个零占据 Gram 在非零源上分别满足
$$
\boxed{G_1-I=U_s^*U_s>0,\qquad
Y_2=Z_{2,s-1}^*Z_{2,s-1}>0}
\tag{3.1}
$$
（只需 $M-2s\ge1$），以及
$$
\boxed{X_2=Z_{2,s}^*Z_{2,s}>0,\qquad
Y_3=Z_{3,s-1}^*Z_{3,s-1}>0}
\tag{3.2}
$$
（要求 $M-2s\ge2$）。前两者对应物理次数 $s+1\ge2$，后两者对应物理次数 $s+2\ge3$。

在这个有限、所有权非零的范围内，主稿中的 $H^\dagger$ 与 $Y_3^\dagger$ 因而可以分别用普通逆 $(G_1-I)^{-1}$、$Y_3^{-1}$ 书写。主稿保留的带真实范围条件的伪逆形式仍是正确的，并便于处理退化极限；不能把有限维严格正定性误写成极限中的一致有界逆。

这里所有 $b_i\ne0$ 是实质条件。若某些物理位权为零，平方自由高次多项式可以含集体线性因子，(2.1) 就可能失败。本文不对这种退化模型作严格正定声明，也没有从严格号推出一般首边或 S1/S2。
