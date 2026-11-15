# R768 — 同一有限纤维的 normal 留数及原全局极除子

**原来源范围补充（2026-11-15）：本篇 b0>4k+2 必须与 3b0+deg Q(0,Y)≤4r+2 同时成立，故 r≥3k+2；r≤13时k≤3。后续r=1/b0≥3增补为空，不能使用。证明与准确影响见[次数门更正](../notes/2026-11-15-r768-original-fiber-degree-feasibility.md)。**

日期：2026-11-15。**状态：下述真实 normal 留数公式与全局极除子已证明；R766 的指定全局延拓仍未解决。**

继续 R766 的同一个 $d_k$，不换原来源。
在明确的有限纤维门
$\deg_YF(0,Y)>4k+2$
下，$d_k$ 可由 $t=0$ 同一纤维上除 $P$ 外的有限分支直接读取；
其它分支允许非约化，公式不要求全部根简单。

所用核是一个完整多项式 Lagrange 核。
它给原主部泛函的确定局部代表，保原 $w/t$ 因子和 Weierstrass 单位。
这个代表在 $P$ 无极，但作为原
$\omega_C\mathcal N^{-3}$ 的全局有理截面，
至少有 $2\kappa+\chi$ 的极次数，全部出现在原边界。
本篇把这些极和所有十九角保留；没有把局部代表当成已经存在的全局左行。

## 1. 原范围与有限纤维的额外门

保 R765、R766 全部数据和
$$
k<r_F,\quad 0\le k<\ell\le r\le13<h,\quad
N_0=s-13,\quad T=N_0-r,
$$
$$
P^{\rm fact}=qt^rF^3,\qquad
q=d^{-C_D}Q,\quad d=1+8t,\quad
\mathcal N=\mathcal O_C(C).
$$
仍有 $p=6s-1>101$、$f_D<p$、
$F(0,1)=0$、$F_Y(0,1)\ne0$，并且 $C$ 几何整。
本篇另保
$$
\boxed{b_0=\deg_YF(0,Y)>4k+2.}
\tag{1}
$$
不能以 $m=-v_0(F)>4k+2$ 替换 (1)；
加权最低项可能出现在正 $t$ 次数。

令
$$
A=k[t]/t^{k+1},\qquad b=\deg_YF.
$$
原 $p>f_D$ 保 $b<p$。
当 $k=0$ 时，(1) 只是 $b_0\ge3$。

## 2. 全部有限分支的准确 Weierstrass 因子

在 $A[Y]$ 中唯一写成
$$
\boxed{F=\mathfrak u\,W,}
\tag{2}
$$
其中 $W$ 是次数 $b_0$ 的 monic 多项式，
$\mathfrak u$ 是 $A[Y]$ 的单位，且
$$
\deg_Y\mathfrak u\le b-b_0,\qquad
W\bmod t=F(0,Y)/c_0,\qquad
\mathfrak u\bmod t=c_0,
$$
$c_0$ 为 $F(0,Y)$ 的最高系数。

这是整个有限纤维的因子，不只保原 $P$ 分支。
证明可逐 $t$ 阶进行：
在第 $j$ 步，将当前差按 monic $W_0=F(0,Y)/c_0$
唯一作商与余式分解，商改 $\mathfrak u_j$、次数 $<b_0$ 的余式改 $W_j$。
由 $\deg F\le b$，归纳给商次数至多 $b-b_0$。
$\mathfrak u-c_0$ 的系数均在 nilpotent 理想 $(t)$ 中，
故它确实是 $A[Y]$ 的单位。
这个证明不要求 $F(0,Y)$ squarefree。

同一 $\psi$ 在 $A$ 中是 $W$ 的简单根，因此
$$
W(Y)=(Y-\psi)V(Y),\qquad V(\psi)=W_Y(\psi)\in A^\times.
\tag{3}
$$
于是
$$
A[Y]/W\simeq A\times A[Y]/V
\tag{4}
$$
是真整有限代数分裂。
第二项保全部其它有限分支及其非约化结构。

## 3. 完整 Lagrange 核

