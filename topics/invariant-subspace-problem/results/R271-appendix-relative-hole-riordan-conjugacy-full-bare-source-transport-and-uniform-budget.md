# R271 附录：相对孔层 Riordan 共轭、完整与裸右域的同源运输及一致常数

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。相对层数 $j=1,\ldots,h$ 与真实删除行给出不含 $D^\dagger$ 的有限 Riordan 共轭。它保持全部物理头旗及尾旗，下降到原裸商，并准确运输首段源与完整最小 Gram。对两个原头函数，另选稍小的尾半径后，共轭及其逆有一个与 $m,n,h$ 无关的有限常数。这个常数很大，不称共轭接近单位。

本文没有删除并头的强位 $D_<$。新头准确是 $\psi_m(A_m+D_<)/d_0$，不是 $B_m/d_0+D_<$。同样没有把右窗口的相对层共轭直接推广到整个左前缀，或从两端 Gram 比较相减得到返回预算。

依赖：

- [强尾同源流、完整域与裸商](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
- [首段损耗与真源圆盘演算](R271-appendix-first-row-observability-loss-exact-source-contraction-and-disk-calculus.md)；
- [完整返回的物理系统](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)；
- 原头函数及系数使用[真实逆芽原式](../notes/2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)。

## 1. 真实相对层环境

固定 $m,R,n$，写
$$
C=A_m+D_<,\qquad h=d+R,\qquad C^h=0,\qquad
D=D_>,\qquad \delta=\|D\|.
$$
仍取同一完整右环境
$$
\mathscr W=\bigoplus_{j=1}^{h}
 \bigl(\ker C^{h-j+1}\otimes E_{h,n+j}\bigr),
\qquad
E_{a,p}=\ker D^a\cap\mathcal H_p^>.
\tag{1.1}
$$
其头内积、所有尾孔层和真核旗不变。定义
$$
(\mathcal T x)_j=Dx_{j+1}\quad(j<h),\qquad
(\mathcal T x)_h=0,\qquad
Jx_j=jx_j.
$$
于是
$$
\mathcal T^h=0,\qquad \|\mathcal T\|\le\delta,\qquad
[J,\mathcal T]=-\mathcal T.
\tag{1.2}
$$
$J$ 的本征值是相对层数 $1,\ldots,h$，不是绝对孔数 $n+j$。

两算子均保持 (1.1)。具体地，$\mathcal T^k$ 将第 $j+k$ 段送到第 $j$ 段，原头核
$\ker C^{h-j-k+1}$ 包含于 $\ker C^{h-j+1}$，而 $D^k$ 保持 $\ker D^h$。

原高出生空间
$$
\mathscr W^{\rm hi}
=\bigoplus_{j=1}^{h}
 \ker C^{h-j+1}\otimes E_{j-1,n+j}
\tag{1.3}
$$
也被 $J,\mathcal T$ 保持。其正交商仍以
$P=P^{\rm lo}$ 的原物理代表实现；商删除行是
$\overline{\mathcal T}=P\mathcal T|_{P\mathscr W}$。
由于 $J$ 与 $P$ 交换，商上也有
$[J,\overline{\mathcal T}]=-\overline{\mathcal T}$。

## 2. 不使用任何尾逆的有限共轭

设 $\phi(z)=z\,a(z)$ 为零点解析芽，$a(0)=1$。定义
$$
p_k(t)=[z^k]a(z)^t,\qquad
K_\phi=\sum_{k=0}^{h-1}p_k(J)\mathcal T^k.
\tag{2.1}
$$
在 (2.1) 中 $J$ 作用于输出行。逐行公式是
$$
(K_\phi x)_j
=\sum_{k=0}^{h-j}[z^k]a(z)^j\,D^k x_{j+k}.
\tag{2.2}
$$
这是有限和，仅使用真实删除幂；不含原像、最小逆或创造算子。

直接比较第 $j$ 行、总降阶 $k+1$ 的系数，有
$$
[z^k]a(z)^{j+1}
=[z^{k+1}]a(z)^j\phi(z).
$$
所以
$$
\boxed{\mathcal T K_\phi=K_\phi\phi(\mathcal T).}
\tag{2.3}
$$

同一系数求和还给复合律
$$
K_\phi K_\chi=K_{\phi\circ\chi}.
\tag{2.4}
$$
例如其第 $j$ 行总降阶 $r$ 系数为
$$
\begin{aligned}
\sum_{k=0}^r
 [z^k]a_\phi(z)^j\,
 [z^{r-k}]a_\chi(z)^{j+k}
&=[z^r]a_\chi(z)^j a_\phi(\chi(z))^j\\
&=[z^r]\left(\frac{\phi(\chi(z))}{z}\right)^j .
\end{aligned}
$$
因 $\phi'(0)=1$，存在唯一形式逆芽 $\chi=\phi^{-1}$，故
$$
\boxed{K_\phi^{-1}=K_{\phi^{-1}}.}
\tag{2.5}
$$
有限 nilpotence 意味着这里只读取有限个系数；不存在未证明的全环境级数收敛。

$K_\phi$、其逆均保持 (1.3)，所以它们诱导的真实裸商算子
$$
\overline K_\phi=P K_\phi|_{P\mathscr W}
=\sum_{k<h}p_k(J)\overline{\mathcal T}^{\,k}
$$
互为有界逆。其范数不大于相应完整环境范数。此处没有把环境先取核与先取商免费认同；下一节分别核两个原域。

## 3. 完整／裸核和首段源一起运输

先一般地取两个同头算子 $C_0,\widehat C$，满足
$$
\widehat C=-\phi(-C_0)
=C_0a(-C_0).
\tag{3.1}
$$
它们都是至多 $h$ 阶 nilpotent。因 $a(-C_0)$ 可逆并与 $C_0$ 交换，全部头旗准确相同：
$$
\ker\widehat C^{\,k}=\ker C_0^k\qquad(k\ge0).
$$
故它们可在同一个 (1.1) 中比较。

$K_\phi$ 与头算子交换，(2.3) 给
$$
(\widehat C+\mathcal T)K_\phi
=K_\phi(\widehat C+\phi(\mathcal T)).
$$
另一方面
$$
\widehat C+\phi(\mathcal T)
=\phi(\mathcal T)-\phi(-C_0)
=(C_0+\mathcal T)\,\phi^{[1]}(\mathcal T,-C_0).
\tag{3.2}
$$
最后因子是常项为 $1$ 的、两个交换 nilpotent 算子的多项式，因而可逆，并与 $C_0+\mathcal T$ 交换。由此得到完整内部及末端方程的双向等价：
$$
K_\phi:\ker(C_0+\mathcal T)
 \longrightarrow\ker(\widehat C+\mathcal T).
\tag{3.3}
$$
在裸商中以 $\overline{\mathcal T}$ 重复同一原式，得到裸域的双向等价；全部头旗和末端均保留。

还必须核源。对完整链 $x$，令 $r=Dx_1$。内部方程逐次给
$$
D^j x_j=(-C_0)^{j-1}r.
\tag{3.4}
$$
因 $p_k(1)=[z^k]a(z)$，(2.2) 的第一行给
$$
\boxed{
F K_\phi x
=a(-C_0)r=:g(C_0)r.
}
\tag{3.5}
$$
对裸链同样有 (3.4)：逐次压掉的高部分在相应 $\ker D^{j-1}$ 中，再施所需删除幂后严格为零。因此
$$
\boxed{
F_b\overline K_\phi x=g(C_0)F_bx.
}
\tag{3.6}
$$
这同时证明完整及裸零源核被准确送到对应的新零源核。

两个真实源空间相同。确实，旧源空间对 $C_0$ 及其多项式保持；$g(C_0)$ 和逆都是可逆的常项 $1$ 多项式，故保持旧源空间。再由 (3.3)–(3.6) 的满射及逆向式，新旧源像相等。这里没有换成某个较小 primitive 输入族。

## 4. 物理范数及真实最小 Gram 的条件比较

对 $a(z)=1+\sum_{\ell\ge1}a_\ell z^\ell$ 置
$$
U_\phi(t)=\sum_{\ell\ge1}|a_\ell|t^\ell.
$$
若该和在 $t=\delta$ 有限，则非负系数 majorant
$(1+\sum_{\ell\ge1}|a_\ell|z^\ell)^h$
逐项支配所有 $a(z)^j$，$1\le j\le h$。所以
$$
\|K_\phi\|
\le(1+U_\phi(\delta))^h
\le e^{hU_\phi(\delta)}.
\tag{4.1}
$$
同式适用于逆芽。商上的范数满足同一上界。

假设
$$
\|K_\phi\|,\ \|K_\phi^{-1}\|\le\mathcal C.
$$
令 $H_0,B_0$ 为 $C_0$ 的完整／裸最小右 Gram，
$\widehat H,\widehat B$ 为 $\widehat C$ 的对应 Gram。对完整可行集先使用 (3.5)，再取真实最小值；逆向用 $K_\phi^{-1}$。裸域用 (3.6)。得到同一个源上的准确比较
$$
\boxed{
\begin{aligned}
\mathcal C^{-2}H_0
&\preceq g(C_0)^*\widehat H\,g(C_0)
\preceq\mathcal C^2H_0,\\
\mathcal C^{-2}B_0
&\preceq g(C_0)^*\widehat B\,g(C_0)
\preceq\mathcal C^2B_0 .
\end{aligned}}
\tag{4.2}
$$
所有最小化都在原完整核／完整裸域中进行，包含全部零源及高返回。没有先压缩逆。

特别，若另有 $\widehat H\preceq\kappa\widehat B$ 的真实证明，(4.2) 才能给
$H_0\preceq\mathcal C^4\kappa B_0$。仅有 (4.2) 本身不能相减成
$\widehat H-\widehat B$ 与 $H_0-B_0$ 的序比较。

## 5. 两个原函数的统一参数

仍用原系数
$$
d=2^m,\quad m\ge10,\quad d_0=e^{-20},\quad
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i,\quad d_i=e^{-\Lambda_i},
$$
以及原 $F_{N,m},F_{Y,m}$。取
$$
q=d/2,\qquad
\tau=\frac{\Lambda_{m-1}+14d^3+\log16}{q-1},
\qquad
R=\lceil4e^\tau\rceil,\qquad h=d+R .
\tag{5.1}
$$
原远尾满足 $\delta\le1/(m+R)\le1/R$。准确除法给
$$
\tau=\frac{25}{2}d^3+\frac{107}{4}d^2+\frac{107}{2}d
 +150m-18+\frac{300m-36+2\log16}{d-2}.
\tag{5.2}
$$
对 $m\ge10$，由原 $\Lambda_{m-1}\ge6d^4$ 以及 (5.2)，
$$
12d^3\le\tau\le\frac{25}{2}d^3+27d^2\le13d^3,
\qquad h\le2R .
\tag{5.3}
$$
(5.2) 到中间上界的余量为
$d^2/4-(107/2)d-150m+18-(300m-36+2\log16)/(d-2)>0$；
在 $d\ge1024$ 可分别以 $d^2/16,d^2/32,d^2/32$ 控制后三个正量。

令
$$
\phi(z)=-\psi_m(-z)/d_0,\qquad
\chi(z)=\phi^{-1}(z)=-F_m(-d_0z).
\tag{5.4}
$$
两者首阶系数均为 $1$。下面先直接估计显式的 $\chi$，再估其逆；不把整个非线性粗记成一个 $h\varepsilon_m$。

置
$$
c_2=\frac{b_1d_0^2}{d_1}=\frac14e^{1070},
\qquad
M_0=16(1+e^{1070}).
\tag{5.5}
$$
这个固定二次系数很大，但不依赖 $m$。

取 $x=2\delta\le2/R$。$N$ 模型的 $\chi(z)/z-1$ 由
$i\ge1$ 项给出。$Y$ 模型还含最低位的 $z/(1-z)$，其非线性绝对和为
$x/(1-x)$。所有其余 Cayley 分母的绝对倒数至多损因子 $2$：最低位 $x<1/2$，$i=1$ 由
$4c_2x^2<1/2$，$i\ge2$ 由下列更强指数界直接保证。

最低有理项与固定二次项分别满足
$$
h\frac{x}{1-x}\le8,\qquad
2h c_2x\le8c_2.
\tag{5.6}
$$
对 $i\ge2$ 令 $q_i=2^i\ge4$。统一包含 Cayley 的因子 $2$，有
$$
2h\,b_i\frac{d_0^{q_i}x^{q_i-1}}{d_i}
\le e^{\Lambda_i-(q_i-2)\tau}.
\tag{5.7}
$$
确实，$h\le2R$、$R\ge4e^\tau$ 使额外常数至多
$2^{5-q_i}e^{-20q_i}\le1$。

对 $2\le i\le m-2$，原
$\Lambda_i\le(25/16)d^3q_i$ 与 $\tau\ge12d^3$ 给
$$
\Lambda_i-(q_i-2)\tau
\le\left(24-\frac{167}{16}q_i\right)d^3
\le-\frac{71}{4}d^3 .
\tag{5.8}
$$
最高位则准确满足
$$
\Lambda_{m-1}-(q-2)\tau
=\tau-14d^3-\log16
\le-d^3-\log16.
\tag{5.9}
$$
这些量求和小于 $1$。合并得到
$$
\boxed{h\,U_\chi(2\delta)\le9+8c_2<M_0.}
\tag{5.10}
$$
由于 $h\ge4e^{12d^3}$，还严格有 $U_\chi(2\delta)<1/8$。

为估逆芽，写
$\chi(z)=z+\sum_{\ell\ge2}c_\ell z^\ell$。
$\phi$ 的绝对系数被正系数形式解
$$
y=z+\sum_{\ell\ge2}|c_\ell|y^\ell
$$
逐阶支配。对实 $z=\delta$ 从 $y_0=\delta$ 单调迭代，(5.10) 保证
$y_k\le2\delta$，所以该正级数在 $\delta$ 收敛，且
$$
y-\delta\le2\delta\,U_\chi(2\delta).
$$
因此
$$
U_\phi(\delta)\le2U_\chi(2\delta).
\tag{5.11}
$$
这是同一真实形式逆的绝对系数预算，不调用任意替换模型。

由 (4.1)、(5.10)–(5.11)，完整及裸窗口均有
$$
\boxed{
\|K_\phi\|,\ \|K_\phi^{-1}\|,\
\|\overline K_\phi\|,\ \|\overline K_\phi^{-1}\|
\le\mathcal C_0:=e^{2M_0}.
}
\tag{5.12}
$$
常数与绝对切口 $n$、原头数 $m$ 和强位数 $R$ 无关。它不是小常数；
(5.12) 不含 $K_\phi-I\to0$ 的结论。

## 6. 对原强联块的准确作用及窗口

对原
$$
C_0=A_m+D_<,\qquad C_0^h=0
$$
使用 (5.4)。新头和源准确为
$$
\boxed{
\widehat C=\psi_m(C_0)/d_0,\qquad
g(C_0)=\frac{\psi_m(C_0)}{d_0C_0}.
}
\tag{6.1}
$$
全部函数按 $<h$ 阶代入；商在零点取常项 $1$。新旧头的核旗完全相同，
但其算子和完整左前缀度量一般不同。

在旧源的四个已付右／联合度量 $B_0,H_0,L_0+B_0,L_0+H_0$ 中，
$C_{0,s}$ 是 $\delta$ 收缩。于是
$$
\boxed{
\|g(C_{0,s})-I\|
\le U_\phi(\delta)\le2M_0/h
}
\tag{6.2}
$$
分别在这四个度量中成立。(4.2) 及 (5.12) 是原同一个源的完整／裸右费用比较，不含全左 $L_0$ 的免费运输。

取原带权母窗口
$$
Q_*=\left\lfloor e^{(1601/64)d^3}\right\rfloor .
$$
(5.1)–(5.3) 给 $h\le6e^\tau$、$R\le5e^\tau$；因此
$2h+R<Q_*/2$ 对 $m\ge10$ 成立，原
$n+2h+R<Q_*$ 的同一来源窗口仍可使用。并且
$$
\boxed{
\frac{h^2}{Q_*}
\le72\exp\!\left(-\frac{d^3}{64}+54d^2\right)
\longrightarrow0 .
}
\tag{6.3}
$$
所以固定的 $\mathcal C_0$ 因子不会破坏后续所需
$\kappa_m=O(h)$ 的窗口量级。这里没有断言该 $\kappa_m$ 已证明。

最后明确两个不能省掉的部分。首先，即使
$\psi_m(A_m)=B_m$，一般也有
$$
\psi_m(A_m+D_<)\ne B_m+d_0D_< .
$$
(6.1) 保留全部强位混合项，不能把它改写成一个已经解决的线性头加原强位。
其次，$J$ 在本文只取右段的 $1,\ldots,h$；若把它直接搬到整个左前缀，
相对层数会跨到大小为 $n$ 的负值，(5.12) 不再是该算子的范数证明。
真实返回主配对、普通右封口及原 $N=M$ 仍需后续同源预算。
