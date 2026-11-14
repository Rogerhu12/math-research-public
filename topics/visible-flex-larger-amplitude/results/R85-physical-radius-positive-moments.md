# R85. 同一物理半径候选的真实五矩与径向区间精化

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-12
范围：完整条件工具；其数值应用另外登记。本文不宣称外头真解、全局 Schur 门或最终闭合已经成立。

## 1. 固定对象与两个不同坐标

设原始实源参数为 $x\in[0,1]$，固定度量的实际径向速度为
$g(x)=r_x(x)>0$，实际坡度背景为 $w(x)>0$。定义

$$
R(x)=\int_0^x g(s)\,ds,\qquad W=R(1),\qquad
r(x)=r_L+R(x),\qquad u(x)=\frac{R(x)}W. \tag{85.1}
$$

$u$ 是 [R48](R48-weighted-compatible-outer-interpolation.md) 插值中使用的物理半径坐标
$(r-r_L)/(r_R-r_L)$。一般 $u\ne x$。本文始终保留 (85.1)，并保持原候选的两端物理高度、$h_r$、$h_{rr}$、真实背景及五个精确积分的定义。
R48 的五个非负基函数为：

$$
\phi_{00}=(1-u)^2(1+2u),\quad \phi_{10}=u(1-u)^2,\quad
\phi_{01}=u^2(3-2u),\quad \phi_{11}=u^2(1-u),\quad
\phi_b=u^2(1-u)^2. \tag{85.2}
$$

它们在 $[0,1]$ 非负，在 $(0,1)$ 严格为正。原候选的五矩恰为

$$
I_j=\int_{r_L}^{r_R}w(r)\phi_j\!\left(\frac{r-r_L}W\right)dr
=\int_0^1w(x)g(x)\phi_j\!\left(\frac{R(x)}W\right)dx.
\tag{85.3}
$$

右边只是对同一实积分作严格单调换元。新的包围盒不能用其中心值代替 $I_j$；候选仍用同一未知精确实数 $I_j$。

## 2. 带真实原函数的复合 Taylor 求积定理

设一个原始源小区间为 $[a,b]$，$\Delta=b-a>0$。在该区间上，所有实际分支与绝对值符号已经确定，且 $g,w$ 具有所需阶数的连续导数；它们的区间 Taylor 算法逐阶包含真实导数。记 $p\ge1$，并假定已经有严格有效的盒

$$
R(a)\in A,\qquad R([a,b])\subset B,\qquad W\in\mathcal W\subset(0,\infty).
\tag{85.4}
$$

对任一基点 $\xi\in[a,b]$，用形式变量 $t$ 展开实际函数

$$
x=\xi+\Delta t,\quad G_\xi(t)=\Delta g(\xi+\Delta t),\quad
\mathcal R_\xi(t)=R(\xi)+\sum_{k=0}^{p}\frac{[t^k]G_\xi(t)}{k+1}t^{k+1}.
\tag{85.5}
$$

等式中的有限原函数包含 $R(\xi+\Delta t)$ 的真实 Taylor 系数，至少直到 $p+1$ 阶，因为 $R'=g$。由普通有限级数乘、除、指数等运算形成

$$
F_{j,\xi}(t)=w(\xi+\Delta t)G_\xi(t)
\phi_j\!\left(\frac{\mathcal R_\xi(t)}W\right).
\tag{85.6}
$$

令 $c_{jk}$ 是在点基点 $\xi=a$、$R(a)\in A$ 下的 $[t^k]F_{j,a}$ 包围；令 $D_{jp}$ 是在区间基点 $\xi\in[a,b]$、$R(\xi)\in B$ 下的 $[t^p]F_{j,\xi}$ 包围。所有参数盒均须包含同一固定实源的实际值，而不要求相互独立。则同一真实小区间矩满足

$$
\int_a^b wg\phi_j(R/W)\,dx
\in\sum_{k=0}^{p-1}\frac{c_{jk}}{k+1}
 +\left[-\frac{\sup|D_{jp}|}{p+1},
          \frac{\sup|D_{jp}|}{p+1}\right]. \tag{85.7}
$$

**证明。** 对实际固定参数令
$f_j(x)=w(x)g(x)\phi_j(R(x)/W)$。
(85.5) 的逐阶积分恒等式说明 (85.6) 的 $p$ 阶以内系数恰为
$\Delta^{k+1}f_j^{(k)}(\xi)/k!$；保留 $p+1$ 阶原函数已经足够。
对 $\Delta f_j(a+\Delta t)$ 使用带 Lagrange 余项的 $p-1$ 阶 Taylor 公式，
余项绝对值至多 $\sup|D_{jp}|t^p$。积分 $0\le t\le1$ 即得 (85.7)。
用区间 $B$ 代入原函数的常数项，仅扩大允许参数集合；所有真实中间基点的值仍在其中。
因此这一步没有把独立变量 $x$ 与 $u$ 认同，也没有假定在整区间上 $R$ 是低阶多项式。
$\square$

