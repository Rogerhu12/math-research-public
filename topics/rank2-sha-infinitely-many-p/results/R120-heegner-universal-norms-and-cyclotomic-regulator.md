# R120：实际 Heegner 点的整范数族及范数一块的 cyclotomic regulator 非退化

日期：2026-11-12。状态：**已证明**。

完整规范、逐层总迹和高度来源见
[工作证明](../notes/2026-11-12-actual-heegner-universal-norms-and-cyclotomic-height.md)。
本卡保留全部核心证明，不把高度非零替代最低增广层的单位性。

## 1. 实际对象与结论

取 R116 的实际 $p,\ell$，$E:y^2=x^3-17x$、
$F=\mathbf Q(\sqrt{-15})$，以及环类域中的次数 $p$ 扩张
$L/F$。记 $\Gamma=\langle\tau\rangle$、
$A=\ker(\operatorname{Res}_{L/F}E\to E)$，实际点为
$$
Q=\operatorname{Tr}_{F[\ell]/L}P[\ell]\in A(F).
$$
R116 给 $Q$ 非挠；R106 给 $cQ=-\tau^jQ$；R119 给
$\operatorname{rank}_{\mathbf Z}A(F)=p-1$ 和 $\Sha(A/F)$ 有限。
输入 $p\ge13$ 在 $F$ 及 $\mathbf Q(i)$ 中分裂，
$\ell$ 在两域中惰性且 $v_p(\ell+1)=1$。

**定理。** 设 $F_\infty/F$ 为反圆分 $\mathbf Z_p$ 扩张。

1. 存在 $\mathcal Q_m\in E(LF_m)\widehat\otimes\mathbf Z_p$，
   $\mathcal Q_0=Q$，且每层迹将 $\mathcal Q_{m+1}$ 送到
   $\mathcal Q_m$；整个族位于 $\Gamma$-范数一块。
2. cyclotomic $p$ 进高度在 $A(F)\otimes\mathbf Q_p$ 上非退化。
3. $F$-反圆分方向的高度在此块上恒零；相应完整增广提升的
   派生 Bockstein 配对也杀此块。

## 2. 第零项精确为 Q 的范数族

令 $L_m=LF_m$，$F_m/F$ 次数 $p^m$。设
$$
Q_0=Q,\qquad
Q_n=\operatorname{Tr}_{F[\ell p^n]/L_{n-1}}P[\ell p^n]
\quad(n\ge1).
$$
若 $\sigma\in\Gamma$ 是 $F$ 中一个 $p$ 上素理想的 Artin
符号，则实际 CM 同源图给
$$
\begin{aligned}
Q_1&=(a_p-\sigma-\sigma^{-1})Q_0,\\
\operatorname{Tr}Q_2&=a_pQ_1-(p-1)Q_0,\\
\operatorname{Tr}Q_n&=a_pQ_{n-1}-Q_{n-2}\quad(n\ge3).
\end{aligned}                                       \tag{1}
$$
其中完整 tame 迹群的阶在 $n=0$ 为 $2u$，$n\ge1$ 为
$2u(p-1)$，$u=(\ell+1)/p$。第一映射的核阶 $p-1$，
以后映射同构；这证明第二式和第三式的不同系数。

令 $\alpha\in\mathbf Z_p^\times$ 为 ordinary 单位根。
对 $n\ge2$ 置
$$
z_n=\alpha^{-n}(Q_n-\alpha^{-1}Q_{n-1}).
$$
由 $a_p-p\alpha^{-1}=\alpha$，$\operatorname{Tr}z_n=z_{n-1}$
对 $n\ge3$ 成立，而初层为
$$
\operatorname{Tr}z_2
 =(1-\alpha^{-1}\sigma)(1-\alpha^{-1}\sigma^{-1})Q=:u_pQ.
                                                               \tag{2}
