# R180. 原 theta 有限源的多层 p 精度

日期：2026-11-12。**状态：已证明；主目标未完成。**

## 结论

固定原两行 $\mathcal A=A_{17}(2z)/16,B$，
$\mathcal C=B-\mathcal A+22\mathcal A^2$。
对惰性 $p\ge7$、$p\ne11$，置

$$
r=(p+1)/4,\quad R=r(p-1),\quad
\varpi^R=p,\quad\lambda=\varpi^r,\quad\gamma=\varpi^p.
$$

对每个 $1\le n\le p-1$，存在原源 primitive 元

$$
\mathcal P_{p,n}\in
\mathbb Z_p[\mathcal A,B]_{\le D_{p,n}},\qquad
[B^p]\mathcal P_{p,n}=1,
$$
$$
D_{p,n}=2p+(n+1)r-\left\lfloor\frac{nr}{p}\right\rfloor-1,
$$

满足完整实际级数关系

$$
\boxed{\quad
\frac{\mathcal P_{p,n}(\mathcal A(\gamma T),B(\gamma T))}
{\lambda^p\gamma^{2p}}
\in p^n\mathcal O_{\mathbb Q_p(\varpi)}[[T]].
\quad}
$$

所有 $n$ 的初始权均为 $\Omega=p(r+2p)$，
初始式都是

$$
\mathcal C^p+p\,374^{p-1}\mathcal C\mathcal A^{2p-2}
-374^p\widetilde\tau\mathcal A^{r+2p}.
$$

特别 $n=1$ 的次数为 $(5p-1)/2$；
$n=p-1$ 的次数为 $2p+R$，付清完整 $p^{p-1}$ 改良。
同一多项式同时满足真实准确零前缀

$$
\operatorname{ord}_{s=0}
\mathcal P_{p,n}(\mathcal A(s),B(s))\ge D_{p,n}+1.
$$

## 完整证明机制

实际 $a(s)^p=\exp(p t(s))=\sum d_ms^m$ 在
$\varpi$ 尺度满足 $R v_p(d_m)+m\ge r$。
故 $d_m$ 在 $m<pr$ 全整，且
$p d_{pr}\equiv-\tau\pmod p$，边界确实出现分母。

取 $N_n=(n+1)r-1$，实际整多项式

$$
a^{N_n+p}-\sum_{m\le N_n}d_m a^{N_n-m}b^m
$$

在 $\gamma$ 尺度有精度 $\lambda^p p^n$。
把它写进真实 $Z=\mathcal C/\mathcal A^2$ 坐标，
作首一 $p$ 次 Weierstrass 准备；
其整单位因子在整个实际缩放下仍整且可逆。
截 $\mathcal A$ 次数到
$J_n=(n+1)r-\lfloor nr/p\rfloor-1$，
再乘 $\mathcal A^{2p}$ 逐项清分母，
即得原次数、精度及 $B^p$ 首一性。
原整多项式沿图的阶至少为 $N_n+1$；
准备单位不改阶，截尾误差的阶至少为 $J_n+1$，
清分母再增加 $2p$ 阶，故得到上述 $D_{p,n}+1$ 前缀。

完整全系数证明及准确环、单位、截断界见
[证明](../notes/2026-11-12-original-theta-multiple-precision-source-polynomials.md)。
所用标准代数定理为 Hochster 作者讲义
*The structure theory of complete local rings*，
2026 年网页版本，pp. 14–15；原文已读。

## 范围

这是原有限次数源的逐 $p$ 构造，
系数仅需在 $\mathbb Z_p$。
已证的 $D_{p,n}+1$ 前缀不自动保持任意更长准确零前缀；
尚须与余项一同纳入完整饱和核。
它本身没有证明原中央导数无穷次非零或 R159 的严格总预算。