同样，令 (85.6) 只取 $G_\xi$，便得到真实子宽 $\int_a^b g$ 的余项公式。正性可与 (85.7) 相交；只有相交后存在严格正下端才登记完整正矩。

## 3. 原函数位置与正前后缀

取有理端点的完整有序分割 $0=a_0<\cdots<a_N=1$，逐项得到真实正子宽
$\omega_i=\int_{a_i}^{a_{i+1}}g$ 的盒。另有此前认证的同一总宽 $W$。
于是

$$
R(a_i)\in\left(\sum_{j<i}\omega_j\right)
\cap\left(W-\sum_{j\ge i}\omega_j\right),\qquad
R([a_i,a_{i+1}])\subset
[\inf R(a_i),\sup R(a_{i+1})]. \tag{85.8}
$$

第一式由两个完全相同的精确和给出，第二式由 $g>0$ 的单调性给出。
端点 $R(0)=0,R(1)=W$ 可直接使用其精确恒等式。所有相交必须非空，且源分割必须无遗漏、无重叠。

把 (85.7) 的局部矩相加并与原 $I_j$ 盒相交后，记精确正前缀
$A_j(x)=\int_0^x wg\phi_j(R/W)$。在每个源区间上有

$$
A_j([a_i,a_{i+1}])\subset
[\inf A_j(a_i),\sup A_j(a_{i+1})],\qquad
I_j-A_j([a_i,a_{i+1}])\subset
[\inf(I_j-A_j(a_{i+1})),\sup(I_j-A_j(a_i))].
\tag{85.9}
$$

每个端点前缀同时与“总矩减后缀”相交。因此 (85.9) 包含整个区间内的候选高度，而不只是抽样点。由于 $r_x>0$，完整源分割的像恰为完整物理半径区间；不同盒的浮点端点可以重叠，这不构成真实区间的遗漏。

## 4. 同一候选的真实物理导数与完整缺陷

把更紧的五矩放入原 R48 两端 $C^2$ 兼容构造，只改变已知包围，不改变实际插值系数。其归一斜率 $k(u)$ 仍是原四次多项式，实际高度是它的带权原函数。必须先核原候选的全部端点/背景身份，且新系数与旧系数盒相交；有限整数 Horner 只重写同一多项式。

在某源小区间上，取 (85.8) 给出的 $u$、$r$ 盒，以及同一实源的 $w$、$g=r_x$、$w_x$。实际物理导数由

$$
\frac{du}{dr}=\frac1W,\qquad w_r=\frac{w_x}{g},\qquad
\ell_r=\frac{w_r}w,\qquad
k_r=\frac1W\frac{dk}{du},\qquad
h_{\perp,rr}=w(k_r+\ell_r k) \tag{85.10}
$$

给出。这里在 R64/完整 $J$ 计算中使用的独立变量是物理 $r$，故 $r_r=1$；源 $x$ 仅用于支付背景和正矩的位置盒。不得将 $k_x$ 直接当 $k_r$，也不得将 Darboux 方程右端给出的二阶导数替换 (85.10)。

若每片完整 R64 小均值根、其隐函数导数、$D,L$ 与所有逆分母正性均通过，并保存完整有限 $J$ 的所有频率至两倍高度截断，则所得物理缺陷界覆盖完整真实半径区间。R77 的均值约束可在每片额外收紧零模，但其使用的 $E_{\max},D_{\min},\|D_\perp\|$ 必须来自相同整片盒。此后仍须外 Green/Schur 估计才能得到真实解。

## 5. 当前应用的实际分支范围

`computations/tail_outer_physical_r_true_moments.py` 只接受现有 cell $0$ 的 segment $8$。
它逐项核对真实 `OuterCell` 的完整 profile/integrand 源、原 ready 与候选输入哈希，确认整个源段属于 raw 分支且 $(\log w)_x<0$。原 $\chi=1-S(x)$、$j_0=1+(r_{\mathrm{cut}}/r_{\mathrm{old}}-1)S(x)$、固定校准 $\alpha$、正 warp 权及曲率再分配项全部保留。
它没有使用 cell $10/11$ 的 uncapped 简式，也不把 nominal binary $0.3$ 替换已认证的真实外半径。

此源码不主张覆盖一般跨 cap 分支的物理半径积分；若将来扩展到这种区间，必须先对全部实际分支/临界点完整分割，或对无法分辨的窄条使用完整分支并集与正积分上界。本文 (85.7) 的解析求积只用于分支与符号已经严格确定的区间。
