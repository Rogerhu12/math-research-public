# R176 附录：共同根的实结构、仿射直线与任意实主行的奇次幂

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已复核真实闭域、共同根、全部权/幂及旧范围。
状态：完整证明。普通实主行没有尾率或相位缺陷假设；指数权仍为任意复 $\ell^2$。不排除剩余偶次候选或一般多项式的真实单根核。

## 1. 依赖及新增范围

[R176 谱相交附录](R176-appendix-bounded-part-spectral-intersection-and-common-exceptional-root.md)
已证明：固定实际 first $X_u$ 的全部非零有限谱有界不变部分，
若存在，都共享唯一谱点 $r_u$；
$\mathcal A$ 扰动只按其字符平移此值，
所以任意复指数倾斜共享未倾斜的 $r_u$。

其首位碰撞定理还给：令
$$
u=a_*+\sum_j a_j\chi_j,\qquad a\in\ell^2,\quad a\ne0,
$$
$$
j_0=\min\{j:a_j\ne0\},\qquad \alpha=a_{j_0}\ne0.
$$
若对某个非恒定多项式 $q$、$\lambda\in\mathbb C$、
$m\ge1$ 和复 $\ell^2$ 指数权 $w$，
$$
(q(u)-\lambda)^m e^w
$$
不循环，则 $r_u$ 必存在，且
$$
\boxed{q(r_u)=q(r_u-2\alpha)=\lambda.}
\tag{1.1}
$$
这里是点态幂；已经对多项式 $(q-\lambda)^m$ 使用了完整 Bell 自然域。

本稿用原模型的另一项实际结构——逐点复共轭——
证明实主行的共同根为实数。
这把 (1.1) 的复根候选缩到实根，
并无条件完成实主行的全部奇次幂位移及它们的全部点态幂。

## 2. 逐点复共轭与实际闭域

记
$$
(Jf)(y)=\overline{f(y)}.
$$
这是逐点复共轭，区别于原双线性对称使用的
$Cf(y)=\overline{f(-1-y)}$。

原 $A$ 的权为实数，故
$$
JAJ=A.
\tag{2.1}
$$
因此 $J$ 把闭 $A$ 不变空间双向送到闭 $A$ 不变空间。
实际局部算子
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad N_j=A^{2^j}/d_j
$$
的系数及 $d_j$ 均实，故 $JV_jJ=V_j$。

令
$$
\bar u=\bar a_*+\sum_j\bar a_j\chi_j.
$$
有限 first 截断满足
$$
JX_{u,N}J=X_{\bar u,N}.
$$
对每个有限 Walsh 向量 $f$，R125/R128 的核心收敛使
$X_{u,N}f\to X_uf$；$Jf$ 仍是有限 Walsh 向量。
因此先在这个共同图核心上得到
$JX_uf=X_{\bar u}Jf$，再用两边的核心闭包，得到
$$
\boxed{
J\operatorname{Dom}X_u=\operatorname{Dom}X_{\bar u},
\qquad
JX_uJ=X_{\bar u}.
}
\tag{2.2}
$$
这是真实闭算子及其定义域的等式，不只是有限截断恒等式。

如果 $M$ 是 $X_u$ 的非零有限谱有界部分，
则 $JM$ 是 $X_{\bar u}$ 的同类部分，
且
$$
(X_{\bar u})_{JM}=J(X_u)_M J,\qquad
\sigma((X_{\bar u})_{JM})
=\overline{\sigma((X_u)_M)}.
$$
谱相交附录中的唯一性于是给
$$
\boxed{r_{\bar u}=\overline{r_u}}
\tag{2.3}
$$
只要这些等价的有限谱部分族非空。

特别，当 $a_*,a_j$ 全为实数时，$\bar u=u$，所以
$$
\boxed{r_u\in\mathbb R.}
\tag{2.4}
$$
此处不要求某个具体 $M$ 被 $J$ 保持；
$M$ 与 $JM$ 可以不同，使用的是两者必须共享同一个谱值。
也没有对未知 $M$ 附加通常自伴性。

## 3. 任意实主行的实碰撞集合

现在假设 $a_*,a_j\in\mathbb R$，仍只要求
$a\in\ell^2$、$a\ne0$。
所以 $\alpha\in\mathbb R\setminus\{0\}$。