$$
$\mathbf Z_p[C_p]$ 是局部环，$u_p$ 在其剩余域中的像为
$(1-\alpha^{-1})^2$。$E$ 的有理二挠点使 $a_p$ 为偶数，
Hasse 界及 $p\ge13$ 使 $a_p\not\equiv1\pmod p$。
所以 $u_p$ 是单位。取
$$
\mathcal Q_0=Q,\qquad \mathcal Q_m=u_p^{-1}z_{m+1}\quad(m\ge1)
$$
即得结论 1。加入 $\ell$ 导子的范数因子是 $a_\ell=0$，
故该族仍在 $\Gamma$-范数一块。这些是真实全局点的 $p$ 进
整线性组合；没有除 $p$ 或使用一个未证明存在的全局除点。

## 3. 一个实际非零高度与秩一迹形式

设 $K=\mathbf Q(i)$，$p=\mathfrak p\bar{\mathfrak p}$。
Rubin 附录 Theorem A.1 所引 Bertrand 单点非零定理，
可先应用于 R103 已证根数为 $-1$ 的 $E^{(-15)}$ 上
对应的非挠点，再经 $F\subset L$ 上的同构运输回来。
这完全保留附录的根数约定，给
$h_{\mathfrak p}(Q,Q)\ne0$。

single-prime 高度对 $\Gamma$ 不变，复共轭交换两个 prime
字符。因此实际 $cQ=-\tau^jQ$ 给
$$
h_{\bar{\mathfrak p}}(Q,Q)=h_{\mathfrak p}(Q,Q),\qquad
h_{\rm cyc}(Q,Q)=2h_{\mathfrak p}(Q,Q)\ne0.           \tag{3}
$$
域扩张高度规范只改已知非零次数因子。

令 $\mathcal K=\mathbf Q_p(\zeta_p)$、
$W=A(F)\otimes\mathbf Q_p$。$N$ 在 $A$ 上为零，而
R119 给 $\dim_{\mathcal K}W=1$；非零 $Q$ 是一组基。
每个 $\Gamma$-不变双线性配对唯一形如
$$
h(xQ,yQ)=\operatorname{Tr}_{\mathcal K/\mathbf Q_p}(c_hx\bar y),
                                                               \tag{4}
$$
其中 bar 将 $\zeta_p$ 送到 $\zeta_p^{-1}$。对称性等价于
$c_h=\bar c_h$。对 cyclotomic 高度，(3) 迫使 $c_h\ne0$；
迹配对非退化及乘 $c_h$ 可逆给结论 2。

## 4. 反圆分方向及精确剩余问题

$F$-反圆分高度对 $c$ 反号。将 $c(xQ)=-\bar x\tau^jQ$
代入 (4)，得到 $\bar c_h=-c_h$，与对称性合起来使
$c_h=0$。更强地，结论 1 给了完整紧 Selmer 范数提升，
所以每个有限增广商中的连接障碍都为零，证明结论 3。
这使用真实的 $LF_\infty/L$，不把在 $\ell$ 分歧的
有限 $L/F$ 当成一个不分歧于 $\ell$ 的 $\mathbf Z_p$ 塔。

令 $\mathcal O=\mathbf Z_p[\zeta_p]$，以 $e$ 为实际饱和
格的一组 $\mathcal O$-基，写 $Q=ae$。结论 2 只给
高度系数 $c_e\ne0$，而目标仍为
$$
v_{\zeta_p-1}(a)=0.
$$
已知 $Q$ 不可被 $p$ 除只给此赋值小于 $p-1$。本结果没有
证明这个赋值为零，也没有由非退化高度推出原曲线的 Sha 有限。

## 外部已证输入

- Cornut（2002），*Mazur's conjecture on higher Heegner points*，
  Invent. Math. 148，§§1、4.1；实际环类点及同源/Artin 作用。
- Bertrand（1984），*Propriétés arithmétiques de fonctions thêta
  à plusieurs variables*；所用单点定理的明确发表表述为
  Rubin Appendix A，Theorem A.1，附于 Agboola--Howard（2006），
  AIF 56，印刷第 1043 页，
  [正式全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- Bertolini--Darmon（1995），*Derived p-adic heights*，
  Amer. J. Math. 117，Theorem 2.18：该文 $1\le k\le p-1$ 阶的
  通用范数与派生高度根；全有限增广层的连接障碍由本篇完整提升直接消去。
  [正式全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/pub13.pdf)。
