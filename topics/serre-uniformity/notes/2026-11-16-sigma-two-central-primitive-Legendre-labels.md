# 两个固定中央标签的本原性与原 Legendre 非共同零

日期：2026-11-16。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：以下两个标签的本原性及其 Legendre 因子不同时为零已证明；同标签的两个原 sigma 系数仍未证明为单位。** 本篇不增加素数扫描，只对 [R734](../results/R734-primitive-unit-toric-norm-at-every-prime.md) 的准确六步递推作纸面代入。

## 1. 两个标签始终是真本原标签

设
$$
p=12k+5\ge41,\qquad N=(p-5)/6=2k.
\tag{CL1}
$$
在 R770 的原标签 $h=6i+7$、$j=N-1-i$ 中取
$$
\begin{array}{c|c|c|c}
 &i&j&h\\ \hline
-&k-1&k&h_-=(p-3)/2=6k+1\\
+&k&k-1&h_+=(p+9)/2=6k+7.
\end{array}
\tag{CL2}
$$
由 $k\ge3$，这些指标均在 $0\le i,j\le N-1$ 内，且
$7\le h_-<h_+\le p-4$。两标签都是奇数并且为 $1\pmod6$。
又
$$
2h_--(p+1)=-4,\qquad
2h_+-(p+1)=8.
\tag{CL3}
$$
所以 $\gcd(h_-,p+1)$ 整除 $4$，
$\gcd(h_+,p+1)$ 整除 $8$；它们又是奇数，故
$$
\boxed{\gcd(h_-,p+1)=\gcd(h_+,p+1)=1.}
\tag{CL4}
$$
这里没有对 $p+1$ 的奇素因子作额外假设。

## 2. 原六步 Legendre 递推在中央位置的单位

保留 R727/R734 的原 $x=1/s$、$s^2=-3$，故 $x^2=-1/3$。
令 $P_d$ 为 $P_d(1)=1$ 的 Legendre 多项式。所需两个值为
$$
L_-=P_d(x),\qquad L_+=P_{d+6}(x),\qquad
d=h_--1=(p-5)/2=6k.
\tag{CL5}
$$
$1\le d$ 且 $d+6<p$，因此 R734.7--R734.11 的所有阶乘及
递推分母都在其已证明的单位范围内。

R734.7 首先给 $P_{d-1}(x)$ 与 $P_d(x)$ 不能同时为零。
如果 $P_d(x)=0$，R734.10--R734.11 准确给
$$
P_{d+6}(x)
=-\frac{d\,U_5(d)}{(d+1)(d+2)\cdots(d+6)}P_{d-1}(x),
\tag{CL6}
$$
$$
U_5(d)=\frac{x}{9}(2d+7)
\left(91[d(d+7)]^2+1800d(d+7)+8748\right).
\tag{CL7}
$$
在 $\mathbf F_p$ 中，(CL5) 给
$$
d=-5/2,\qquad 2d+7=2,\qquad d(d+7)=-45/4.
$$
逐项代入得到
$$
91\left(-\frac{45}{4}\right)^2
+1800\left(-\frac{45}{4}\right)+8748
=\frac{184275-324000+139968}{16}
=\frac{243}{16}.
\tag{CL8}
$$
因而
$$
U_5(d)=\frac{27x}{8}\ne0.
\tag{CL9}
$$
更精确地，(CL6) 的分母在此处为
$$
\prod_{a=1}^6(d+a)
=\frac{(-3)(-1)(1)(3)(5)(7)}{2^6}
=\frac{315}{64},
$$
故
$$
\boxed{P_d(x)=0\quad\Longrightarrow\quad
P_{d+6}(x)=\frac{12x}{7}P_{d-1}(x)\ne0.}
\tag{CL10}
$$
显示的分母只涉及 $2,3,5,7$；$p\ge41$ 已排除所有例外，
且 $x\ne0$。这证明
$$
\boxed{(L_-,L_+)\ne(0,0).}
\tag{CL11}
$$
两个次数均为偶数，所以这两个值实际属于 $\mathbf F_p$；
在 $\mathbf F_{p^2}$ 中选取 $s$ 的另一平方根不改变结论。
由原 $\overline N_h=-P_{h-1}(1/s)^2$，这也是两个指定原本原
有限范数中至少一个为单位的准确陈述。

## 3. 对真正同标签目标的范围

采用 [R770](../results/R770-same-primitive-label-square-and-finite-bilinear-pairing.md)
的原 $c=0$ 系数
$$
x\sigma^6=z^4\sum f_i z^{6i},\qquad
-xy\sigma^6=z\sum g_j z^{6j}.
$$
本窗口的两个实际乘积恰为
$$
T_-=f_{k-1}g_k,\qquad T_+=f_k g_{k-1}.
\tag{CL12}
$$
因此证明
$$
L_-T_-\ne0\quad\hbox{或}\quad L_+T_+\ne0
\tag{CL13}
$$
将给该素数一个满足 R770 三个单位条件的实际本原标签。
例如，若能另证 $T_-T_+\ne0$，则 (CL11) 足以推出 (CL13)。
但本文没有证明这两个 sigma 乘积均为单位，也没有证明其中
一个非零乘积必落在 Legendre 可见的那个标签上。

本篇只给 $p\equiv5\pmod{12}$ 的一个固定二标签充分窗口，
不把原全部标签的存在性问题等同于 (CL13)。
$p\equiv11\pmod{12}$ 的原中央标签及其三个单位条件亦未由此解决。
特征零非零、未筛交替卷积非零和全局 Cartier 非零均不填补
(CL12)--(CL13) 的同标签缺口。
