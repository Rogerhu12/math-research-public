# 原固定 Prym 的三无穷点商与有界 trace 来源

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
状态：完整代数纸证；无数学程序执行。

本篇继续[原 Tate normal-FM §15](2026-11-27-original-Tate-three-torsion-normal-FM-variation.md)。
同一原固定 Prym 有一个明确的 degree-three étale 商，目标准确是原
$E:V^2=U^3+v^2$。本文给出函数、原微分尺度和两个标记的完整 trace，
不只认同 $j$ 值，也不将 trace 的最高系数单位当成指定 Cartier 值单位。

## 1. 固定源、真实平移与商函数域

设 $p=6k-1>37$，$m=(p-1)/2=3k-1$，仍取原 $v^2=-108$、
$v^p=-v$。在包含原常数的域 $K$ 上，源为
$$
E_P:\quad x^3+3xr^2+2v=0,\qquad
\omega_P=\frac{dx}{3xr}.
\tag{T.1}
$$
取一个原三次单位根 $\zeta$，令 $s=\zeta-\zeta^2$，故 $s^2=-3$。
设
$$
A=r+x,\qquad B=r-x,\qquad B^3-A^3=4v.
$$
实际自同构
$$
\tau(A,B)=(\zeta A,\zeta^2B)
\quad\Longleftrightarrow\quad
\tau(x,r)=\left(\frac{-x+sr}{2},\frac{sx-r}{2}\right)
\tag{T.2}
$$
的阶为三。齐次 Fermat 模型的三个坐标轴点均不在曲线上，
而它们是对角作用仅有的 projective 不动点，所以 $\tau$ 没有不动点。
又 $\omega_P=-2\,dA/(3B^2)$，因此 $\tau^*\omega_P=\omega_P$。

取源原点为 $r=\infty,x/r=0$ 的点。
$\tau$ 循环置换三个无穷点，它们是同一个阶三平移子群的轨道；
后述商映射也直接证明这一群律解释。
定义
$$
q=r^2-x^2,\qquad w=r^3+3rx^2.
$$
两者都在 $\tau$ 下不变，且
$$
w^2-q^3=x^2(x^2+3r^2)^2=4v^2.
\tag{T.3}
$$
由
$$
r^3-\frac{3q}{4}r-\frac w4=0,\qquad
x=-\frac{2v}{4r^2-q},
\tag{T.4}
$$
得到 $[K(E_P):K(q,w)]\le3$。
分母不为零函数，因原 cubic 给 $x(4r^2-q)=-2v$。
三个真实 $\tau$ 共轭互异，故次数恰为三，
$K(q,w)$ 正是完整不变子域。

## 2. 目标准确为原 E；微分尺度不能删除

因为 $p\equiv2\bmod3$，取唯一 $\rho\in\mathbf F_p^\times$
使 $\rho^3=2$。定义
$$
\boxed{\quad
\phi:E_P\longrightarrow E,\qquad
U=\frac q{\rho^2},\quad V=\frac w2,\qquad
E:V^2=U^3+v^2 .
\quad}
\tag{T.5}
$$
$\rho^6=4$ 与 (T.3) 直接验证目标方程，原 $v$ 没有改变。
(T.4) 证明其次数为三；它把三个源无穷点都送到原目标 $O$。
这给 smooth projective 曲线间的实际态射。
无不动点的阶三商在 $p>3$ 下有限 étale。
选定的源原点送到 $O$，因此它是一个真正的 elliptic isogeny，
其 deck 作用正是 kernel 平移。

在原 $D_P=d/\omega_P$ 下，
$$
D_Pr=-\frac32(x^2+r^2),\qquad D_Px=3xr,\qquad D_Pq=-3w.
$$
所以原 $\omega_E=dU/(2V)$ 的准确拉回为
$$
\boxed{\quad
\phi^*\omega_E=a\,\omega_P,\qquad
a=-\frac3{\rho^2}\in\mathbf F_p^\times .
\quad}
\tag{T.6}
$$
特别 $a^p=a$。后续相对 Frobenius 的目标 $\phi'$ 使用同一个 $a$；
不能将 degree-three 的 trace 与这个 differential 因子混为一谈。

## 3. 全部多项式 trace 的有限递推

记
$$
P_n(q,w)=\operatorname{Tr}_{K(E_P)/K(E)}(r^n).
$$
由 (T.2)–(T.4)，三个共轭 $r,\tau r,\tau^2r$ 正是
$Z^3-(3q/4)Z-w/4$ 的三根。因此在 $\mathbf Z[1/2,q,w]$ 中，
$$
\boxed{
P_0=3,\quad P_1=0,\quad P_2=\frac{3q}{2},\qquad
P_n=\frac{3q}{4}P_{n-2}+\frac w4P_{n-3}\quad(n\ge3).
}
\tag{T.7}
$$
这不是对若干素数拟合的递推。

$P_{2n}$ 只含偶数次 $w$；用 $w^2=q^3+4v^2$ 消去后，
$$
P_{2n}\in K[q,v^2],\qquad \deg_qP_{2n}\le n .
$$
其最高 $q$ 系数可以在这个多项式恒等式中令 $v^2=0$ 读取。
取 $w=q^{3/2}$，三根是
$\sqrt q,-\sqrt q/2,-\sqrt q/2$；故对 $n\ge0$，
$$
\boxed{\quad [q^n]P_{2n}=1+2^{1-2n}.\quad}
\tag{T.8}
$$
这里的退化只用于读取已构造多项式的最高齐次项，
没有把 $v=0$ 的退化曲线当成原几何纤维。

