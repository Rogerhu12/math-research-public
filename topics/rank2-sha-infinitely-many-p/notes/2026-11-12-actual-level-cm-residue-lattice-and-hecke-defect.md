# 原全级截面的 CM 留数格与实际 Hecke 缺项

日期：2026-11-12。状态：原全 $68$ 级形式的权三提升、全部 CM
标记上的留数、一层 $p$ 分母的尖锐性，以及这个提升不保持原
Hecke 零关系，均已证明。所选中央留数仍准确保留；本文没有证明
它在无穷多个素数处非零。

## 1. 保留原截面的全局提升

取原来的全 $N=68$ 级模曲线的一个几何连通分支 $X$，
在固定数域上使 Weil 配对和所需标签有定义。记尖点除子为 $Z$，
并用
$$
\lambda:X\longrightarrow X(2)=\mathbb P^1,\qquad
t=\lambda-\tfrac12,\qquad s=1-4t^2
$$
表示遗忘映射。此映射只在尖点分歧。记
$$
D=\deg(\lambda),\qquad \mathcal C=\lambda^{-1}(\tfrac12).
\tag{1.1}
$$
因 $68$ 是偶数，这里的有序 $2$ 阶标记已包含在全级结构中。
所以 $\mathcal C$ 是有 $D$ 个几何点的有限 étale 纤维。

实际权一截面记为 $\mathfrak f_e$。在 Legendre 微分
$\omega=dx/(2y)$ 的框架下，
$$
\mathfrak f_e=M_e\omega.
\tag{1.2}
$$
它是 [R82 的原 $F_e$](2026-11-12-actual-weight-one-hecke-and-character-decomposition.md)
在撤去仅用于整数 $q$ 展开的固定 $\tau\mapsto68\tau$ 后的截面。
没有将 $M_e$ 的一个 Taylor 多项式另当作全局模形式。
在原标记点 $x_0\in\mathcal C$，
$$
M_{x_0}(t)=M_e(t)=t^4+\tfrac72t^6+\cdots.
\tag{1.3}
$$
对其它 $x\in\mathcal C$，用 $M_x(t)$ 表示同一个截面
$\mathfrak f_e$ 在该标记分支的 Legendre 系数。
不预先假设它仍为偶函数或有四阶零点。

固定惰性 $p\ge7$，置 $d=p+1$。沿用真实周期
$$
Y=\begin{pmatrix}K&L\\K'&L'\end{pmatrix},\qquad
J=L/t,\qquad KL'-K'L=s^{-1},
$$
并定义有限的、系数 $p$ 整的核
$$
S_p(t)=
\left[\frac{K(t)^p}{s(t)J(t)^{p+2}}\right]_{\le p-3}
\in\mathbb Z_p[t],\qquad S_p(0)=1.
\tag{1.4}
$$
只有次数 $<p$ 的周期系数用于此式，因此其整性不含额外假设。
这与 Hermite 笔记的 $R_p$ 相差一个 $K$ 因子；本篇单独命名为
$S_p$，以免混淆。

真正保留原全级截面的 $\mathcal E=H^1_{\rm dR}$ 值一形式为
$$
\boxed{\qquad
\nu_p=\frac{S_p(t)}{t^{p+2}}\,\mathfrak f_e\,dt.
\qquad}
\tag{1.5}
$$
经 Kodaira--Spencer 同构，这是权三的亚纯尖形式。
在解析记号中，其标量式是
$F_e^{\rm unscaled}D_\tau t\,S_p(t)t^{-p-2}$，
其中 $D_\tau=(2\pi i)^{-1}\partial_\tau$。

内点极点全部在 $\mathcal C$。尖点条件也可直接核对：
在 $\lambda=0,1$ 处，$t$ 是单位，而 $D_\tau\lambda$
至少有一阶零点；在 $\lambda=\infty$ 处，
$D_\tau\lambda$ 与 $\lambda$ 有同样的极点阶，
而 $S_pt^{-p-2}=O(t^{-5})$。
原 $F_e$ 在所有尖点全纯，故新形式在这些尖点均消失。