给任意非恒定复多项式 $q$，定义
$$
\boxed{
\mathcal E_q^{\mathbb R}(\alpha)
=
\{q(t):t\in\mathbb R,\ q(t)=q(t-2\alpha)\}.
}
\tag{3.1}
$$
它是有限集合：
$q(t)-q(t-2\alpha)$ 为次数 $\deg q-1$ 的非零多项式，
所以
$$
|\mathcal E_q^{\mathbb R}(\alpha)|\le\deg q-1.
$$

**定理 3.1。**
对每个
$$
\lambda\notin\mathcal E_q^{\mathbb R}(\alpha),\qquad
m\ge1,
$$
以及任意
$$
w=b_*+\sum_j b_j\chi_j,\qquad b\in\ell^2(\mathbb C),
$$
有
$$
\boxed{(q(u)-\lambda)^m e^w\text{ 非零且循环}.}
\tag{3.2}
$$
若某个候选实际失败，所有权和所有幂的失败仍只能发生在
同一数值 $q(r_u)$。

**证明。**
若输出不循环，R176 的实际 Bell 闭图和循环图核心使相应自然多项式具有非零核。
因此其核上出现一个非零有限谱有界部分，
$r_u$ 已有定义。
(1.1) 与 (2.4) 给
$r_u\in\mathbb R$ 且
$q(r_u)=q(r_u-2\alpha)=\lambda$，
即 $\lambda\in\mathcal E_q^{\mathbb R}(\alpha)$，矛盾。
不存在有限谱部分时，反证在第一步就已完成。
证毕。

直接推论：

- 如果 $q$ 在实轴上单射，则 $\mathcal E_q^{\mathbb R}(\alpha)=\varnothing$，
  所有 $\lambda,m,w$ 均满足 (3.2)。
  $q$ 可以有复系数；这里的单射是映射 $\mathbb R\to\mathbb C$ 的单射。
- 更弱地，只需
  $q(t)\ne q(t-2\alpha)$ 对全部实 $t$ 成立。
- 若 $q$ 没有实根，则 $q(u)^m e^w$ 对全部 $m,w$ 循环，
  即使其非实根之间存在旧 R147 允许的首位间距碰撞。
- 若 $q\in\mathbb R[z]$，则候选均实；
  所以每个非实 $\lambda$ 都满足 (3.2)。

例如，对任意 $p\in\mathbb R[z]$，
$q(t)=p(t)+it$ 在实轴上单射，因为其虚部恰为 $t$。
所以对全部 $\lambda,m,w$，
$$
\bigl(p(u)+iu-\lambda\bigr)^m e^w
$$
非零且循环；不要求 $p$ 单调或具有特定次数。
特别，普通 $u^2+i\tau u-\lambda$ 对每个实 $\tau\ne0$、
每个 $\lambda$ 及全部点态幂/复指数权都循环。

这些推论均直接作用于一个点态多项式；
没有把几个循环点态因子的乘积自动判为循环。

## 4. 全部奇次位移与偶次的唯一显式候选

### 4.1 奇次幂：全部标量位移闭合

令 $k\ge0$。
$t\mapsto t^{2k+1}$ 在实轴上严格递增，
所以对非零实 $\alpha$，
$$
t^{2k+1}\ne(t-2\alpha)^{2k+1}
\qquad(t\in\mathbb R).
$$
定理 3.1 给
$$
\boxed{
\left(u^{2k+1}-\lambda\right)^m e^w
\text{ 非零且循环}
}
\tag{4.1}
$$
对全部 $\lambda\in\mathbb C$、$m\ge1$ 和复 $\ell^2$ 指数权成立。
$k=0$ 已是旧平移幂结论；新增是一般奇次 $2k+1\ge3$ 在所有实 $\ell^2$ 行上的全部候选消失。

例如 $q(t)=t^3$ 的旧复碰撞方程为
$$
t^3=(t-2\alpha)^3
\iff
t=\alpha\pm i\alpha/\sqrt3.
$$
相应 R147 候选是
$$
\lambda=\pm\frac{8i\alpha^3}{3\sqrt3}.
$$
它们不能是实 $r_u$，所以这里也全部排除。
不需要对主行追加双侧幂率、熵预算、非负系数或空谱假设。

