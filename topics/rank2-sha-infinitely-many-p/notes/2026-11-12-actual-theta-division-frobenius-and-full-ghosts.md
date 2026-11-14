# 原 theta 除法多项式、真正 Frobenius 提升与全部精度的连接

日期：2026-11-12。**状态：以下整除法多项式、真实拉回恒等式和全精度
展开已证明。** 原两分子 $P,Q$ 及正 theta 次数始终保留。
本文不将其改成 Mellin 乘法，也未证明原有限次数源在该拉回下闭合。

## 1. 标准除法多项式给出的整 theta 倍乘

保留 R162 的 $E_0:y^2=x^3-x$、$u=x^{-1/2}$、
$s=u^4=x^{-2}$、$\vartheta=\sigma/u$，原点规范为
$u(z)=z+\cdots$、$\vartheta(0)=1$。

对正奇数 $n$，令 $\psi_n(x)$ 为标准除法多项式，首项
$n x^{(n^2-1)/2}$，并令

$$
\phi_n=x\psi_n^2-\psi_{n-1}\psi_{n+1},\qquad
x([n]P)=\frac{\phi_n(x(P))}{\psi_n(x(P))^2}.
\tag{1.1}
$$

这里 $\phi_n\in\mathbb Z[x]$ 为次数 $n^2$ 的首一多项式。
这些整系数及首项事实、倍乘坐标式见 Stange [1] §2、
Proposition 2.2；本篇下面的平方、模 $p$ 及常数规范另作证明。

**引理。** 存在唯一首一 $h_n(x)\in\mathbb Z[x]$ 使

$$
\phi_n(x)=x h_n(x)^2,\qquad
\deg h_n=(n^2-1)/2.
\tag{1.2}
$$

而且

$$
H_n(s):=x^{-(n^2-1)/2}h_n(x)\in\mathbb Z[s],\qquad H_n(0)=1,
\tag{1.3}
$$

$$
\boxed{\qquad
\vartheta(nz)=H_n(s(z))\,\vartheta(z)^{n^2}.
\qquad}
\tag{1.4}
$$

**证明。** 令 $T=(0,0)$。奇数倍乘使 $[n]T=T$；
$[n]^{-1}T$ 的其余点按 $\{P,-P\}$ 配对，且均不是二挠点。
在 $T$ 处，$x$ 的零阶是二，所以 $\phi_n$ 的 $x=0$ 根为一重。
在其余原像处，$x$ 是局部参数而 $x\circ[n]$ 有二重零，
所以 $\phi_n$ 的每个非零根都是二重。
这些点不在 $[n]^{-1}O$，故与分母没有公共零点。
因此 $\phi_n/x$ 是首一多项式的平方。唯一首一平方根被 Galois 固定，
属于 $\mathbb Q[x]$；它又整于 $\mathbb Z[x]$，由后者整闭得
$h_n\in\mathbb Z[x]$。

自同构 $[i]:(x,y)\mapsto(-x,iy)$ 与 $[n]$ 交换。
$\psi_n$ 是偶多项式，$\phi_n$ 是奇多项式；这也可由
标准除法多项式的权齐次性直接看出。
唯一首一平方根 $h_n$ 因而是偶多项式。
因 $(n^2-1)/2$ 为偶数，(1.3) 确实是 $s=x^{-2}$ 的整多项式，
常数项为一。

奇数 $n$ 的标准 sigma 倍乘规范为
$\sigma(nz)=\psi_n(x(z))\sigma(z)^{n^2}$。
这可由两边除子及原点首项 $n z^{1-n^2}$ 固定；
一般倍乘式亦见 [1] (2.3)，此处无偶数符号歧义。
用 $\vartheta^2=x\sigma^2$，得到

$$
\left(\frac{\vartheta(nz)}{\vartheta(z)^{n^2}}\right)^2
=\frac{\phi_n(x)}{x^{n^2}}=H_n(s)^2.
$$

两边原点值均为一，形式平方根唯一，给 (1.4)。$\square$

相应地定义整多项式

$$
D_n(s)=x^{-(n^2-1)/2}\psi_n(x),\qquad D_n(0)=n.
\tag{1.5}
$$

其整性与 $H_n$ 相同。真正的源参数倍乘准确为

$$
\boxed{\qquad
s(nz)=\Phi_n(s):=
s\left(\frac{D_n(s)}{H_n(s)}\right)^4.
\qquad}
\tag{1.6}
$$

这是 (1.1)–(1.3) 直接平方所得，原点首项为 $n^4s$。
例如 $n=3$ 时
$D_3=3-6s-s^2$、$H_3=1+6s-3s^2$；
这个例子仅校准常数与坐标方向。