## 2. 其它 CM 标记不能一起消失

令 $\boldsymbol\omega$ 为紧化模曲线的 Hodge 线丛。
Kodaira--Spencer 与遗忘映射的对数 Riemann--Hurwitz 给
$$
\boldsymbol\omega^{\otimes2}\simeq\Omega_X^1(\log Z),
\qquad
\deg\Omega_X^1(\log Z)
=D\,\deg\Omega_{\mathbb P^1}^1(\log\{0,1,\infty\})=D.
$$
因此
$$
\boxed{\deg\boldsymbol\omega=D/2.}
\tag{2.1}
$$
原截面非零，由 (1.3) 已可知。非零全纯截面的零除子次数是
$D/2$，所以在 $\mathcal C$ 的 $D$ 个点中，至多 $D/2$ 个能是零点。
特别，不能把原分支的四阶消失推广到整个 CM 纤维。

这个结论还能在每一个本题的好惰性素数上应用，而不用另外排除
一个未确定有限集。理由如下。

1. 在开模曲线上，[固定除法函数模型](2026-11-12-weight-one-division-unit-relative-model.md)
   将所有 $U_P$ 写成
   $-D_\lambda^2\Psi_{68}(P)/(2\cdot68^2D_\lambda\Psi_{68}(P))$。
   $68$ 阶挠点在这些好位互异，分母是单位。
2. 在任意尖点，运输标签后仍是同一个 completed-zeta Fourier
   展开。当第二标签非零时，常数和系数的分母只来自 $2N$；
   当第二标签为零时，只另出现 $1-\zeta_N^a$。
   这些数的非单位素因子只在 $2,17$。本题的固定规范常数另只
   排除 $3,5$。所以 $\mathfrak f_e$ 是每个 $p\ge7,\ p\ne17$
   的整 Hodge 截面。
3. 全级模曲线在 $p\nmid68$ 时有光滑整模型，$\mathcal C$ 仍为
   $D$ 个几何点的 étale 纤维，Hodge 次数不变。
   (1.3) 的 $t^4$ 系数为 $1$，使约化截面非零。

在特殊纤维对同一零除子次数计数，得到
$$
\boxed{\quad
\#\{x\in\mathcal C(\overline{\mathbb F}_p):
          M_x(0)\not\equiv0\pmod p\}\ \ge D/2.
\quad}
\tag{2.2}
$$
可在包含这些级结构的有限未分歧扩张 $B$ 上逐点使用此式。
这里非零点可以随 $p$ 改变；不需要强行指定一个对所有 $p$
都为单位的代数数。

若要具体数目，$|\mathrm{SL}_2(\mathbb Z/68)|=48\cdot4896$，
在遗忘有序 $2$ 阶结构及中心符号后
$D=48\cdot4896/(6\cdot2)=19584$。
因此 (2.2) 的下界为 $9792$；后面的证明只用正下界。

## 3. 全部标记的准确留数与尖锐分母

在每个 $x\in\mathcal C$，采用同一底层 Legendre 曲线的整初值基
$e=(\omega,\eta)$，$\eta=\nabla_{\partial_t}\omega$，
以及初值为单位矩阵的水平基 $h=Y^{-1}e$。
于是 $\omega=Kh_1+Lh_2$。记 $\nu_p$ 的水平留数向量为
$$
\operatorname{Res}_x\nu_p=(A_{x,p},B_{x,p}).
$$
完全直接地，
$$
\boxed{
\begin{aligned}
A_{x,p}&=[t^d]\,M_x(t)S_p(t)K(t),\\
B_{x,p}&=[t^d]\,M_x(t)S_p(t)L(t).
\end{aligned}}
\tag{3.1}
$$