### 4.2 偶次幂：仅保留 $\alpha^{2k}$

令 $k\ge1$。
对实 $t,\alpha$，
$$
t^{2k}=(t-2\alpha)^{2k}
\iff
|t|=|t-2\alpha|
\iff
t=\alpha.
$$
因此
$$
\mathcal E_{z^{2k}}^{\mathbb R}(\alpha)=\{\alpha^{2k}\}.
$$
由定理 3.1，
$$
\boxed{
\left(u^{2k}-\lambda\right)^m e^w
\text{ 非零且循环}
\quad\text{只要 }\lambda\ne\alpha^{2k}.
}
\tag{4.2}
$$
对留下的唯一显式候选不作无条件排核。
如果它实际不循环，必有 $r_u=\alpha$。

候选确不能仅凭本定理删掉：
当 $u=\alpha\chi_{j_0}$ 时，
$u^{2k}-\alpha^{2k}=0$ 点态恒成立。
这个有限支撑例子只是说明充分条件的边界，
不是无限慢行存在非零核的证据。

## 5. 同一仿射实线上的主模式

取
$$
u=c+\eta v,\qquad
c\in\mathbb C,\quad \eta\in\mathbb C\setminus\{0\},
$$
其中 $v$ 是非恒定实系数、实常数的 $\ell^2$ first。
设其首位系数为 $\beta\ne0$，
则 $u$ 的首位仍为相同 $j_0$，系数
$$
\alpha=\eta\beta.
$$
实际闭域满足
$X_u=cI+\eta X_v$，
所以有限谱部分族相同，并在非空时
$$
\boxed{r_u=c+\eta r_v\in c+\eta\mathbb R.}
\tag{5.1}
$$
若 $(q(u)-\lambda)^m e^w$ 不循环，
必有某个实 $t$ 使
$$
q(c+\eta t)
=
q(c+\eta(t-2\beta))
=
\lambda.
\tag{5.2}
$$
因此，只要 $t\mapsto q(c+\eta t)$ 在实轴上单射，
就得到全部位移、幂次和指数权的循环性。

特别，
$$
\boxed{
\left((u-c)^{2k+1}-\lambda\right)^m e^w
\text{ 对全部 }\lambda,m,w\text{ 循环},
}
\tag{5.3}
$$
而偶次只需排除
$$
\lambda=\alpha^{2k}.
\tag{5.4}
$$
这里保留了中心 $c$。
若主行只知系数同相位而常数项任意复数，
不能未经 (5.2) 核验就把 $(u-c)^{2k+1}$ 改为未居中的 $u^{2k+1}$。

## 6. 可和复误差给直线约束，但首位必须另行保留

更一般设
$$
u=c+\eta v+h,
$$
其中 $v$ 如 §5，且
$$
h=h_*+\sum_j d_j\chi_j,\qquad d\in\ell^1(\mathbb C).
$$
令
$$
\beta_h=h_*+\sum_j d_j.
$$
实际 $X_h\in\mathcal A$，$\chi(X_h)=\beta_h$。
谱相交附录的有界扰动式给
$$
\boxed{r_u\in \mathcal L:=c+\beta_h+\eta\mathbb R}
\tag{6.1}
$$
只要有限谱部分族非空。

仍假设扰动后的 $u$ 非常数。
令 $\alpha$ 为**扰动后实际 $u$** 的第一个非零系数；
其位置可以比 $v$ 的首位更早。
坏点态多项式仍必须满足
$$
\boxed{
r\in\mathcal L,\qquad
q(r)=q(r-2\alpha)=\lambda.
}
\tag{6.2}
$$
这给一个明确有限候选集
$$
\{q(r):r\in\mathcal L,\ q(r)=q(r-2\alpha)\}.
$$

一般 $\alpha/\eta$ 未必为实数，
于是 $r-2\alpha$ 未必仍在 $\mathcal L$。
所以仅凭 $q$ 在 $\mathcal L$ 上单射，
不能删掉 (6.2) 的候选；
§5 的奇次推论只在实际首位平移沿同一条线时适用。