## 2. 惰性特殊纤维：排除竖直常数的完整证明

现在令 $p\ge7$、$p\equiv3\pmod4$。
对 $E_0/\mathbb F_p$，配对 $x$ 与 $-x$ 给 $a_p(E_0)=0$，
于是 Frobenius 特征式为 $\operatorname{Fr}_p^2+[p]=0$。
因此

$$
x([p]P)=x(P)^{p^2}
\quad\text{在 }\mathbb F_p(E_0)\text{ 中}.
\tag{2.1}
$$

这里不能仅由除子约化猜测一个常数单位；需要检查标准多项式的
竖直因子。事实上对所有正奇数 $n$，

$$
\psi_n(0)=(-1)^{(n-1)/2}.
\tag{2.2}
$$

证明只用 $\psi_1(0)=1$、$\psi_3(0)=-1$、偶数除法多项式含因子
$2y$，以及
$\psi_{2m+1}=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3$。
将 $m$ 分成奇偶，正好分别得到 $n\equiv3$ 与 $1\pmod4$ 的符号。
故惰性 $p$ 的 $\psi_p(0)=-1$，其特殊纤维不是零多项式。

因而可在 (1.1) 约化后使用 (2.1)，得到多项式恒等式

$$
\overline{\phi_p}=x^{p^2}\overline{\psi_p}^{\,2}.
$$

左边仍是次数 $p^2$ 的首一多项式，右边分母已经排除了恒零。
比较次数，再用 (2.2)，准确得到

$$
\overline{\psi_p}=-1,\qquad
\overline{\phi_p}=x^{p^2},\qquad
\overline{h_p}=x^{(p^2-1)/2}.
\tag{2.3}
$$

最后一个等式由 (1.2) 及首一规范固定符号。因此

$$
\boxed{\quad
H_p(s)\equiv1\pmod p,\qquad
D_p(s)\equiv-s^{(p^2-1)/4}\pmod p,
\qquad \Phi_p(s)\equiv s^{p^2}\pmod p.
\quad}
\tag{2.4}
$$

所有式子都是整系数多项式／形式级数的约化；
特别 $\Phi_p\in s\mathbb Z_p[[s]]$，且 $\Phi_p'(0)=p^4$。

## 3. 保完整固定分子的连接单位

记 R162/R163 的同一个输入

$$
\mathcal A=P(s)e^{W(s)}=sZ(s),\quad
B=Q(s)e^{W(s)},\quad
Z=p_0e^W,\quad G=\log Z,\quad p_0=P/s.
$$

(1.4) 准确给出

$$
W(\Phi_p(s))-p^2W(s)=68\log H_p(s).
\tag{3.1}
$$

于是定义

$$
\mathscr U_p(s)=
\frac{p_0(\Phi_p(s))H_p(s)^{68}}{p_0(s)^{p^2}}.
$$

由于 $p_0\in1+s\mathbb Z_p[s]$、(2.4) 以及
$p_0(s^{p^2})\equiv p_0(s)^{p^2}\pmod p$，有真正的全系数关系

$$
\boxed{\quad
\frac{Z(\Phi_p(s))}{Z(s)^{p^2}}
=\mathscr U_p(s)\in1+ps\mathbb Z_p[[s]].
\quad}
\tag{3.2}
$$

对原两条行自身，准确式仍是

$$
\begin{aligned}
\mathcal A(\Phi_p)
 &=\mathcal A^{p^2}\,
       \frac{P(\Phi_p)H_p^{68}}{P^{p^2}},\\
B(\Phi_p)
 &=B^{p^2}\,
       \frac{Q(\Phi_p)H_p^{68}}{Q^{p^2}}.
\end{aligned}
\tag{3.3}
$$

这里 $P$、$Q$ 都在原点有一阶零。
因此 (3.3) 的显示商各含 $s^{1-p^2}$ 型因子，
不能把它们称为 (3.2) 那种原点整单位。
两式相除才给实际的 $Q/P$ 在 $[p]$ 下的有理拉回。
原分子和正 theta 次数没有被删除。

## 4. 真正可迭代的全部精度展开

令

$$
\mathscr L_p(s)=-\frac1p\log\mathscr U_p(s)
\in s\mathbb Z_p[[s]].
\tag{4.1}
$$

其整性来自 $\mathscr U_p-1\in ps\mathbb Z_p[[s]]$：
形式对数第 $j$ 项除以 $p$ 后的赋值至少
$j-1-v_p(j)\ge0$。由 (3.2) 得

$$
G(s)=\frac1p\mathscr L_p(s)+\frac1{p^2}G(\Phi_p(s)).
\tag{4.2}
$$