对任意 monic 多项式 $W$，定义
$$
L(Z,Y)=\frac{W(Z)-W(Y)}{Z-Y}\in A[Z,Y],
$$
$$
\boxed{
K_\psi(Y)=
\left.(Z\partial_Z)^2L(Z,Y)\right|_{Z=\psi}.
}
\tag{5}
$$
$Z$ 在求导时是独立变量；$\psi$ 仅在最后代入。
显然
$$
\deg_Y K_\psi\le b_0-2.
\tag{6}
$$

令 $\operatorname{res}_W(H\,dY/W)$ 为
$H$ 模 $W$ 的余式中 $Y^{b_0-1}$ 的系数。
这就是 monic 有限代数的相对 Grothendieck 留数。
在分裂且根简单时它为 $\sum H(\alpha)/W_Y(\alpha)$，
但本篇不以这个简单根公式作为定义。

对 $\deg R_0<b_0$，准确有多项式恒等式
$$
\operatorname{res}_W
\left(R_0(Y)L(Z,Y)\frac{dY}{W(Y)}\right)=R_0(Z).
\tag{7}
$$
它可在 $Y=\infty$ 展开，或逐 monomial 直接作 monic 除法证明，
在任意系数环 $A$ 上均成立。
对 (7) 作 $(Z\partial_Z)^2$ 得
$$
\boxed{
\operatorname{res}_W
\left(R_0(Y)K_\psi(Y)\frac{dY}{W(Y)}\right)
=(\mathcal E^2R_0)(\psi).
}
\tag{8}
$$

原 canonical 列有 $t^{A_n}$ 因子，
$A_n=\lfloor(n+1)/4\rfloor$。
所以任意原 $R$ 在模 $t^{k+1}$ 后都准确满足
$$
\boxed{\deg_Y(R\bmod t^{k+1})\le4k+2<b_0.}
\tag{9}
$$
$d$ 的逆只改 $t$ 系数，不改这个 $Y$ 次数。
因此 (8) 对全部原来源的这个低截断适用，
不是对一个额外增补的多项式空间适用。

## 4. 原 P 分支消失，normal 行由其它有限分支读取

取同一个 R766 的
$$
R^{(r)}=R-\iota_r(\pi_r(R|_C)),\qquad
u_R=R^{(r)}|_C/(q_0t^r).
$$
因为 $r>k$，在 $A$ 中准确有
$$
R^{(r)}(t,\psi)=0.
$$
(4) 的 $P$ 分支对 (8) 的贡献因此为零。
其它分支的留数可不选根地写为
$$
\operatorname{res}_V
\left(
\frac{R^{(r)}(Y)K_\psi(Y)}{Y-\psi}
\frac{dY}{V(Y)}
\right).
$$
$Y-\psi$ 在 $A[Y]/V$ 中是单位，由 (3) 保证。