例如 $q(z)=z^3$ 在 $\mathbb R$ 上单射，
但取
$$
\alpha=1-i/\sqrt3,\qquad r=4/3,
$$
却有
$$
r^3=(r-2\alpha)^3=64/27.
$$
这里 $r-2\alpha$ 不在实轴上。
该算例仅核验几何条件不可省略，不声称存在相应非循环向量。

若另有 $\alpha/\eta\in\mathbb R\setminus\{0\}$，
则两个点均在 $\mathcal L$，
此时确可重新使用沿线单射判据；
中心必须取 $c+\beta_h$。

## 7. 多个主行的线性兼容只在共同部分上使用

还有一项真实但有条件的多变量接口。
设 $u_1,\ldots,u_d$ 是有限个非恒定 $\ell^2$ first，
并且确实存在同一个非零闭 $A$ 不变 $M$，
使每个 $X_i=X_{u_i}$ 在整个 $M$ 上有界且谱有限。
则每个谱都是单点
$$
\sigma((X_i)_M)=\{r_i\},\qquad r_i=r_{u_i}.
$$

R186 的共同混合域给这些有界限制两两交换：
$M$ 被每个 $X_i$ 保持，所以它处在全部有限混合词域中；
在该真实共同域上，自然词交换已成立。
因此
$$
K_i=(X_i)_M-r_iI_M
$$
为有限个交换拟幂零算子。

对任意 $c_0,c_1,\ldots,c_d\in\mathbb C$，
实际线性 first
$X_{c_0+\sum_i c_i u_i}$
在 $M$ 上等于
$c_0I+\sum_i c_i(X_i)_M$，
于是
$$
\boxed{
\sigma\!\left(X_{c_0+\sum_i c_i u_i}|_M\right)
=
\left\{c_0+\sum_i c_i r_i\right\}.
}
\tag{7.1}
$$
当该 first 非恒定时，
唯一性给
$r_{c_0+\sum_i c_i u_i}=c_0+\sum_i c_i r_i$；
恒定情形就是相应标量。

在 $B(M)$ 中取由
$\mathcal A|_M,(X_1)_M,\ldots,(X_d)_M$
生成的含单位交换 Banach 代数。
它有唯一实际字符，取值为
$$
E|_M\longmapsto\chi(E),\qquad
(X_i)_M\longmapsto r_i.
\tag{7.2}
$$
确实，每个生成元减去所列标量都拟幂零，
任意字符必须取这些值；
它们在稠密生成代数上唯一决定字符。
这是在给定 $M$ 上的真实多变量字符。

但几个主行分别存在有限谱部分，不保证这些部分相同或相交。
本稿不从各自 $r_{u_i}$ 已有定义，便无条件写出全部线性组合的加性关系。
如果不存在所假设的共同 $M$，
(7.1)–(7.2) 不能反过来构造它，也不定义整个无界代数的全局字符。

## 8. 与 R147、R150 及后续旧范围的逐项关系

- [R147](R147-exponential-weighted-first-mode-polynomial-cyclicity.md) §1
  只要求复多项式 $q(z)$ 与 $q(z-2\alpha)$ 互素，
  留下由全部复碰撞根产生的有限位移集合。
  它没有实共同根约束；§4.1 明确写出的两个三次复候选
  正是其原判据不能直接删除的点。
- [R150](R150-empty-spectrum-anchor-rectangular-polynomial-cyclicity.md) §1
  需要一个实际空谱锚、首位顺序和矩形最高系数的平移互素。
  任意有正负不可和质量的实主行可以属于全平面谱分支，
  不满足该空谱输入；本稿没有通过形式拆成正负两部分来省掉此条件。
- R134/R138/R155 的空谱相位类早已完成相应单模式多项式，
  不在这里重复登记。
- R259 已处理双侧同幂行的普通简单根多项式；
  R268/R269 及 R236 后续附录又处理相应熵、排序和重数范围。
  本稿在这些行上的交集只记为兼容，
  新结论没有任何排序、衰减、带宽或熵条件。
- R236 最新双池全阶结论处理其预算下的 $F_q+v_c-\lambda$。
  本稿处理普通 $q(u)$，
  并没有重新把已闭的规则晚首偏离列为未知。

剩余偶次临界值、一般实碰撞集合中的实际单根核，
以及两个独立全平面慢方向的普遍排核仍未解决。