所以对每个 $h\ge1$ 有准确有限恒等式

$$
\boxed{\quad
G(s)=\sum_{j=0}^{h-1}
 \frac{\mathscr L_p(\Phi_p^{\circ j}(s))}{p^{2j+1}}
 +\frac{G(\Phi_p^{\circ h}(s))}{p^{2h}}.
\quad}
\tag{4.3}
$$

最后一项逐系数趋于零，因而也有逐系数 $p$ 进收敛的全展开

$$
G(s)=\sum_{j\ge0}
 \frac{\mathscr L_p(\Phi_p^{\circ j}(s))}{p^{2j+1}}.
\tag{4.4}
$$

为严证余项，固定截断次数 $M$。
$\Phi_p^{\circ h}(s)$ 正是 $u(p^h z)^4$ 用 $s=u(z)^4$ 表示。
将固定 $\exp_E$ 及 $\log_E$ 截到所需有限次数后，
每个系数是 $p^h$ 的有理多项式，且每个单项至少含其四次幂。
故有与 $h$ 无关的常数 $C_{p,M}$，使

$$
v_p([s^m]\Phi_p^{\circ h})\ge4h-C_{p,M}
\qquad(1\le m\le M).
$$

再与固定 $G$ 复合，仍有相同形式的下界，
除以 $p^{2h}$ 后至少为 $2h-C'_{p,M}\to+\infty$。
这证明 (4.4)，但没有把这里依赖 $M$ 的常数称为已经得到的
统一小精度成本。

## 5. 第一层确实只有一个 p

置 $r=(p+1)/4$，并沿 R160 的准确规范取

$$
C_p=p[s^{r-1}]W'(s)\pmod p\ne0.
$$

则原连接满足

$$
\boxed{\quad
\mathscr L_p(s)\equiv(C_p/r)s^r+O(s^{r+1})\pmod p.
\quad}
\tag{5.1}
$$

证明如下。R163 的精确赋值给
$[s^m]G$ 在 $m<r$ 时整，在 $m=r$ 时恰有一层分母，且
$p[s^r]G\equiv C_p/r$。
由 (2.4)，$D_p/H_p$ 在小于 $r$ 的次数处均被 $p$ 除，
因为 $r<(p^2-1)/4$。
于是 $\Phi_p=s(D_p/H_p)^4$ 到 $s^r$ 的系数均在
$p^4\mathbb Z_p$。所以 $G(\Phi_p)$ 在所需次数上被 $p^4$ 除，
再用
$\mathscr L_p=pG-G(\Phi_p)/p$ 即得 (5.1)。

因此 $\mathscr U_p\in1+p$ 的层数是真实的；
不能将本例无条件提升成 $1+p^2$。
这与 R160 中 $\exp(pW)$ 的首次指数进位一致，也与 R163
在偶次幂截断上保留的一层余量一致。

## 6. 对原平面源的已付作用与剩余问题

对同一个实际 theta 次数 $j$，拉回公式是

$$
[p]^*(\vartheta^{68j}f(s))
=\vartheta^{68p^2j}H_p(s)^{68j}f(\Phi_p(s)).
\tag{6.1}
$$

因此它真实地把 theta 次数 $j$ 改成 $p^2j$，
并运输原分子。它不是在固定 $j$ 的原两维空间
$\langle P,Q\rangle$ 内的一个未经证明的矩阵作用。
同样，原列 $\mathcal A^jV^c$ 仍必须按 $0\le c\le j\le D$
放回同一前缀格，不能由 (3.2) 自由增加任何分子列。

(4.3) 提供了保留真实 Frobenius 提升和完整连接的全精度输入；
但把它变成 R159 所需的饱和前缀收益，仍须控制 (6.1)
的实际次数和分子格。它本身不使用两个原中央 Mellin 条件，
也没有将中央投影当成乘法同态。

## 来源与依赖

[1] Katherine E. Stange, *Integral Points on Elliptic Curves and Explicit
Valuations of Division Polynomials*, Canadian Journal of Mathematics
68 (2016), 1120–1158，§2、Proposition 2.2 与 (2.3)。
[出版版](https://doi.org/10.4153/CJM-2015-005-0)。
本文仅借用标准除法多项式的整性、坐标式、首项及 sigma 倍乘规范；
特殊的平方、竖直常数、整 Frobenius 关系和收敛均在上文证明。

原固定 $P,Q,W$ 及源格见
[R162](2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)；
精确惰性赋值见
[R163](2026-11-12-actual-theta-inert-valuation-and-even-power-jet-resonance.md)，
首 carry 规范见
[R160](2026-11-12-inert-theta-carry-and-common-degree-spectrum.md)。