在原分支，(1.3)--(1.4) 给
$$
\boxed{\operatorname{Res}_{x_0}\nu_p=(C_{p+1},0).}
\tag{3.2}
$$
第一坐标正是
$[t^d]M_eK^d/(sJ^{d+1})$；
核的截断误差乘 $M_e=O(t^4)$ 后不影响该系数。
第二坐标由奇偶性为零。因此原中央行没有丢失。

但在整个 CM 纤维上的整格不同。
[临界 Gauss 约化](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)
已证明
$$
[t^d]K=\kappa_p/p,\qquad
\kappa_p\in\mathbb Z_p^\times,
$$
且 $K$ 的次数 $<d$ 的系数均整；$L$ 的次数 $\le d$ 的系数也均整。
把 $\kappa_p$ 取为这里准确的 $p[t^d]K$，而非仅其剩余类。
由 (1.4)、$M_x\in\mathcal O_B[[t]]$，(3.1) 立即给
$$
\boxed{\qquad
A_{x,p}\in p^{-1}\mathcal O_B,\qquad
pA_{x,p}\equiv\kappa_pM_x(0)\pmod p,\qquad
B_{x,p}\in\mathcal O_B.
\qquad}
\tag{3.3}
$$
唯一可能的非整贡献是
$[t^d]K\cdot S_p(0)M_x(0)$，没有忽略其它同阶项。

由 (2.2)，对每一个目标惰性素数，至少一个实际标记满足
$$
\boxed{v_pA_{x,p}=-1.}
\tag{3.4}
$$
因此整个留数向量恰需乘一个 $p$ 才整。
这个一层损失发生在同一个实际全级形式中，
不是仅由一般极点上界所允许的最坏情况。

整对数 de Rham 格也给同样的尖锐结论。
局部有整连接 $\nabla=d+\gamma(t)\,dt$；
将一个极点阶至多 $p+2$ 的整一形式减去
$\nabla(v_jt^{-j})$，可依次去掉高于一阶的极点，
每步只除以 $j$，$1\le j\le p+1$。
其中恰有一个非单位除数 $j=p$。
所以乘一个 $p$ 后，所有局部消元、对数代表及其重叠上的
Čech 差均整，给出整对数复形中的类。
反之，整对数类的留数在纤维整格中；
(3.4) 证明未经乘 $p$ 的类不可能已在该格中。

这也是 Allen--Long--Saad §4 Proposition 4.1 的本题直接证明：
其 $m!$ 成本在本次 $m=p+1$ 时恰含一个 $p$。
这里不使用该文引言中需另核符号约定的 ASD 赋值指数。

要特别区分：所选分支的 (3.2) 属于
$p\mathcal O_Bh_1$，而其它分支在 (3.4) 中属
$p^{-1}\mathcal O_Bh_1$。
整化后的全局类 $p[\nu_p]$ 模 $p$ 非零，
并不检测 $\Gamma_{i,p}=C_{p+1}/p$；
在所选分支，其留数已经属于 $p^2\mathcal O_Bh_1$。

## 4. 真正的 Hecke 交换子

把
$$
h_p(t)=S_p(t)t^{-p-2}
$$
看成基底上的有理函数。
对每条实际循环 $p$ 次同源
$\varphi_j:E_t\to E_{t_j}$，记
$$
\varphi_j^*\omega_j=c_j\omega,\qquad
t_j'=\frac{s(t_j)}{s(t)}\frac{c_j^2}{p}.
\tag{4.1}
$$
所有目标的 prime-to-$p$ 标记均按同源运输。
若需将它们写回原正式盘，就使用 R86 已核定的
$M_e/M_o$ 交换与规范单位，不能保持错误的原标签。
下式暂用 $M_e^{\rm tr}(t_j)$ 表示这个实际运输值。
若同源改变 Weil 配对所在的连通分支，则先在全级曲线的这些
共轭分支上取对应的同一截面，再按 R86 的系数作用识别；
没有假定 $p\equiv1\pmod{68}$。