## 4. 两个原标记的完整 trace 源

原规范 primitive 为
$$
\mathcal R(U)=U^2\sum_{i=0}^{k-1}r_iU^{3i},
\qquad r_{k-1}=1,\qquad D_E\mathcal R=\Psi .
$$
所有 $r_i$ 都沿原 R1061/N.65/N.72，不作重标。
在源上 $\mathcal R$ 的自变量是 $r^2$；在目标上则使用 (T.5) 的 $U$。
定义两个明确多项式
$$
\boxed{
\begin{aligned}
A_*(U)&=\frac13\operatorname{Tr}\left(
 \frac{\mathcal R(r^2)}{r^2}\right)
 =\frac13\sum_{i=0}^{k-1}r_iP_{6i+2}(\rho^2U,2V),\\
B_*(U)&=\frac13\operatorname{Tr}\left(\mathcal R(r^2)^2\right)
 =\frac13\sum_{i,j=0}^{k-1}r_ir_jP_{6i+6j+8}(\rho^2U,2V).
\end{aligned}}
\tag{T.9}
$$
上节的偶性及 $V^2=U^3+v^2$ 保证右侧确是 $U$ 的多项式，
没有留在未知的三次 splitting field 中。

源 CM 作用 $(x,r)\mapsto(\zeta x,\zeta r)$ 与 $\tau$ 交换，
在目标上为 $(U,V)\mapsto(\zeta^2U,V)$。
所以两多项式都在 $U K[U^3]$ 中。
原最高项及 (T.8) 给出准确单位：
$$
\boxed{
\deg A_*=m-1,\quad [U^{m-1}]A_*=\frac3{\rho^2};
\qquad
\deg B_*=p-1,\quad [U^{p-1}]B_*=1.
}
\tag{T.10}
$$
第一式使用 $1+2^{4-p}=9$ 和 $\rho^{p-3}=\rho^{-2}$；
第二式使用 $1+2^{3-2p}=3$ 和 $\rho^{2p-2}=1$。
所有等式是在当前 $\mathbf F_p$ 中的准确读取。

相对 Cartier 标量也完整保留：
$$
\boxed{
C_{{\rm rel},E}(A_*\omega_E)=\frac e v\,\omega_E',
\qquad
C_{{\rm rel},E}(B_*\omega_E)=K_4\,\omega_E'.
}
\tag{T.11}
$$
证明如下。若源函数为 $f$，则 (T.6) 给
$$
\phi_*(f\omega_P)=a^{-1}\operatorname{Tr}(f)\,\omega_E.
$$
相对 Cartier 与这个 étale trace 相容：
拉回后两边都是 $\sum_{j=0}^2\tau^{j*}C(f\omega_P)$，
可由可分拉回的单射性确认。
N.69/N.68 分别给
$C((\mathcal R/r^2)\omega_P)=(e/v)\omega_P'$
和 $C(\mathcal R^2\omega_P)=K_4\omega_P'$。
又 $\phi'_*\omega_P'=3a^{-1}\omega_E'$，
且 Cartier 对底域常数线性、$a^p=a$。
将两边共同的 $3a^{-1}$ 消去，恰得 (T.11)，
没有额外的三或半线性重标。

## 5. Proper 类及尚需支付的具体非零

原 N.68–70 已构造来源固定的 proper de Rham 类
$$
\Xi=d(x\mathcal R/r)+3v(\mathcal R/r^2)\omega_P,
\qquad \Upsilon=-3\mathcal R^2\omega_P .
$$
推送后精确为
$$
[\phi_*\Xi]=-3v\rho^2[A_*\omega_E],\qquad
[\phi_*\Upsilon]=3\rho^2[B_*\omega_E].
\tag{T.12}
$$
全局 exact 项经 trace 仍 exact。三个 kernel 平移对
$H^1_{\rm dR}(E_P)$ 的作用为恒等；也可从
$\tau^*\omega_P=\omega_P$、Serre 对偶和阶三作用可半单直接推出。
于是 $\phi^*\phi_*=3$，从而
$$
\boxed{
[\Xi]=-v\rho^2\phi^*[A_*\omega_E],\qquad
[\Upsilon]=\rho^2\phi^*[B_*\omega_E].
}
\tag{T.13}
$$
这是真正同源上的类识别，不是只在一个 Cartier 系数上作比例猜测。

$A_*\omega_E$ 的极阶为 $p-3$，$B_*\omega_E$ 的极阶为 $2p-2$，
都只有原 $O$ 一处极。其相对 Cartier 已证全纯；
高极 primitive 的 $p$ 次自由项按 N.70 的同一 CM 角色排除，
故这些也是来源固定的 proper 类。

(T.9)–(T.13) 付出了后继可以直接使用的原目标多项式、
最高项、trace 及微分尺度。它们仍没有证明两个指定
Cartier 系数不能同时为零。最高项单位、degree-three 同源为
$p$ 单位，以及整个 de Rham 空间完美，都不能代替这一未付结论。

来源：原 R1061 的 $\Psi,\mathcal R$ 规范及原 Tate normal-FM
N.68–72；本篇所有商函数、次数、微分和 trace 均逐式证明。
root 推导；o1_theta 独立纸核 (T.2)–(T.11) 的原函数域、
Fermat 三根、目标模型、相对 trace 尺度和两个最高系数。