**定理 1。** R766 的同一泛函准确为
$$
\boxed{
d_k(\operatorname{pp}_{E'}u_R)
=
\frac{a^2}{2}[w^k]\,
\operatorname{res}_V\left(
\frac{R^{(r)}(t,Y)K_\psi(Y)}{Y-\psi}
\frac{dY}{V(Y)}
\right).
}
\tag{10}
$$
$t=t(w)$ 是原变量变换。
由于 $h>k$，在这个系数中 $g$ 可替为同一 $\psi$；
没有更换任何高 jet 或 Gaussian。

(10) 读取的是其它有限 $t=0$ 分支。
它不把这些分支的值重新赋为独立来源：
$R^{(r)}$ 仍来自整个原 $\mathcal W_D$，
而 $\iota_r$ 的全部高尾照 R766 保留。
其它纤维中的重根、奇点和非约化交都由同一个有限留数代数保留。

## 5. 经原 w/t 和单位校准的局部微分代表

系数提取的准确形式是
$$
[w^k]f(t(w))
=\operatorname{Res}_{t=0}
f(t)\frac{w'(t)}{w(t)^{k+1}}\,dt.
$$
定义原单位低 jet
$$
\ell_k(t)=
\pi_{k+1}^t\left(
\frac{t^{k+1}w'(t)}{w(t)^{k+1}}
\right),
\qquad \ell_k(0)=\tau_0^k.
\tag{11}
$$
在 (2)、(5) 的准确有限代数中令
$$
\boxed{
A_k(t,Y)=
\pi_{k+1}^t\bigl(\mathfrak u(t,Y)K_\psi(Y)\ell_k(t)\bigr),
}
\tag{12}
$$
并取这个唯一次数 $<k+1$ 的 $t$ 多项式代表。
由 (6) 及 (2)，
$$
\deg_t A_k\le k,\qquad
\boxed{\deg_YA_k\le b-2.}
\tag{13}
$$

在 $C$ 的原仿射框中定义确定的有理截面
$$
\boxed{
\omega_0=
\frac{a^2}{2}\,
q\,t^{r-k-1}A_k(t,Y)\,
\frac{dt}{F_Y(t,Y)}.
}
\tag{14}
$$
它在此框中按 $\omega_C\mathcal N^{-3}$ 读取。
把 (14) 与 $u_R$ 相乘后，$qt^ru_R=R^{(r)}|_C$；
同时 $F_Y=\mathfrak u W_Y$ 在 $C$ 上成立，
所以 (11)、(12) 正好还原 (10)。

更精确地，设 $E'_0$ 是 $E'$ 在
$t=0$、有限 $Y$、$Q\ne P$ 的全部局部 Cartier 部分。
则
$$
\boxed{
d_k(\operatorname{pp}_{E'}u)
=
\sum_{Q\in\operatorname{supp}E'_0}
\operatorname{Res}_Q(u\,\omega_0)
\quad(u\in\mathcal U_D).
}
\tag{15}
$$
在奇点使用原 Rosenlicht 分支和；
相对有限留数与曲线留数的相容性也可直接在 (4) 的有限代数上证明，
不需要把每个分支设为独立行。

因 $r-k-1\ge0$ 且 $F_Y(P)\ne0$，
$\omega_0$ 在 $P$ 正则。
在其它有限 $t=0$ 点，$dt/F_Y$ 是原平面 Cartier 曲线的对偶化微分，
$q,A_k,t^{r-k-1}$ 正则，故 (14) 也给正确的正则对偶化局部代表。
表面出现的 $F_Y=0$ 不成为一个遗漏的新仿射极。

若改变 (12) 的代表一个 $t^{k+1}$ 倍，
与 $u$ 相乘并用 $qt^ru=R^{(r)}|_C$ 后，所差留数为零。
所以所需局部类仅由显示的有限原输入决定。

特别，$d_k$ 杀掉在 $E'_0$ 上主部为零的实际元素。
它只依赖这个实际零纤维主部投影；
这没有把该投影换成整个环境主部空间。

## 6. 真正全局极除子：全部原边界仍在

(14) 给一个固定有理截面，但一般不是 R766 要求的
$\mathcal D_T=H^0(C,\omega_C\mathcal N^{-3}(TP))$ 元素。

这里给准确的全局极账本。
原 $\mathcal E=Y\partial_Y$ 保 $\mathcal H_1$，
所以 $e=\mathcal EF|_C$ 是 $\mathcal N$ 的非零全局截面。
记
$$
D_e=\operatorname{div}_C(e),\qquad \deg D_e=\kappa.
$$
令 $\pi:\widetilde C\to C$ 为正规化，
$\Delta_C$ 为 Gorenstein conductor 除子：
$$
\pi^*\omega_C=\omega_{\widetilde C}(\Delta_C),\qquad
\deg\Delta_C=2(p_a(C)-g(\widetilde C)).
$$
在原仿射框中 $e_{\rm aff}=YF_Y$。
将 (14) 乘同一个 $e^3$ 得真正的有理微分
$$
\boxed{
\Omega_0=e^3\omega_0
=
\frac{a^2}{2}\,
q\,t^{r-k-1}A_k\,Y^3F_Y^2\,dt.
}
\tag{16}
$$
所以 (14) 作为原线束有理截面的准确拉回除子为
$$
\boxed{
D(\omega_0)
=\operatorname{div}_{\widetilde C}(\Omega_0)
+\Delta_C-3\pi^*D_e.
}
\tag{17}
$$
其完整极除子为
$$
\boxed{\mathfrak P_0=(-D(\omega_0))_+.}
\tag{18}
$$
(17) 不能把 $D_e$ 的全局框替成一个未校准的仿射 $YF_Y$ 阶；
$D_e$ 使用原 $\mathcal H_1$ 的全部角框。

对任一正规化支 $Q$，(17) 的系数明确为
$$
\begin{aligned}
&v_Q(q)+(r-k-1)v_Q(t)+v_Q(A_k)
+3v_Q(Y)+2v_Q(F_Y)+v_Q(dt)\\
&\hspace{22mm}+(\Delta_C)_Q-3(\pi^*D_e)_Q .
\end{aligned}
\tag{19}
$$
这给每个原角、每个中间例外分量及无穷远的同一精确读取规则。
没有将奇点 conductor 设为零。
$t:\widetilde C\to\mathbf P^1$ 为可分、次数 $b<p$ 的映射，
故每支的分歧指数均小于 $p$：
在有限纤维 $v_Q(dt)=e_Q(t)-1$，
在无穷远 $v_Q(dt)=-e_Q(t)-1$。
因此这里没有正特征导数首项被 $p$ 抹掉的例外。

在原 $t,Y$ 有限且 $d\ne0$ 的仿射开集，
(14) 的系数多项式正则，$dt/F_Y$ 正是对偶化局部生成元。
所以 (18) 在该开集之外才可能非零。
原十九次吹起都在这一补集：
有限 $Y=\infty$ 的三条四链及一条三链、
$d=0,Y=0$ 的二链，以及 $t=\infty$ 的二链。
连同原边界的严格变换，它们包含 (18) 的全部支。
因此没有漏掉一个新的非固定仿射极；
但这些原十九角和无穷远的极全部仍须用 (19) 计算，不能免费删掉。

由 (15) 及 R766 的实际单位 $v_k$，$\omega_0\ne0$。
又
$$
\deg(\omega_C\mathcal N^{-3})=-2\kappa-\chi.
$$
所以 (17)–(18) 给
$$
\boxed{\deg\mathfrak P_0\ge2\kappa+\chi.}
\tag{20}
$$
而 $P$ 不在 $\mathfrak P_0$ 中。
故这个明确局部代表的至少 $2\kappa+\chi$ 极预算全部位于其它原边界。
它本身不能被称为已完成的全局左行。
(20) 是对这个代表的实际极账本，不是说任何允许的全局修正都不可能消极。

## 7. 与 O_T* 的准确全球延拓问题

(15) 给一个确定的局部对偶主部数据：
在 $E'_0$ 使用 (14)，在 $E'$ 的其余部分使用零。
记这个数据为 $\mathfrak d_k$；
它属于原主部空间的留数对偶，
并只在实际 $\mathcal V_{E'}$ 上按 (15) 读取。

R766 的对偶方程
$$
\mathcal O_T^*(\omega)=d_k,\qquad \omega\in\mathcal D_T
$$
准确等价于
$$
\boxed{
\operatorname{res}_{E'}(\omega)+\mathfrak d_k
\in\mathcal V_{E'}^\perp.
}
\tag{21}
$$
这里负号来自
$\operatorname{Res}_P(u\omega)
=-\sum_{E'}\operatorname{Res}_Q(u\omega)$。
$\mathcal V_{E'}^\perp$ 是原**实际**主部像的留数 annihilator，
不是把完整环境数据都任意指定。

所以全局延拓须同时：
在原线束中消掉 (18) 记录的其它边界极；
只在 $P$ 使用允许的 $T$ 阶极；
并满足 (21) 的实际局部同余。
(14) 的仿射正则性和次数界 (13) 不能替代这些要求。

如果真实 $\mathcal Q_T=0$，R766 已证明选定值加 normal 条件可解，
此时 (21) 对非零 $d_k$ 没有解。
因此不能用 Riemann–Roch 维数或“局部核已显式”推断其全球延拓存在。

(1) 失败时，(9) 的原截断多项式不一定低于有限 Weierstrass 次数。
那时 $Y=\infty$ 的分支和原加权零角必须补入留数公式；
本篇不把 (10)、(15) 扩到该范围。
R765、R766 的原全来源结论则完全不依赖 (1)，继续有效。

本篇支付了 $d_k$ 的实际有限纤维代表及其完整边界极账本。
指定 (21) 的解仍未构造，原完整同一个 $R$ 的其它 normal、
两条十三行 carry 及下一位仍保持。

依赖：
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R765](R765-original-zero-angle-and-unavoidable-nonfactor-first-correction.md)；
[R766](R766-actual-principal-part-normal-functional-and-specified-small-obstruction.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R517](R517-actual-tangent-return-full-gamma-transpose-and-ramification-differential.md)。