对 $\mathcal E$ 值微分定义未归一的几何 Hecke 拉回和
$\mathscr T_p=\sum_j\varphi_j^*$。
逐项拉回 (1.5) 得到准确公式
$$
\boxed{\qquad
\mathscr T_p\nu_p
=\sum_j c_j\,M_e^{\rm tr}(t_j)\,
                 h_p(t_j)t_j'\,\omega\,dt.
\qquad}
\tag{4.2}
$$
这与原权一零迹
$\sum_jc_jM_e^{\rm tr}(t_j)=0$ 的关系是
$$
\mathscr T_p\nu_p
=\sum_jc_jM_e^{\rm tr}(t_j)
       \bigl(h_p(t_j)t_j'-h_p(t)\bigr)\omega\,dt.
\tag{4.3}
$$
因此多出来的是准确的基底微分和极点核，
不是一个可以从原 $T_pF_e=0$ 中删掉的公共因子。
标准模形式 Hecke 的整体归一标量不影响下面的非零结论。

事实上，本题的 (4.2) **确实不为零**。
这可以由实际 CM 同源而非任意函数反例证明。

选一个 $x\in\mathcal C$，使 $M_x(0)\ne0$；
§2 保证这样的标记存在。
在该点 $\nu_p$ 的极点阶准确为 $p+2$，最高系数非零。
取从这个最大 CM 阶纤维出发的任意循环 $p$ 次商。
其目标的局部 CM 阶是 $\mathbb Z_p+p\mathbb Z_{p^2}$。
从该目标出发的 $p+1$ 条循环 $p$ 次同源中，
恰有一条上升回最大 CM 阶，另外 $p$ 条到导子 $p^2$。

这个唯一性可直接从格得到。把目标格缩放成
$\mathcal O_p=\mathbb Z_p+p\mathcal O$，$\mathcal O=\mathbb Z_{p^2}$。
若一个指数 $p$ 的超格 $\Lambda\supset\mathcal O_p$ 的乘法环为
$\mathcal O$，则 $\Lambda$ 是秩一的 $\mathcal O$ 格，
故 $\Lambda=a\mathcal O$。
它必须含由 $\mathcal O_p$ 生成的 $\mathcal O$，而
$[\mathcal O:\mathcal O_p]=p$，于是只能 $\Lambda=\mathcal O$。
其余超格的初等因子给导子 $p^2$。

选择目标全级标记，使这条上升同源运送到原来的标记 $x$；
因 $p\nmid68$，这一步在级结构上可逆。
在这个目标点附近，(4.2) 只有上升支会遇到 $\mathcal C$
中的极点。所有下降支的目标均非最大 CM 阶，因而都正则。
特征零中的同源对应在内点 étale，$c_j$ 和 $t_j'$ 都非零；
唯一的极点支仍有阶数 $p+2$，不能被其余正则支抵消。
所以
$$
\boxed{\mathscr T_p\nu_p\ne0.}
\tag{4.4}
$$
这不否定原权一 Hecke 恒等式，而是准确说明
“乘中央极点核再视作权三形式”这一操作不保持该零关系。

### 4.1 非零 CM 留数使 Hecke 缺陷在上同调中仍非零

以下结论针对原标准 GM 系数 $\mathcal H$；标量 Hecke 规范中的
非零 $p$ 次幂不影响结论。所有上同调均在特征零系数域上取值。
给定 full-level 细模曲线的一个有限 CM 点集 $S$，令
$$
c\in H^1_{\mathrm{dR}}(Y\setminus S,\mathcal H).
$$
假设至少一个 CM 留数 $v_x=\operatorname{Res}_x(c)\in\mathcal H_x$
非零。不对 cusp 或 parabolic 分量作任何非零假设。

**命题。** 对任意奇素数 $\ell$ 不整除固定模层数，$c$ 不能在
扩大到包含全部 Hecke 逆像的开曲线上满足
$$
T_\ell c=\lambda c
$$
（任意标量 $\lambda$）。这同样排除通过加入 exact/Bol 项、
或加入所有 CM 留数均为零的类，把 $c$ 修成这种 Hecke 特征类。
这里不排除纯 parabolic 类；非零 CM 留数是假设的核心。

**证明。** 选择一个有非零留数的 CM 二次域 $K$，并在属于这个域
的非零留数支撑中，令 $r$ 为 CM order 导子的最大 $\ell$ 进指数。
取达到这个最大值的标记 $x$。
存在一个下降的 cyclic $\ell$ 同源，从 $x$ 的底层 CM 曲线通往
导子指数 $r+1$ 的曲线 $y$。调整 $y$ 的 prime-to-$\ell$ 层标记，
使其对偶上升同源在所用的标准 Hecke 标签规范下准确通往标记 $x$。
这是可行且唯一的标签运输，因为同源在固定模层的挠子上可逆。
若工作在固定 Weil-pairing 的连通分支，先应用定义该 Hecke
对应时的固定 determinant 校正；这不改变下面的导子或唯一性。

所需的 CM 格点事实可以直接核对。局部把一个 proper CM 格子
缩放为
$$
\Lambda_a=\mathbb Z_\ell+\ell^a\mathcal O_{K,\ell}.
$$
对 $a\ge1$，它的 $\ell+1$ 个 index-$\ell$ superlattice 中，
准确一个给导子指数 $a-1$，其余 $\ell$ 个给指数 $a+1$。
例如写 $\mathcal O_{K,\ell}=\mathbb Z_\ell+\mathbb Z_\ell\theta$：
上升格子为 $\mathbb Z_\ell+\ell^{a-1}\theta\mathbb Z_\ell$；
其他格子可写为
$$
\mathbb Z_\ell(\ell^{-1}+b\ell^{a-1}\theta)
 +\mathbb Z_\ell\ell^a\theta,\qquad b\bmod\ell.
$$
先乘 $\ell$，再除以单位 $1+b\ell^a\theta$，所得格子的 multiplier
order 正是 $\mathbb Z_\ell+\ell^{a+1}\mathcal O_{K,\ell}$。
在 $a=0$ 时，最多两个 superlattice 为水平格子；$\ell\ge3$
保证至少一个下降格子，所以前一步的 $y$ 总存在。
这也涵盖 split、inert、ramified 的 $K_\ell$；在 ramified 情形
水平格子的个数至多一。

现在 $y$ 的导子指数为 $r+1\ge1$，故它的 $\ell+1$ 个 quotient
中准确一个上升到 $x$，其余全在导子指数 $r+2$。
不同 CM 二次域不能由同源连接；按 $r$ 的定义，这些其他目标处
的留数全部为零。
Hecke 对应的两个 forgetful map 在特征零非 cusp 的细模曲线上
均为 étale，因此局部一形式的留数严格按纤维拉回。
于是
$$
\operatorname{Res}_{y}(T_\ell c)
 =u_\ell\,q_{\mathrm{asc}}^*v_x\ne0,
$$
其中 $u_\ell$ 是选定 Hecke 规范中的非零常数。
同源的 $\mathcal H$ 纤维映射在特征零可逆，最后的不等号成立。
另一方面 $\operatorname{Res}_y(c)=0$，因为 $y$ 的导子指数严格
大于该 CM 域非零留数支撑的最大值。
故两边不可能满足特征关系。
exact 类没有留数；CM 留数全零的类经过对应拉回、推前后仍无
CM 留数，所以两种修补都不能消去这个非零分量。证毕。

**应用于本文实际类。** 这里 $c=[\nu_p]$，$\ell=p$。
前文已经在至少 $9792$ 个实际 CM 标记上证明
$\operatorname{Res}_x(\nu_p)\ne0$，且这些点均为最大 CM order。
取其中一个及其 conductor-$p$ 上升逆像，便得到
$$
\operatorname{Res}_{y}(T_p[\nu_p])\ne0.
$$
所以本文 Hecke 缺陷不仅是某个 meromorphic 代表不为零；
它在 de Rham 上同调中已经非零。
原 weight-one 对象的 $T_p=0$ 因而不能通过追加一个 exact/Bol
修正直接传递给这个中央 principal-part 类。
该结论没有给中央留数 $C_{p+1}/p$ 的新下界：见证非零的是
先前已经明确的其他 CM 标记的留数，而不是原点的中央分量。

## 5. 留数投影保留什么

原标记点所在的 CM 算术轨道是一个固定有限 étale 分量。
在留数直和
$$
\bigoplus_{x\in\mathcal C}H^1_{\rm dR}(E_x)(-1)
$$
中可以保留这一分量；若只在一个固定 $p$ 完成，
也可以继续分成当地 Frobenius 轨道。
这个直和投影不会强行带入 (3.4) 的其它分量。
其在原标记上的实际值仍为 (3.2)，所以
$$
\frac1p\operatorname{Res}_{x_0}\nu_p
=\Gamma_{i,p}\,h_1
\tag{5.1}
$$
正是目标的整中央类。

但从留数直和选择一块，不等于已经选择了一个
既整又保留原 Hecke 的全局提升。
高极点消元、全纯尖形式核和同源运输仍是全局数据；
(4.4) 已证明最直接的实际提升不满足原零 Hecke 关系。
低级 principal-part 模型将其它标记和全纯核移去，
虽准确编码 (5.1)，也不能因此自动继承它们的约束。

Frobenius 在这个留数直和上是 $p$ 倍的纤维 Frobenius，
同时运输 CM 标记。这给一个确切的固定秩接口，
但允许 (5.1) 被任意多的 $p$ 整除。
整化后的其它分量已知非零不解决这个指定分量。
同样，R91 的完整深度 Hermite 数据确实来自原 $M_e$，
却不能仅因每一层有全局提升，就免去本篇展示的全级
整格和 Hecke 交换子。

下一项实际算术任务是将这些交换子或全 CM 轨道的更高关系
用于 (5.1) 及 R81 的全部深度；本篇没有将重述这个任务
登记为中央非零结论。

## 来源

- 原全级截面、全部标签的 Fourier 展开和 Hecke 零关系：
  [R82 完整证明](2026-11-12-actual-weight-one-hecke-and-character-decomposition.md)。
  实际同源的级结构、微分及基底导数：
  [R86 完整证明](2026-11-12-actual-hecke-isogeny-gm-trace.md)。
- M. Bertolini, H. Darmon, K. Prasanna,
  *Generalized Heegner cycles and $p$-adic Rankin L-series*,
  Duke Math. J. 162 (2013), 1033--1148，
  [作者提供的出版版本](https://www.math.mcgill.ca/darmon/pub/Articles/Research/51.BDP1/duke-publishedversion.pdf)，
  §1.1，式 (1.1.9)--(1.1.12)，用于 Hodge 丛的
  Kodaira--Spencer 与权三微分解释。
- M. Allen, L. Long, H. Saad,
  *Atkin and Swinnerton-Dyer congruences for meromorphic modular forms*
  (2025)，[原文](https://arxiv.org/html/2511.05718v1)，
  §3 Lemmas 3.3--3.4 的留数序列及 Frobenius；
  §4 Proposition 4.1、Corollary 4.2 的整消元。
  本篇所需的一层分母界和其尖锐性已在 §3 直接证明，
  不将该文的 ASD 形式递推额外当作本题中心非零定理。
- [首层 Hermite 与完整深度输入](2026-11-12-hermite-central-trace-and-full-depth-neighbor-jets.md)；
  [低级主部/Picard--Fuchs/Bol 比较](2026-11-12-central-principal-parts-pf-bol-residue.md)。
